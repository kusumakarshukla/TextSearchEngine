from flask import Flask, flash, request, redirect, url_for,render_template
from werkzeug.utils import secure_filename
import os
import textract
import datetime
import re
app = Flask(__name__)

@app.route("/")
def return_h():
	return render_template("index.html")
UPLOAD_FOLDER = 'data/'
ALLOWED_EXTENSIONS = {'txt', 'pdf'}

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
	search_type= request.form.get("data")
	if search_type==None:
		return "No File Uploaded. Please Upload a txt , pdf , csv or excel file to search"
	if request.method == 'POST':
		
		if 'filename' not in request.files:
			
			flash('No file part')
			
			return "Not uploaded"
		
		file = request.files['filename']
		
		if file.filename == '':
			
			flash('No selected file')
			return redirect(request.url)	
		if file and allowed_file(file.filename):
			filename = secure_filename(file.filename)
			file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
			return redirect('/uploaded_file/{0}/{1}'.format(filename,search_type))

def get_months():
	months_choices = []
	for i in range(1,13):
		months_choices.append( datetime.date(2008, i, 1).strftime('%B'))
	return months_choices
@app.route('/uploaded_file/<filename>/<search>')
def render_file(filename,search):
	text=textract.process('data/'+filename, method='pdfminer')
	text=text.decode('utf-8')
	months=get_months()
	m6=[]
	if search=='date':
		
		pattern1=re.compile("[0-9][0-9]-[0-9][0-9]-[0-9][0-9][0-9][0-9]")
		pattern2=re.compile("[0-9][0-9]/[0-9][0-9]/[0-9][0-9][0-9][0-9]")
		pattern3=re.compile("[0-9][0-9][0-9][0-9]/[0-9][0-9]/[0-9][0-9]")
		pattern4=re.compile("[0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9]")
		pattern5=re.compile("(?:{0})\s*[0-9][0-9]\W\s*[0-9][0-9][0-9][0-9]".format('|'.join(months)))
		pattern6=re.compile("[0-9][0-9]/(?:{0})/[0-9][0-9][0-9][0-9]".format('|'.join(months)))
		pattern7=re.compile("[0-9][0-9]-(?:{0})-[0-9][0-9][0-9][0-9]".format('|'.join(months)))
		pattern8=re.compile("[0-9][0-9]\s*(?:{0})\s*[0-9][0-9][0-9][0-9]".format('|'.join(months)))
		
		
		m1=pattern1.findall(text)
		if len(m1)!=0:
			m6.extend(m1)
		m2=pattern2.findall(text)
		print(m2)
		if len(m2)!=0:

			m6.extend(m2)
			print(m6)
		m3=pattern3.findall(text)
		if len(m3)!=0:
			m6.extend(m3)
		
		m4=pattern4.findall(text)
		if len(m4)!=0:
			m6.extend(m4)
		m5=pattern6.findall(text)
		if len(m5)!=0:
			m6.extend(m5)
		m5=pattern7.findall(text)
		if len(m5)!=0:
			m6.extend(m5)
		m5=pattern8.findall(text)
		if len(m6)!=0:
			m6.extend(m5)
		m5=pattern5.findall(text)
		if len(m5)!=0:
			m6.extend(m5)
		


	return render_template('index.html',text=text,matches=m6)

	
	
if __name__=='__main__':
	app.secret_key = 'ABCD1993'
	app.config['SESSION_TYPE'] = 'filesystem'
	app.run(debug=True)


