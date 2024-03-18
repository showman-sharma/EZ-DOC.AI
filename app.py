"""
EZ-DOC.AI Flask Application

This Flask application provides a web interface for generating documents using the EZ-DOC.AI system. It utilizes the EZ-DOC.AI backend,
which employs the Cohere API for document generation based on user prompts.

Author: V S S Anirudh Sharma
Date: 18th March 2024

Usage:
1. Ensure that the EZ-DOC.AI backend is properly configured and running.
2. Access the EZ-DOC.AI web interface through the specified endpoint to generate documents.
3. Input a prompt into the web interface and click on the "Generate" button to initiate document generation.
4. Once the document is generated, click on the "Download" button to download the generated document.

Endpoints:
- /ez_doc_ai: Renders the EZ-DOC.AI web interface for document generation.
- /generate_docx: Accepts POST requests with user prompts and returns the generated document text.
- /download_docx: Returns the generated document file for download.

Dependencies:
- Flask: Web framework for Python
- ezdocai: EZ-DOC.AI backend for document generation

"""

from flask import Flask, request, jsonify, render_template, send_file
from ezdocai import Doc_Generator

app = Flask(__name__)
doc_generator = Doc_Generator()
output_path = "temp/OUTPUT_FILE.docx" 

@app.route('/ez_doc_ai')
def index():
    return render_template('index.html')

@app.route('/generate_docx', methods=['POST'])
def generate_docx():
    data = request.form['prompt']
    response_text = doc_generator.QA_bot(data)
    return jsonify({"response": response_text})

@app.route('/download_docx', methods=['GET'])
def download_docx():
    return send_file(output_path, as_attachment=True, download_name='output.docx', mimetype='application/vnd.openxmlformats-officedocument.wordprocessingml.document')

if __name__ == "__main__":
    app.run(debug=True)