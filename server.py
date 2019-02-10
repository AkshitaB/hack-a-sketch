import os
import json
from flask import Flask, render_template, request, jsonify, url_for, redirect
from edge_detect import Stroker

UPLOAD_FOLDER = os.path.dirname(os.path.abspath(__file__)) + '/uploads/'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

#@app.route('/')
#def index():
#    return render_template('index.html')

@app.route('/get_contours',methods = ['POST', 'GET'])
def get_contours():
    if request.method == 'POST':
        #data = request.form['data']
        stroker = Stroker()
        data = stroker.detect_edges(dest_path)
        #return redirect(url_for('success',name = user))
    else:
        data = request.form
        #data = request.form['data']
        print(data)
        return jsonify({'testdata':1})

def allowed_file(filename):
   return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def upload_file():
   if request.method == 'POST':
       if 'file' not in request.files:
           print('No file attached in request')
           return redirect(request.url)
       file = request.files['file']
       if file.filename == '':
           print('No file selected')
           return redirect(request.url)
       if file and allowed_file(file.filename):
           filename = file.filename
           dest_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
           file.save(dest_path)
           #return redirect(url_for('index', filename=filename))
           return render_template('result.html', result=dest_path)
           #return jsonify({'contours':data})
   return render_template('index.html')

@app.route('/getpythondata', methods=['GET', 'POST'])
def get_python_data():
    #print(jsdata)
    path = request.args.get('path')
    stroker = Stroker()
    contours = stroker.detect_edges(path)
    return json.dumps({'contours':contours})




if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
