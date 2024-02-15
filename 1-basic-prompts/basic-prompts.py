# https://docs.streamlit.io/knowledge-base/tutorials/build-conversational-apps

# import necessary libraries
import os
import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv

# Loads the environment variables including OPENAI_API_KEY from the .env file in the main directory
# NOTE: It's important not to store API keys in Git repos. This is why we are storing it in an ignored .env file.
load_dotenv('../.env')

# Specify the OpenAI model to use
MODEL = "gpt-3.5-turbo" 	# Options "gpt-4", "gpt-3.5-turbo" - Run openai.Model.list() for full list

# Create the OpenAI client
client = OpenAI()

# If no messages exist in the streamlit session, create the default assistant message
if "messages" not in st.session_state:
    st.session_state.messages = [{"role":"assistant", "content": "How can I help you?"}]

# Function to get the assistant's response
def get_assistant_response(messages):
    # Add empty placeholder
    message_placeholder = st.empty()
    # Add empty response string
    full_response = ""
    # Stream responses to chat window
    for response in client.chat.completions.create(
        model=MODEL,
        # Add all collected messages to the completions object
        messages=[{"role": m["role"], "content": m["content"]} for m in messages],
        # Enable streaming so we can see the text as it is generated
        stream=True,
    ):
        # Append each response delta to the full_response
        full_response += (response.choices[0].delta.content or "")
        # Update the message placeholder with the response to date and a "virtual cursor" (purely cosmetic)
        message_placeholder.write(full_response + "|")
    # Replace the streamed message with the final full_response without a cursor, rendering markdown
    message_placeholder.markdown(full_response)
    # Return the response text so we can append it to the message list
    return full_response

# Set the title of the streamlit app
st.title("Welcome to LocalGPT")

# Write out the content for all messages
for message in st.session_state.messages:
    st.chat_message(message['role']).write(message['content'])

# React to chat input
if prompt := st.chat_input():
    # Display user message
	st.chat_message("user").write(prompt)
    # Add user message to chat history
	st.session_state.messages.append({"role":"user", "content": prompt})
    # Get assistant response
	response = get_assistant_response(st.session_state.messages)
    # Add assistant response to chat history
	st.session_state.messages.append({"role":"assistant", "content": response})
