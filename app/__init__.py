from flask import Flask
from app.models import db


app = Flask(__name__)
app.config.from_object('config.Config')
db.init_app(app)
db.create_all(app=app)


from app.controllers.main import main
app.register_blueprint(main, url_prefix='/review')

