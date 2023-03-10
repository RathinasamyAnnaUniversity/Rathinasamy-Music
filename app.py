import flask
import flask_wtf
import wtforms
from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField
app = Flask(__name__)
app.config['SECRET_KEY'] = 'supersecretkey'
class UploadFileForm(FlaskForm):
        file = FileField("File")
        submit = SubmitField("Upload File")

@app.route('/', methods = ['GET', "POST"])
@app.route('/home', methods = ['GET', "POST"])
def home():
    form = UploadFileForm()
    return render_template('index.html', form = form)

if __name__=='__main__':
    app.run(debug=True)
