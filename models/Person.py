from sqlalchemy import Column, Integer, String, UniqueConstraint

from BotaniBase import BotaniBase, Base

class Person( BotaniBase, Base ):

    id = Column( Integer, primary_key=True )
    first_name = Column( String, nullable=False )
    last_name = Column( String, nullable=False )
    email = Column( String, nullable=False )

    UniqueConstraint( first_name, last_name, email )

    def __repr__( self ):
       return "<Person(first_name='%s', last_name='%s', email='%s')>".format(
           self.first_name, self.last_name, self.email )
