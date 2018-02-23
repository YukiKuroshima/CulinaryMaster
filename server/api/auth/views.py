from flask import Blueprint, jsonify, request, render_template, \
        session, redirect, url_for
from sqlalchemy import exc
from server.api.auth.models import User
from server import db
from server.api.auth.forms import SignupForm, LoginForm
from sqlalchemy.exc import IntegrityError
from flask_login import login_user, login_required, logout_user


auth_blueprint = Blueprint('auth', __name__, template_folder='./templates')


@auth_blueprint.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify({
        'status': 'success',
        'message': 'pong!'
    })


@auth_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        # TODO
        # Find user by email. 'Using User.get_one_user_by_email'
        temp = User.get_one_user_by_email(form.email.data)
        # If no user found
        if temp is None:
            # Add error message to form.email.errors
            form.email.errors.append('No accound found')
        # else
        else:
            # Check if the password is correct. Using is.password_correct()
            # if correct
            if temp.is_password_correct(form.password.data):
                # redirect to /profile
                return "Success"
            # else
            else:
                # add error massage to form.password.errors
                return "Failed"

    return render_template('login.html', form=form)


@auth_blueprint.route('/signup', methods=['GET', 'POST'])
def signup():
    """ Sign up user """
    form = SignupForm()
    if form.validate_on_submit():
        new_user = User(first_name=form.first_name.data, last_name=form.last_name.data, 
                email=form.email.data, password=form.password.data)
        try:
            new_user.save()
            login_user(new_user)
            return new_user.tojson()
        except IntegrityError as e:
            form.email.errors.append('This email is taken')

    # Render template iff `GET` or validation did not pass
    return render_template('signup.html', form=form)


@auth_blueprint.route('/users', methods=['POST'])
def add_user():
    post_data = request.get_json()
    if not post_data:
        response_object = {
            'status': 'fail',
            'message': 'Invalid payload.'
        }
        return jsonify(response_object), 400
    username = post_data.get('username')
    email = post_data.get('email')
    try:
        user = User.query.filter_by(email=email).first()
        if not user:
            db.session.add(User(username=username, email=email))
            db.session.commit()
            response_object = {
                'status': 'success',
                'message': f'{email} was added!'
            }
            return jsonify(response_object), 201
        else:
            response_object = {
                'status': 'fail',
                'message': 'Sorry. That email already exists.'
            }
            return jsonify(response_object), 400
    except exc.IntegrityError as e:
        db.session.rollback()
        response_object = {
            'status': 'fail',
            'message': 'Invalid payload.'
        }
        return jsonify(response_object), 400


@auth_blueprint.route('/users', methods=['GET'])
def get_all_users():
    """Get all users"""
    users = User.query.all()
    users_list = []
    for user in users:
        user_object = {
            'id': user.id,
            'username': user.username,
            'email': user.email,
            'created_at': user.created_at
        }
        users_list.append(user_object)
    response_object = {
        'status': 'success',
        'data': {
            'users': users_list
        }
    }
    return jsonify(response_object), 200


@auth_blueprint.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect('/login')


@auth_blueprint.route('/', methods=['GET'])
def landing():
    return render_template('landing.html')
