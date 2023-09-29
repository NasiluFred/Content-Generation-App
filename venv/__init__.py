import os
from flask import Flask
from config import Config
import requests
import cohere  

#Inject Flask magic
app = Flask(__name__)

#load configurations
app.config.from_object( Config)

# import routing to render the pages

#from myenv.myflaskapp import views
