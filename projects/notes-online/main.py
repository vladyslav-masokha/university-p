from flask import Flask, render_template, request, redirect, url_for, flash, session
import secrets

app = Flask(__name__)
app.secret_key = secrets.token_hex(16)

def get_notes_key():
    return f"notes_{session['user_id']}" if 'user_id' in session else None

def load_notes():
    notes_key = get_notes_key()
    if notes_key:
        return session.get(notes_key, [])
    return []

def save_notes(notes):
    notes_key = get_notes_key()
    if notes_key:
        session[notes_key] = notes

@app.before_request
def initialize():
    if 'user_id' not in session:
        session['user_id'] = secrets.token_hex(8)

@app.route('/')
def index():
    notes = load_notes()
    return render_template('index.html', notes=notes)

@app.route('/add', methods=['POST'])
def add_note():
    note = request.form['note'].strip()
    if note:
        if len(note) <= 200:
            notes = load_notes()
            notes.append(note)
            save_notes(notes)
        else:
            flash('Нотатка не може перевищувати 200 символів', 'error')
    else:
        flash('Потрібно ввести текст нотатки', 'error')
    return redirect(url_for('index'))

@app.route('/edit/<int:index>', methods=['GET', 'POST'])
def edit_note(index):
    notes = load_notes()
    if request.method == 'POST':
        new_note = request.form['note']
        notes[index] = new_note
        save_notes(notes)
        return redirect(url_for('index'))
    return render_template('edit.html', note=notes[index], index=index)

@app.route('/delete/<int:index>')
def delete_note(index):
    notes = load_notes()
    if 0 <= index < len(notes):
        notes.pop(index)
        save_notes(notes)
    return redirect(url_for('index'))

@app.route('/clear')
def clear_notes():
    notes_key = get_notes_key()
    if notes_key:
        session.pop(notes_key, None)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
