from flask import Flask, render_template, request, redirect, url_for, flash
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
import secrets
import pickle

app = Flask(__name__)
app.secret_key = secrets.token_hex(16)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'  # Перенаправлення на сторінку логіну

# Замість бази даних ми використовуватимемо словник для зручності демонстрації
users = {'user1': {'password': 'pass1'}, 'user2': {'password': 'pass2'}}
notes_data = {}

class User(UserMixin):
    def __init__(self, user_id):
        self.id = user_id

    def get_id(self):
        return self.id

@login_manager.user_loader
def load_user(user_id):
    if user_id in users:
        return User(user_id)
    return None

@app.errorhandler(401)  # Обробник помилки "Unauthorized"
def unauthorized(error):
    flash('Для перегляду цієї сторінки потрібно увійти в систему', 'error')
    return redirect(url_for('login'))

@app.route('/')
@login_required
def index():
    user_notes = notes_data.get(current_user.id, [])
    return render_template('index.html', notes=user_notes)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = users.get(username)
        if user and user['password'] == password:
            login_user(User(username))
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
        if username not in users:
            users[username] = {'password': password}
            notes_data[username] = []
            flash('Ви успішно зареєструвалися', 'success')
            return redirect(url_for('login'))
        else:
            flash('Користувач з таким іменем вже існує', 'error')
    return render_template('register.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Ви вийшли з акаунту', 'success')
    return redirect(url_for('login'))

@app.route('/add', methods=['POST'])
@login_required
def add_note():
    note = request.form['note'].strip()
    if note:
        if len(note) <= 200:
            user_notes = notes_data.get(current_user.id, [])
            user_notes.append(note)
            notes_data[current_user.id] = user_notes
            flash('Нотатка додана', 'success')
        else:
            flash('Нотатка не може перевищувати 200 символів', 'error')
    else:
        flash('Потрібно ввести текст нотатки', 'error')
    return redirect(url_for('index'))

@app.route('/edit/<int:index>', methods=['GET', 'POST'])
@login_required
def edit_note(index):
    user_notes = notes_data.get(current_user.id, [])
    if 0 <= index < len(user_notes):
        if request.method == 'POST':
            new_note = request.form['note']
            user_notes[index] = new_note
            notes_data[current_user.id] = user_notes
            flash('Нотатка відредагована', 'success')
            return redirect(url_for('index'))
        return render_template('edit.html', note=user_notes[index], index=index)
    flash('Нотатка не знайдена', 'error')
    return redirect(url_for('index'))

@app.route('/delete/<int:index>')
@login_required
def delete_note(index):
    user_notes = notes_data.get(current_user.id, [])
    if 0 <= index < len(user_notes):
        user_notes.pop(index)
        notes_data[current_user.id] = user_notes
        flash('Нотатка видалена', 'success')
    else:
        flash('Нотатка не знайдена', 'error')
    return redirect(url_for('index'))

@app.route('/clear')
@login_required
def clear_notes():
    notes_data[current_user.id] = []
    flash('Нотатки очищені', 'success')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
