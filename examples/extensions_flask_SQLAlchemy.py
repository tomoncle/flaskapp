#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time           : 18-3-28 下午5:27
# @Author         : Tom.Lee
# @File           : extensions_flask_SQLAlchemy.py
# @Product        : PyCharm

"""
flask 支持 sqlAlchemy
sudo pip install Flask-SQLAlchemy
"""

from datetime import datetime

from flask import Flask
from flask import request, flash, url_for, redirect, render_template
from flask_sqlalchemy import SQLAlchemy

import config

app = Flask(__name__, static_folder=config.STATIC_FOLDER, template_folder=config.TEMPLATE_FOLDER)

# 'sqlite:////tmp/db_flask'
app.config['SQLALCHEMY_DATABASE_URI'] = config.SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_ECHO'] = False
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.secret_key = '1!@#$%^&*()'
db = SQLAlchemy(app)


class Todo(db.Model):
    __tablename__ = 't_todo'
    id = db.Column('todo_id', db.Integer, primary_key=True)
    title = db.Column(db.String(60))
    text = db.Column(db.String)
    done = db.Column(db.Boolean)
    pub_date = db.Column(db.DateTime)

    def __init__(self, title, text):
        self.title = title
        self.text = text
        self.done = False
        self.pub_date = datetime.utcnow()


@app.route('/')
def lists():
    data = Todo.query.order_by(Todo.pub_date.desc()).all()
    return render_template('examples/extensions_flask_sqlAlchemy.html', todos=data)


@app.route('/', methods=['POST'])
def create():
    if not request.form['title']:
        flash('Title is required', 'error')
    elif not request.form['text']:
        flash('Text is required', 'error')
    else:
        todo = Todo(request.form['title'], request.form['text'])
        db.session.add(todo)
        db.session.commit()
        flash(u'Todo item was successfully created')
    return redirect(url_for('lists'))


@app.route('/update', methods=['POST'])
def update():
    for todo in Todo.query.all():
        todo.done = ('done.%d' % todo.id) in request.form
    flash('Updated status')
    db.session.commit()
    return redirect(url_for('lists'))


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
