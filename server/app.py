from flask import Flask
from flask_migrate import Migrate
from models import db
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("FLASK_SQLALCHEMY_DATABASE_URI")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config.from_prefixed_env()

db.init_app(app)
 
migtation  = Migrate(app,db) 





if __name__ == "__main__":
    app.run(debug=True)