from flask import Flask, flash, request, redirect, url_for,render_template
from werkzeug.utils import secure_filename
import os



app = Flask(__name__)

@app.route("/")
def return_h():
	return render_template("index.html")
UPLOAD_FOLDER = 'data/'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def read_pdf(filename):
	print("I am here")
	fd = open(filename, "rb")
	viewer = SimplePDFViewer(fd)
	viewer.render()
	return viewer.render()


@app.route('/')
def hello():
	return render_template("index.html")
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
@app.route('/file', methods=['GET', 'POST'])
def upload_file():	
	print(request.method)
	if request.method == 'POST':
		print("hi ")
		# check if the post request has the file part
		print(request.files)
		if 'filename' not in request.files:
			print("NO FILE")
			flash('No file part')
			print(request.url)
			return "Not uploaded"
		print(request.files)
		file = request.files['filename']
		print(file)
		# if user does not select file, browser also
		# submit an empty part without filename	
		if file.filename == '':
			print("No file")
			flash('No selected file')
			return redirect(request.url)	
		if file and allowed_file(file.filename):
			filename = secure_filename(file.filename)
			file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
			return redirect('/uploaded_file/{0}'.format(filename))
@app.route('/uploaded_file/<filename>')
def render_file(filename):
	return filename
	filename=request.args['filename']
	print(filename)
if __name__=='__main__':
	app.secret_key = 'ABCD1993'
	app.config['SESSION_TYPE'] = 'filesystem'
	app.run(debug=True)


