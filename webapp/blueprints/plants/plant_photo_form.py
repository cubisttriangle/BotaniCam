from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, SubmitField
from wtforms.validators import DataRequired, Email

class PlantPhotoForm( FlaskForm ):

    plant_id = IntegerField( 'Plant',
                     validators=[ DataRequired() ] )

    photo_path = StringField( 'Photo',
                    validators=[ DataRequired() ] )

    submit = SubmitField( 'Submit' )
