from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains import SequentialChain
from langchain.callbacks import get_openai_callback
import os 
import json
import pandas as pd
import traceback
from dotenv import load_dotenv
import PyPDF2


load_dotenv()

key = os.getenv("OPENAI_API_KEY")

llm = ChatOpenAI(openai_api_key = key, model= 'gpt-3.5-turbo', temperature=0.7)

with open(r"C:\Users\Gaurav\OneDrive\Desktop\Projects\LLM Projects\MCQ Generator\MCQ-Generator-Using-LLM\response.json") as f:
    RESPONSE_JSON = json.load(f)


TEMPLATE = """
Text : {text}
You are a expert in MCQ maker. Given the above text, it is your job to create quiz \
of {number} multiple choice question for subject in {tone}. Make sure the questions are not repeated and check all the questions to be conforming.
Make sure to format your response like RESPONSE_JSON below and use it as a guide. \
ensure to make {number} MCQ

### RESPONSE_JSON
{RESPONSE_JSON}
"""


quiz_generation_prompt=PromptTemplate(
    input_variables = ["text", "numbers", "tone", "response_json"],
    template=TEMPLATE
)

quiz_chain = LLMChain(llm=llm, prompt=quiz_generation_prompt, output_key="quiz", verbose=True)


TEMPLATE2 = """
You are an expert english grammarian and writer. Given a Multiple Choice Quiz for {subject} students.\
You need to evaluate the complexity of the question and give a complete analysis of the quiz. Only use at max 50 words for complexity analysis. 
if the quiz is not at per with the cognitive and analytical abilities of the students,\
update the quiz questions which needs to be changed and change the tone such that it perfectly fits the student abilities
Quiz_MCQs:
{quiz}

Check from an expert English Writer of the above quiz:
"""

quiz_evaluation_prompt=PromptTemplate(input_variables=["subject", "quiz"], template=TEMPLATE2)


review_chain=LLMChain(llm=llm, prompt=quiz_evaluation_prompt, output_key="review", verbose=True)


# Combining quiz_chain and review_chain
generate_evaluate_chain=SequentialChain(chains=[quiz_chain, review_chain], input_variables=["text", "number", "subject", "tone", "RESPONSE_JSON"],
                                        output_variables=["quiz", "review"], verbose=True,)


PATH = r"C:\Users\Gaurav\OneDrive\Desktop\Projects\LLM Projects\MCQ Generator\MCQ-Generator-Using-LLM\data.txt"

with open(PATH, 'r', encoding='utf-8') as file:
    TEXT = file.read()
