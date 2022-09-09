"""Blogly application."""

from flask import Flask, request, redirect, render_template
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, User

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRE_KEY'] = 'secretkey'

debug = DebugToolbarExtension(app)

connect_db(app)
db.create_all()




@app.route("/")

@app.route("/users")

@app.route("/users/new", methods=['POST', 'GET'])

@app.route("/users/<int:user_id>")

@app.route("/users/<int:user_id>/edit", methods=['POST', 'GET'])

@app.route("/users/<int:user_id>/delete", methods=['POST'])