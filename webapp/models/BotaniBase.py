from sqlalchemy.ext.declarative import declarative_base, declared_attr

Base = declarative_base()

class BotaniBase( object ):

    @declared_attr
    def __tablename__( cls ):
        return cls.__name__
