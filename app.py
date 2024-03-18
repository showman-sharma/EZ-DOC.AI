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
