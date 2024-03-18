# EZ-DOC.AI

EZ-DOC.AI is a document generation tool that utilizes the Cohere API to generate documents based on user prompts. It provides a convenient way to quickly generate documents by inputting a prompt, which is then processed by the Cohere API to generate a response text.

## Features

- Input a prompt and generate a document based on the provided query.
- Easy-to-use interface for generating documents effortlessly.
- Supports downloading the generated document in .docx format.

## Installation

1. Install Python (if not already installed).
2. Clone this repository:

    ```bash
    git clone https://github.com/your-username/ez-doc-ai.git
    ```

3. Navigate to the project directory:

    ```bash
    cd ez-doc-ai
    ```

4. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Configure the `config/config.json` file with the necessary parameters, such as the Cohere API key.
2. Run the Flask app:

    ```bash
    python app.py
    ```

3. Access the web interface by navigating to `http://localhost:5000/ez_doc_ai` in your web browser.
4. Enter your prompt in the provided text area and click the "Generate" button.
5. Once the document is generated, click the "Download" button to download the document in .docx format.

## Dependencies

- Python 3.x
- Flask
- Cohere API
- Other dependencies (see `requirements.txt`)

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
