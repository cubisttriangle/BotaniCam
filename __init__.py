
def set_db_session( app ):

    from flask import _app_ctx_stack
    from sqlalchemy.orm import scoped_session
    import models
    Session = models.create_db_session_factory()
    app.session = scoped_session( Session, scopefunc=_app_ctx_stack.__ident_func__ )

def register_blueprints( app ):

    from blueprints.dashboard import dashboard
    from blueprints.users import users
    app.register_blueprint( dashboard )
    app.register_blueprint( users )

def load_config( app, app_config ):

    app.config.from_mapping( SECRET_KEY='dev' )

    if app_config is None:
        app.config.from_pyfile( 'config.py', silent=True )
    else:
        app.config.from_mapping( app_config )

def verify_instance_path( app ):

    try:
        import os
        os.makedirs( app.instance_path )
    except OSError:
        pass

def create_app( app_config = None ):

    from flask import Flask

    app = Flask( __name__, template_folder='templates', instance_relative_config=True )

    load_config( app, app_config )
    verify_instance_path( app )
    set_db_session( app )
    register_blueprints( app )

    return app
