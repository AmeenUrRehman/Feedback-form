from flask import Blueprint, render_template, request, flash
from flask_login import login_required, current_user
from .models import Note
from . import db

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST':
        # Gets the note from the HTML
        note = request.form.get('note')
        new_note = Note(data=note, user_id=current_user.id)
        db.session.add(new_note)
        db.session.commit()
        return render_template('home.html', user=current_user)

    return render_template("login.html", user=current_user)
