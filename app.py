from flask import Flask, request, render_template, send_from_directory
import os
import Logic

app = Flask(__name__)

UPLOAD_FOLDER = ""
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/', methods=['GET'])
def index():
    return render_template('PDF-Seiten-Trenner.html')

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    if file:
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(file_path)
        
        Logic.process_pdf(file_path)

       
        return "PDF wurde erfolgreich getrennt!"

if __name__ == '__main__':
    app.run(debug=True)
