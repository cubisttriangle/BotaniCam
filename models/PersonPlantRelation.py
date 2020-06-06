from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, UniqueConstraint

from BotaniBase import BotaniBase, Base

class PersonPlantRelation( BotaniBase, Base ):

    id = Column( Integer, primary_key=True )
    person_id = Column( Integer, ForeignKey( 'Person.id' ), nullable=False )
    plant_id = Column( Integer, ForeignKey( 'Plant.id' ), nullable=False )
    name = Column( String, nullable=False )
    alive = Column( Boolean, server_default='1', nullable=False )

    UniqueConstraint( person_id, plant_id, name )
