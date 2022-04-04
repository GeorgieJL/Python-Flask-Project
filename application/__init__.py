from flask import Flask

# instantiating a flask application
app = Flask(__name__)

# special directory where we can import stuff
from application import routes

