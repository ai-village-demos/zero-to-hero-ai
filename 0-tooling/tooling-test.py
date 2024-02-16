import sys
import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv

# Loads the environment variables including OPENAI_API_KEY from the .env file in the main directory
# NOTE: It's important not to store API keys in Git repos. This is why we are storing it in an ignored .env file.
load_dotenv('../.env')

# Create the OpenAI client
client = OpenAI()

# Set the title of the streamlit app
st.title("LocalGPT Configuration Check")
st.write("Checking setup for LocalGPT...")

# Check if we're in a venv
if sys.prefix != sys.base_prefix:
    st.write("Running from a `venv`")

    # Get list of models from the openai API
    model_list = "\n".join(["- {}".format(m.id) for m in client.models.list()])

    # Print the all good message after the checks
    st.write("Everything looks like it's working.")

    # Write the model list to the streamlit app
    st.write("## Available Models")
    st.write(model_list)
else:
    st.write("Virtual environment is not active.")
