"""
EZ-DOC.AI: Document Generation with Cohere

This script utilizes the Cohere API to generate documents based on user prompts. It allows users to input a prompt,
which is then processed by the Cohere API to generate a response text, providing a convenient way to quickly generate documents.

Author: [Your Name]
Date: [Current Date]

Usage:
1. Install required dependencies: pip install cohere
2. Update the 'config/config.json' file with the necessary parameters, such as the API key.
3. Initialize an instance of the Doc_Generator class with the appropriate configuration file path.
4. Use the QA_bot method of the Doc_Generator class to generate documents by providing a query prompt.

Dependencies:
- Cohere API

Example:
```python
from ezdocai import Doc_Generator

# Initialize Doc_Generator instance
generator = Doc_Generator()

# Provide a prompt for document generation
prompt = "Please provide a summary of the project goals."

# Generate document based on the prompt
response_text = generator.QA_bot(prompt)

print(response_text)
```

Note: Ensure that you have the appropriate permissions and API key for using the Cohere API.

"""

import cohere
import json
from docx import Document

class Doc_Generator:
    """
    A class for generating documents using the Cohere API based on user prompts.
    """

    def __init__(self, config_path='config/config.json'):
        """
        Initializes the Doc_Generator.

        :param config_path: Path to the configuration file (default is 'config.json').
        """
        self.config_path = config_path
        self.api_key = None
        self.co = None
        self.service_query = None
        self.output_file = None
        self.config = None

        self.load_config()
        self.initialize_cohere()

    def initialize_cohere(self):
        """
        Initializes the Cohere client using the provided API key.
        """
        print("Initializing Cohere client...")
        self.co = cohere.Client(self.api_key)
        print("Cohere client connected successfully!")

    def load_config(self):
        """
        Loads configuration from the specified file.
        """
        print("Loading configuration...")
        with open(self.config_path) as config_file:
            config = json.load(config_file)
            self.config = config
            self.api_key = config['api_key']
            self.output_file = self.config.get('output_file', "temp/OUTPUT_FILE.docx")
        print("Configuration loaded successfully.")

    def generate_docx(self,text):
        # Create a new Document
        doc = Document()
        
        # Add the text to the Document
        doc.add_paragraph(text)
        
        # Save the Document
        doc.save(self.output_file)    

    def QA_bot(self, query):
        """
        Uses the Cohere API for question-answering.

        :param query: The query prompt for generating the document.
        :return: The response text generated by the QA bot.
        """
        print("Running QA_bot...")

        print(f"Co.chat begins")

        query = 'Create a well formatted text output for a .docx file based on the following query: \"{0}\"'.format(query)

        response = self.co.chat(
            message=query,
            connectors=[{"id": "web-search"}],
            model='command-r'
        )
        print(f"Co.chat completed")

        print("__________________________________________")
        print("RESPONSE:")
        print(response.text)
        print("__________________________________________")

        self.generate_docx(response.text)
        
        return response.text
        


               


