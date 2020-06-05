from flask import Flask
from blueprints.dashboard import dashboard

app = Flask( __name__ )
app.register_blueprint( dashboard )
