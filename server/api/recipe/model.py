import datetime
import json
from server import db

class Ingredient(db.Model):
    __tablename__ = "ingredients"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(128), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)

    def __init__(self, name, user_id):
        self.name = name
        self.user_id = user_id
        self.created_at = datetime.datetime.utcnow()

    def save(self):
        """Add ingredient to database"""
        db.session.add(self)
        db.session.commit()


    def tojson(self):
        """Represent ingredient data as JSON object"""
        return json.dumps({
                'name': self.name,
                'user_id': self.user_id,
                'created': self.created_at
                })
