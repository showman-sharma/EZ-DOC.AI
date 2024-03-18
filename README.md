# EZ-DOC.AI

EZ-DOC.AI is a document generation tool that provides a convenient web interface for users to generate documents effortlessly. It utilizes the power of the Cohere API for document generation based on user prompts. With EZ-DOC.AI, you can quickly generate documents by simply providing a prompt, making it an ideal tool for various document generation tasks.

## Features

- **Web Interface**: EZ-DOC.AI provides a user-friendly web interface for generating documents.
- **Prompt-Based Generation**: Users can input a prompt into the web interface, and EZ-DOC.AI generates a document based on that prompt.
- **Document Download**: Once the document is generated, users can download it directly from the web interface.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your_username/EZ-DOC.AI.git
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Update configuration:

   Update the `config/config.json` file with your Cohere API key.

4. Run the Flask application:

   ```bash
   python app.py
   ```

5. Access the web interface:

   Open your web browser and navigate to `http://localhost:5000/ez_doc_ai` to access the EZ-DOC.AI web interface.

## Usage

1. Access the EZ-DOC.AI web interface by navigating to `http://localhost:5000/ez_doc_ai`.
2. Enter your prompt into the provided textarea.
3. Click on the "Generate" button to initiate document generation.
4. Wait for the document to be generated. A loading spinner will indicate that the process is ongoing.
5. Once the document is ready, a "Download" button will appear. Click on it to download the generated document.

## Contributing

Contributions to EZ-DOC.AI are welcome! If you have any suggestions, bug reports, or feature requests, please feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

