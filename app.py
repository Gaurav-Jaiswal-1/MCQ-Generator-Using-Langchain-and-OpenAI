import os
import json
import traceback
import pandas as pd
from dotenv import load_dotenv
from src.mcq_generator.utils import read_file, get_table_data
import streamlit as st
from langchain.callbacks import get_openai_callback
from src.mcq_generator.mcqgenerator import generate_evaluate_chain
from src.mcq_generator.logger import logging


# Load environment variables
load_dotenv()

# Reading the response JSON file
with open("Response.json", 'r') as file:
    RESPONSE_JSON = json.load(file)

# Creating a title for the app
st.title("QuizBot Pro: AI MCQ Generator with LangChain")

# Add your Streamlit app code here
with st.form("User input"):
    uploaded_file = st.file_uploader("Upload pdf or text ")

    # How many mcqs does user wnats to generate
    mcq_count = st.number_input("No. of MCQs", min_value = 3, max_value = 50)

    # Enter the subject
    subject = st.text_input("Enter the Subject", max_chars=20)

    # Add tone(Difficulty level)
    tone = st.text_input("Difficulty level of questions", max_chars=20, placeholder="simple")

    #Button to create MCQs
    button = st.form_submit_button("Create MCQs")

    if button and uploaded_file is not None and mcq_count and subject and tone:
        with st.spinner("Loading..."):
            try:
                text = read_file(uploaded_file)
                #Count tokens and API calls
                with get_openai_callback() as cb:
                    response=generate_evaluate_chain({
                        "text": text,
                        "number": mcq_count,
                        "subject":subject,
                        "tone": tone,
                        "RESPONSE_JSON": json.dumps(RESPONSE_JSON)
                    })
            except Exception as e:
                traceback.print_exception(type(e), e, e.__traceback__)
                st.error("Error")

            else:
                print(f"Total Tokens:{cb.total_tokens}")
                print(f"Prompt Tokens:{cb.prompt_tokens}")
                print(f"Completion Tokens:{cb.completion_tokens}")
                print(f"Total Cost:{cb.total_cost}")
                if isinstance(response,dict):
                    #Extract the quiz data drom the response
                    quiz = response.get("quiz",None)
                    if quiz is not None:
                        table_data = get_table_data(quiz)
                        if table_data is not None:
                            df = pd.DataFrame(table_data)
                            df.index = df.index+1
                            st.table(df)
                            # Display the review in the text box
                            st.text_area(label="Review", value=response["review"])
                        else:
                            st.error("Error in the table data")

                    else:
                        st.write(response)

