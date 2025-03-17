import os
import streamlit as st
import google.generativeai as genai
from constant import google_api_key
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SequentialChain
from langchain.memory import ConversationBufferMemory
from langchain_google_genai import ChatGoogleGenerativeAI

# Set up the Google API key
os.environ["GOOGLE_API_KEY"] = google_api_key
genai.configure(api_key=google_api_key)

# Streamlit framework
st.title('Celebrity Search Results')
input_text = st.text_input("Search the celebrity you want")

# Initialize the Gemini LLM with LangChain
llm = ChatGoogleGenerativeAI(model="gemini-1.5-pro-latest", temperature=0.8) ##model="gemini-1.5-pro-latest" can be changed according to time

# Prompt Templates
person_prompt = PromptTemplate(
    input_variables=['name'],
    template="Tell me about celebrity {name}"
)

dob_prompt = PromptTemplate(
    input_variables=['person'],
    template="When was {person} born?"
)

events_prompt = PromptTemplate(
    input_variables=['dob'],
    template="Mention 5 major events that happened around {dob} in the world"
)

# Memory Buffers to store conversation history
person_memory = ConversationBufferMemory(input_key='name', memory_key='chat_history')
dob_memory = ConversationBufferMemory(input_key='person', memory_key='chat_history')
events_memory = ConversationBufferMemory(input_key='dob', memory_key='events_history')

# Chains to handle each query step
person_chain = LLMChain(
    llm=llm, prompt=person_prompt, output_key='person', memory=person_memory, verbose=True
)

dob_chain = LLMChain(
    llm=llm, prompt=dob_prompt, output_key='dob', memory=dob_memory, verbose=True
)

events_chain = LLMChain(
    llm=llm, prompt=events_prompt, output_key='events', memory=events_memory, verbose=True
)

# Sequential Chain to link all steps
parent_chain = SequentialChain(
    chains=[person_chain, dob_chain, events_chain],
    input_variables=['name'],
    output_variables=['person', 'dob', 'events'],
    verbose=True
)

# Process user input
if input_text:
    result = parent_chain({'name': input_text})

    # Extract results
    person_info = result['person']
    dob_info = result['dob']
    events_info = result['events']

    # Display results
    st.subheader("Celebrity Information:")
    st.write(person_info)

    st.subheader("Date of Birth:")
    st.write(dob_info)

    st.subheader("Major Events:")
    st.write(events_info)

    # Expander to show additional details
    with st.expander('Person Details'): 
        st.info(person_memory.buffer)

    with st.expander('Major Events Around DOB'): 
        st.info(events_memory.buffer)
