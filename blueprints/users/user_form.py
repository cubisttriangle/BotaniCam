from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Email
import email_validator

class UserForm( FlaskForm ):

    first_name = StringField( 'First Name',
                     validators=[ DataRequired() ] )

    last_name = StringField( 'Last Name',
                    validators=[ DataRequired() ] )

    email = StringField( 'Email',
                validators=[ Email( message=( 'Not a valid email address.' ) ), DataRequired() ] )

    submit = SubmitField( 'Submit' )
