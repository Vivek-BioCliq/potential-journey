from flask import Flask, render_template, request

app=Flask(__name__)

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
        file.save(file_name)
        return f"File {file_name} uploaded successfully"
    
    

if __name__ == '__main__':
    app.run(debug=True)