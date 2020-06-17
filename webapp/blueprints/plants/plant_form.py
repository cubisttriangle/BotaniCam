from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Email
import email_validator

class PlantForm( FlaskForm ):

    genus = StringField( 'Genus',
                     validators=[ DataRequired() ] )

    species = StringField( 'Species',
                    validators=[ DataRequired() ] )

    common_name = StringField( 'Common Name',
                    validators=[ DataRequired() ] )

    submit = SubmitField( 'Submit' )
