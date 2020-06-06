from sqlalchemy import Column, Integer, String, UniqueConstraint

from BotaniBase import BotaniBase, Base

class Plant( BotaniBase, Base ):

    id = Column( Integer, primary_key=True )
    genus = Column( String )
    species = Column( String )
    common_name = Column( String )

    UniqueConstraint( genus, species )

    def __repr__( self ):
       return "<Plant(genus='%s', species='%s', common_name='%s')>".format(
           self.genus, self.species, self.common_name )
