
def create_db_session_factory( db_config = None ):

    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from .BotaniBase import Base
    from .Person import Person
    from .Plant import Plant
    from .PlantPhoto import PlantPhoto
    from .PersonPlantRelation import PersonPlantRelation

    engine = create_engine( db_config['SQLALCHEMY_DATABASE_URI'] )
    Base.metadata.create_all( engine )
    return sessionmaker( bind=engine )
