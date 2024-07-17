# app/routes.py

from flask import render_template, request, redirect, url_for
from . import db
from .models import User

def register_routes(app):
    @app.route('/')
    def index():
        users = User.query.all()
        return render_template('index.html', users=users)

    @app.route('/create', methods=['GET', 'POST'])
    def create():
        if request.method == 'POST':
            name = request.form['name']
            email = request.form['email']
            new_user = User(name=name, email=email)
            db.session.add(new_user)
            db.session.commit()
            return redirect(url_for('index'))
        return render_template('create.html')

    @app.route('/update/<int:user_id>', methods=['GET', 'POST'])
    def update(user_id):
        user = User.query.get_or_404(user_id)
        if request.method == 'POST':
            user.name = request.form['name']
            user.email = request.form['email']
            db.session.commit()
            return redirect(url_for('index'))
        return render_template('update.html', user=user)

    @app.route('/delete/<int:user_id>', methods=['POST'])
    def delete():
        user_id = request.form['user_id']
        user = User.query.get_or_404(user_id)  # Might raise exception if user not found

        try:
            db.session.delete(user)
            db.session.commit()
            # Redirect or success message
        except:
            # Handle exception like user not found or database error
            return "An error occurred during deletion. Please try again."

        return render_template('delete.html', user=user)

