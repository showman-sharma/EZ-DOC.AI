# EZ-DOC.AI

EZ-DOC.AI is a document generation tool powered by the Cohere API. It allows users to generate documents effortlessly by providing a prompt. The prompt is processed by the Cohere API, which generates a response text that can be saved as a .docx file.

## Features

- Generate documents quickly and easily by providing a prompt.
- Utilizes the Cohere API for accurate and contextually relevant document generation.
- Supports various prompt types, including questions, summaries, and more.
- Download the generated document in .docx format for further use.

## Installation

1. Install the required dependencies using pip:
   ```
   pip install cohere
   ```

2. Clone this repository:
   ```
   git clone https://github.com/yourusername/ez-doc-ai.git
   ```

3. Update the configuration file `config/config.json` with your Cohere API key.

## Usage

1. Run the Flask web application:
   ```
   python app.py
   ```

2. Access the application in your web browser at `http://localhost:5000/ez_doc_ai`.

3. Enter your prompt in the text area provided and click the "Generate" button.

4. Once the document is generated, click the "Download" button to save it as a .docx file.

## Demo Video

Watch the demo video below to see EZ-DOC.AI in action:

[![Demo Video](demo/ezdocai_poc_demo.mp4)](demo/ezdocai_poc_demo.mp4)

## Contributors

- V S S Anirudh Sharma

## License

This project is licensed under the [MIT License](LICENSE).