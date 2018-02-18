from flask import Flask
from flask_mail import Mail

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Dont share'
app.config['MAIL_SERVER'] = 'smtp.mailtrap.io'
app.config['MAIL_PORT'] = '465'
app.config['MAIL_USERNAME'] = 'jonsouthy'
app.config['MAIL_PASSWORD'] = 'Johnnykid1'

mail = Mail (app)
from app import views