from flask import Flask

def create_app( app_config = None ):

    app = Flask( __name__, instance_relative_config=True )
    app.config.from_mapping( SECRET_KEY='dev' )

    if app_config is None:
        app.config.from_pyfile( 'config.py', silent=True )
    else:
        app.config.from_mapping( app_config )

    # ensure the instance folder exists
    try:
        import os
        os.makedirs( app.instance_path )
    except OSError:
        pass

    from blueprints.dashboard import dashboard
    app.register_blueprint( dashboard )

    return app
