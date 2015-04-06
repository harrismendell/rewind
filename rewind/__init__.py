from flask import Flask
from flask.ext.login import LoginManager
app = Flask(__name__)
login_manager = LoginManager()
login_manager.init_app(app)
# use for encrypt session
app.config['SECRET_KEY'] = 'SET T0 4NY SECRET KEY L1KE RAND0M H4SH'
import rewind.views