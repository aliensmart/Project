from flask import Flask
from flask_cors import CORS 
from  kpass import setdb
from config import DBPATH

setdb(DBPATH)
app = Flask(__name__)
cors = CORS(app)

from . import routes