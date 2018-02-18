from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.validators import InputRequired

class Rform(FlaskForm):
    name = StringField('Name',validators=[InputRequired()])
    email = StringField('E-Mail',validators=[InputRequired()])
    subject = StringField('Subject',validators=[InputRequired()])
    message = StringField('Message',validators=[InputRequired()])