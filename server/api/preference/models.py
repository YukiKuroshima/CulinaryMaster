import datetime
import json
from server import db

class Allergy(db.Model):
    __tablename__ = "allergy"
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

    def remove(self):
        """Delete ingredient to database"""
        db.session.delete(self)
        db.session.commit()

    def tojson(self):
        """Represent ingredient data as JSON object"""
        return json.dumps({
                'name': self.name,
                'user_id': self.user_id,
                'created': self.created_at
                })

class Preference(db.Model):
    __tablename__ = "preference"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    diet_pref = db.Column(db.String(128), nullable=False)
    personal_pref = db.Column(db.String(128), nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)

    def __init__(self, diet_pref, personal_pref, user_id):
        self.diet_pref = diet_pref
        self.personal_pref = personal_pref
        self.user_id = user_id
        self.created_at = datetime.datetime.utcnow()

    def save(self):
        """Add ingredient to database"""
        db.session.add(self)
        db.session.commit()

    def remove(self):
        """Delete ingredient to database"""
        db.session.delete(self)
        db.session.commit()

    def tojson(self):
        """Represent ingredient data as JSON object"""
        return json.dumps({
                'diet_pref': self.diet_pref,
                'personal_pref': self.personal_pref,
                'user_id': self.user_id,
                'created': self.created_at
                })

