import os
from dotenv import load_dotenv, find_dotenv
basedir = os.path.abspath(os.path.dirname(__file__))
dotenv_File = find_dotenv('microblog.flaskenv')
if dotenv_File:
    load_dotenv(dotenv_File)
    print ("Found dotenv_File", dotenv_File)
else:
    print (dotenv_File)
    print ("Could not find dotenv_File")

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-can-never-guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = int(os.environ.get('MAIL_PORT') or 25)
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') is not None
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    ADMINS = ['michaelgordoncase@gmail.com']
    
