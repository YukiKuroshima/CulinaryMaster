import datetime
import json
from server import db
from server import login_manager
from flask_login import UserMixin
from server.api.recipe.model import Ingredient


class User(UserMixin, db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(128), nullable=False)
    last_name = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(128), nullable=False, unique=True)
    password = db.Column(db.String(128), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)

    def __init__(self, first_name, last_name, email, password):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.created_at = datetime.datetime.utcnow()

    def save(self):
        """Add user to database"""
        db.session.add(self)
        db.session.commit()

    """
    Get all ingridients for an user

    Returns
    -------
    List of ingridient object
    """
    def get_ingridients(self):
        return Ingredient.query.filter_by(user_id=self.id)

    """
    Add an ingridient

    Parameters
    ----------
    item_name : Str
        Name of ingridient

    """
    def add_ingridient(self, item_name):
        return Ingredient(name=item_name, user_id=self.id).save()

    """
    Remove an ingridient

    Parameters
    ----------
    item_name : Str
        Name of ingridient

    """
    def remove_ingridient(self, item_name):
        Ingredient.query.filter_by(name=item_name, user_id=self.id).first().remove()

    """
    Check if the password given is correct or not
    Correct password is exactly same as the one that is stored in the database

    Parameters
    ----------
    pswd : Str
        Password to be checked. e.q. String that user inputs in the log in page.

    Returns
    -------
    Boolean
        True if the password is same. False if the password is NOT same.
    """
    def is_password_correct(self, pswd):
        return self.password == pswd

    def tojson(self):
        """Represent user data as JSON object"""
        return json.dumps({
                'first_name': self.first_name,
                'last_name': self.last_name,
                'email': self.email,
                'password': self.password
                })

    """
    Get one user based on the email

    Parameters
    ----------
    email : Str
        User's email address that you are looking for

    Returns
    -------
    User
        User object filtered by the email
    """
    @staticmethod
    def get_one_user_by_email(email):
        return User.query.filter_by(email=email).first()

    # callback to reload the user object        
    @login_manager.user_loader
    def load_user(id):
        return User.query.filter_by(id=id).first()
