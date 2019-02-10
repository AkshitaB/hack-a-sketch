import os
from flask import Flask, render_template, request, jsonify, url_for
#from flask import Flask, flash, request, redirect, url_for
from edge_detect import Stroker

UPLOAD_FOLDER = '/tmp/images'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_contours',methods = ['POST', 'GET'])
def get_contours():
    if request.method == 'POST':
        data = request.form['data']
        #return redirect(url_for('success',name = user))
    else:
        data = request.form
        #data = request.form['data']
        print(data)
        return jsonify({'testdata':1})


@app.route('/upload_file', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return jsonify({'done':1})
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    '''


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
