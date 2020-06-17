from sqlalchemy import Column, Integer, String, ForeignKey, UniqueConstraint

from .BotaniBase import BotaniBase, Base

class PlantPhoto( BotaniBase, Base ):

    id = Column( Integer, primary_key=True )
    plant_id = Column( Integer, ForeignKey( 'Plant.id' ), nullable=False )
    photo_path = Column( String, nullable=False )

    UniqueConstraint( plant_id, photo_path )

    def __repr__( self ):
       return "<PlantPhoto(plant_id='{}', photo_path='{}')>".format(
           self.plant_id, self.photo_path )

