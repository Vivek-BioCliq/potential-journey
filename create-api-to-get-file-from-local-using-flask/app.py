from flask import Flask, render_template, request, send_file
from pymongo import MongoClient
# from dotenv import load_dotenv
import os
from io import BytesIO
import yaml

app=Flask(__name__)

# load_dotenv()

with open('test.yml', 'r') as f:
    test = yaml.safe_load(f)
    
print(test)
print(test['name'])

# MONGO_URI= os.environ.get('mongo_uri')
MONGO_URI = test['mongo_uri']
client = MongoClient(MONGO_URI)
db= client['practice1']

uploaded_files= db['files']


@app.route('/')
def fun():
    return "Hello, Vivek here!"


@app.route('/upload')
def get_file():
    return render_template('index.html')

@app.route('/upload-file', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return "No file found", 400 
    
    file= request.files['file']
    file_name= file.filename
    
    if(file_name==""):
        return "File name not found", 400
    
    if file:
        file_data = file.read()
        inserted_file = uploaded_files.insert_one({
            'filename': file.filename,
            'data': file_data
        })

        return f"File {file_name} uploaded and saved in the database with id: {inserted_file.inserted_id}"
    
@app.route('/files')
def show_files():
    files = uploaded_files.find({}, {'filename': 1})  
    return render_template('files.html', files=files)

@app.route('/download/<filename>')
def download_file(filename):
    file_data = uploaded_files.find_one({'filename': filename}) 
    if file_data:
        data = file_data['data']
        return send_file(BytesIO(data), as_attachment=True, download_name=filename)

    else:
        return "File not found", 404
    

if __name__ == '__main__':
    app.run(debug=True)