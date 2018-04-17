# manage.py


import unittest

from flask_script import Manager

from server import create_app, db
from server.api.auth.models import User
from server.api.recipe.model import Ingredient
from server.api.preference.models import Allergy
from server.api.preference.models import Preference


app = create_app()
manager = Manager(app)


@manager.command
def test():
    """Runs the unit tests without test coverage."""
    tests = unittest.TestLoader().discover('server/tests', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1


@manager.command
def recreate_db():
    """Recreates a database."""
    db.drop_all()
    db.create_all()
    db.session.commit()


@manager.command
def seed_db():
    """Seeds the database."""
    test_user = User(first_name="First",
         last_name="Last",
         email="test@gmail.com",
         password="11111111"
         )
    test_user.save()

    Ingredient(name="chicken", user_id=test_user.id).save()
    Ingredient(name="apple", user_id=test_user.id).save()
    Ingredient(name="tomato", user_id=test_user.id).save()
    Ingredient(name="turkey", user_id=test_user.id).save()
    Ingredient(name="bean", user_id=test_user.id).save()
    Ingredient(name="lettuce", user_id=test_user.id).save()

    Allergy(name="Test allergy 1", user_id=test_user.id).save()
    Allergy(name="Test allergy 2", user_id=test_user.id).save()

if __name__ == '__main__':
    manager.run()
