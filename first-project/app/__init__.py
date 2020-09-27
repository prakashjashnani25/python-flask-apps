from flask import Flask

app = Flask(__name__,instance_relative_config=True)

from . import views

#Load the Config Object
app.config.from_object('config')
