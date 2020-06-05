from flask import Flask
from blueprints.dashboard.dashboard import blueprint as dashboard

app = Flask( __name__ )
app.register_blueprint( dashboard )
