from flask import Flask, render_template, request, redirect, url_for, flash
import secrets
import pickle

app = Flask(__name__)
app.secret_key = secrets.token_hex(16)

notes = []
NOTES_FILE = 'notes.data'

def load_notes():
    try:
        with open(NOTES_FILE, 'rb') as file:
            notes = pickle.load(file)
    except FileNotFoundError:
        notes = []
    return notes

def save_notes(notes):
    with open(NOTES_FILE, 'wb') as file:
        pickle.dump(notes, file)

notes = load_notes()

@app.before_request
def initialize():
    load_notes()

@app.teardown_appcontext
def shutdown(exception=None):
    save_notes(notes)

@app.route('/')
def index():
    return render_template('index.html', notes=notes)

@app.route('/add', methods=['POST'])
def add_note():
    note = request.form['note'].strip()
    if note:
        if len(note) <= 200:
            notes.append(note)
        else:
            flash('Нотатка не може перевищувати 200 символів', 'error')
    else:
        flash('Потрібно ввести текст нотатки', 'error')
    return redirect(url_for('index'))
  
@app.route('/edit/<int:index>', methods=['GET', 'POST'])
def edit_note(index):
    if request.method == 'POST':
        new_note = request.form['note']
        notes[index] = new_note
        return redirect(url_for('index'))
    return render_template('edit.html', note=notes[index], index=index)

@app.route('/delete/<int:index>')
def delete_note(index):
    notes.pop(index)
    return redirect(url_for('index'))

@app.route('/clear')
def clear_notes():
    global notes
    notes = []
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)