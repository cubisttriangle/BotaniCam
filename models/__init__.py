
def create_db_session_factory( db_config = None ):

    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from BotaniBase import Base
    from Person import Person
    from Plant import Plant
    from PersonPlantRelation import PersonPlantRelation

    if db_config is None:

        engine = create_engine( 'sqlite:///:memory:' )
        Base.metadata.create_all( engine )
        return sessionmaker( bind=engine )

    return None
