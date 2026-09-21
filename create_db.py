from database import database, app
from database.models import Usuario

with app.app_context():
    database.create_all()
    