# MCQ-Generator-Using-Langchain and OpenAI


# MCQ Generator Using OpenAI and LangChain

Welcome to the **MCQ Generator** repository! This project harnesses the capabilities of OpenAI's language models and the LangChain framework to generate multiple-choice questions (MCQs) from any topic provided as a PDF file. The tool is designed to assist educators, students, and content creators by automating the creation of MCQs, ensuring a wide range of subjects and difficulty levels can be catered to.

## Features

- **PDF Input Support**: Upload a PDF file containing content on any topic, and the generator will extract relevant information to create questions.
- **Subject-Specific Questions**: Specify the subject of interest, and the tool will focus on generating questions relevant to that topic.
- **Adjustable Difficulty Levels**: Set the tone for the desired difficulty level, ranging from easy to challenging, to match the target audience's needs.
- **High-Quality MCQs**: Utilize OpenAI's advanced language models to produce well-structured questions and plausible answer choices.
- **Seamless Integration with LangChain**: Leverage LangChain's framework to streamline the question generation process, ensuring clarity and relevance.

## Getting Started

Follow these steps to get started with the MCQ Generator:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/mcq-generator.git
   cd mcq-generator
   ```

2. **Install Dependencies**:
   Ensure you have Python installed, then install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set Up OpenAI API Key**:
   You'll need an OpenAI API key to access the language models. Set your API key as an environment variable or include it in the configuration file.

4. **Run the Generator**:
   Use the provided script to generate MCQs:
   ```bash
   python generate_mcqs.py --input_file "path/to/your.pdf" --subject "Biology" --difficulty "medium"
   ```

## Customization and Usage

- **Customizable Input**: The tool accepts any PDF file as input, making it versatile for different content types.
- **Subject and Difficulty Specification**: Users can specify the subject area and difficulty level to tailor the MCQs to their needs.
- **Output Formats**: The generated questions can be output in various formats, including JSON, CSV, or plain text, suitable for integration into educational platforms or quizzes.

## Contributing

We welcome contributions to enhance the MCQ Generator! If you have suggestions for new features, improvements, or bug fixes, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

Special thanks to OpenAI for their language models and to the LangChain contributors for facilitating efficient language processing.

---

This description provides a comprehensive overview of the project, including features, setup instructions, and contribution guidelines. You can adjust the specifics as needed to fit your project's details.

'''
To create virtual environment use - 
- conda create -p env python=3.11.4 -y
                or
- python -m venv env

To activate virtual environment use - 
 - .\env\Scripts\activate
'''


'''
write your requirements in requirements.txt file and run -
- pip install -r requirements.txt
'''

'''
To check all the libraries use - 
- pip list
'''

''' 
If you have any issues with kernels for jupyter notebook use -
- pip install ipykernel
'''


'''
For Github

- git init # If you are not cloning

- git add .

- git commit -m "Message" # Message is mandatory(type any message you want)

- git remote add origin https:/(your git hub repo link)

- git push -f origin main 

- git status # to check the current status

- git config --global

'''







