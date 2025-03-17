
# Celebrity Search Application

This Streamlit-based application allows users to search for information about celebrities, including their background, date of birth, and major historical events that occurred around the time of their birth. The application incorporates Google's Gemini LLM (via LangChain) to generate the responses.



## Features

1.Celebrity Information: Provides a detailed description of the celebrity based on the user's input.

2.Date of Birth: Displays the date of birth of the searched celebrity.

3.Historical Events: Lists 5 major events that happened around the time of the celebrity's birth.

4.Conversation Memory: Stores and displays the conversation history for both the celebrity details and historical events.
## Prerequisites

Before running the application, ensure you have the following:

1.Python 3.7 or higher installed.(Used python version -3.12.7)

2.Google API Key: You need a valid Google API key to use the Gemini LLM. Store the key in a constant.py file as google_api_key.
For Api key =https://ai.google.dev/

3.Required Python libraries installed (see Installation below).

## Installation

1.Clone the repository or download the code.

2.Install the required Python libraries using pip:

pip install streamlit google-generativeai langchain langchain-google-genai

3.Create a constant.py file in the same directory as the script and add your Google API key:

google_api_key = "your_google_api_key_here"
## Code Structure

- Google API Setup: The script configures the Google API key and initializes the Gemini LLM.

- Streamlit Interface: Provides a simple text input for the user to search for a celebrity.

- Prompt Templates: Define the structure of the queries sent to the LLM.

- Memory Buffers: Store conversation history for better context management.

- LLM Chains: Handle the sequential processing of the celebrity information, date of birth, and historical events.

- Sequential Chain: Links all the chains together to process the user's input and generate the final output.
## Screenshots

![App Screenshot](https://imgur.com/nIdOhL5.png)

![App Screenshot](https://imgur.com/kawgkvi.png)

![App Screenshot](https://imgur.com/Hi1mXQj.png)

![App Screenshot](https://imgur.com/CavOn2X.png)


## Acknowledgments

- **Streamlit**: For the web application framework.

- **Google Gemini LLM**: For enabling advanced language model capabilities to generate accurate and insightful responses, made accessible through the Gemini API key.

- **LangChain**: For simplifying the integration with LLMs and managing conversation memory.

