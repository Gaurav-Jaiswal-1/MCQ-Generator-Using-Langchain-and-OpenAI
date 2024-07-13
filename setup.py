from setuptools import find_packages, setup

setup(

    name = "MCQ Generator",
    version = "0.0.1",
    author = "Gaurav Jaiswal",
    author_email= "jaiswalgaurav863@gmail.com",
    install_requirements = ["openai", "langchain", "streamlit", "python-dotenv", "PyPDF2"],
    packages=find_packages()

)