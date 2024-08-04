from flask import Flask
from flask_pymongo import PyMongo
import os

app = Flask(__name__)


SECRET_KEY = os.environ.get('SECRET_KEY') or "ajajajjsjsjajjajaaw333"

#app configuration
app_settings = os.environ.get(
    'APP_SETTINGS'
    'app.config'
) 
app.config.from_object(app_settings)


#connecting to database
MONGO_URI = "mongodb+srv://fabulous95:Skyview95.ii@cluster0.nz9zg.mongodb.net/MissingPetsLocator?retryWrites=true&w=majority"

#initializing PyMongo
mongo = PyMongo(app, MONGO_URI)

from app import views
from app import admin 
