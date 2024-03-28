import os
import secrets
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY') or secrets.token_hex(16)

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL') or 'sqlite:///notes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    notes = db.relationship('Note', backref='user', lazy='dynamic')

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    content = db.Column(db.String(200), nullable=False)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/')
@login_required
def index():
    user_notes = current_user.notes.all()
    return render_template('index.html', notes=user_notes)

@app.route('/add', methods=['POST'])
@login_required
def add_note():
    note_content = request.form['note'].strip()
    if note_content:
        new_note = Note(content=note_content, user_id=current_user.id)
        db.session.add(new_note)
        db.session.commit()
        flash('Нотатку успішно додано!', 'success')
    else:
        flash('Потрібно ввести текст нотатки', 'error')
    return redirect(url_for('index'))

@app.route('/edit/<int:note_id>', methods=['GET', 'POST'])
@login_required
def edit_note(note_id):
    note = Note.query.get_or_404(note_id)
    if note.user_id != current_user.id:
        flash('Ви не маєте права редагувати цю нотатку', 'error')
        return redirect(url_for('index'))

    if request.method == 'POST':
        content = request.form.get('content')
        if content is not None and content.strip(): 
            note.content = content.strip()
            db.session.commit()
            flash('Нотатку успішно оновлено!', 'success')
            return redirect(url_for('index'))
        else:
            flash('Потрібно ввести текст нотатки', 'error')

    return render_template('edit.html', note=note)

@app.route('/delete/<int:note_id>')
@login_required
def delete_note(note_id):
    note = Note.query.get_or_404(note_id)
    if note.user_id != current_user.id:
        flash('Ви не маєте права видаляти цю нотатку', 'error')
        return redirect(url_for('index'))

    db.session.delete(note)
    db.session.commit()
    flash('Нотатку успішно видалено!', 'success')
    return redirect(url_for('index'))

@app.route('/clear_notes', methods=['POST'])
@login_required
def clear_notes():
    Note.query.filter_by(user_id=current_user.id).delete()
    db.session.commit()
    flash('Всі ваші нотатки були видалені', 'success')
    return redirect(url_for('index'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if user and user.password == password:
            login_user(user)
            flash('Ви увійшли до свого акаунту', 'success')
            return redirect(url_for('index'))
        else:
            flash('Неправильний логін або пароль', 'error')
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        existing_user = User.query.filter_by(username=username).first()
        if existing_user:
            flash('Це ім\'я користувача вже зайняте. Спробуйте інше.', 'error')
            return redirect(url_for('register'))

        new_user = User(username=username, password=password)
        db.session.add(new_user)
        db.session.commit()

        flash('Реєстрація пройшла успішно! Тепер ви можете увійти до свого акаунту.', 'success')
        return redirect(url_for('login'))

    return render_template('register.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Ви вийшли з акаунту', 'success')
    return redirect(url_for('login'))

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        
        if 'DATABASE_URL' not in os.environ:
            app.run(debug=True)