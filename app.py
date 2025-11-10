from flask import Flask, render_template, request, redirect, url_for, jsonify
import sqlite3
from datetime import datetime
import os

app = Flask(__name__)
DATABASE = 'schedule.db'

def get_db_connection():
    """Create database connection"""
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    """Initialize database with tables"""
    conn = get_db_connection()
    conn.execute('''
        CREATE TABLE IF NOT EXISTS events (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT,
            date TEXT NOT NULL,
            time TEXT NOT NULL,
            location TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')

    # Add sample data if table is empty
    count = conn.execute('SELECT COUNT(*) FROM events').fetchone()[0]
    if count == 0:
        sample_events = [
            ('Team Meeting', 'Weekly team sync', '2025-11-10', '10:00', 'Conference Room A'),
            ('Project Deadline', 'Submit final report', '2025-11-15', '17:00', 'Online'),
            ('Training Session', 'Python Web Development', '2025-11-12', '14:00', 'Training Center'),
        ]
        conn.executemany(
            'INSERT INTO events (title, description, date, time, location) VALUES (?, ?, ?, ?, ?)',
            sample_events
        )

    conn.commit()
    conn.close()

@app.route('/')
def index():
    """Home page with schedule list"""
    conn = get_db_connection()
    events = conn.execute('SELECT * FROM events ORDER BY date, time').fetchall()
    conn.close()
    return render_template('index.html', events=events)

@app.route('/add', methods=['GET', 'POST'])
def add_event():
    """Add new event"""
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        date = request.form['date']
        time = request.form['time']
        location = request.form['location']

        conn = get_db_connection()
        conn.execute(
            'INSERT INTO events (title, description, date, time, location) VALUES (?, ?, ?, ?, ?)',
            (title, description, date, time, location)
        )
        conn.commit()
        conn.close()

        return redirect(url_for('index'))

    return render_template('add_event.html')

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_event(id):
    """Edit existing event"""
    conn = get_db_connection()

    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        date = request.form['date']
        time = request.form['time']
        location = request.form['location']

        conn.execute(
            'UPDATE events SET title=?, description=?, date=?, time=?, location=? WHERE id=?',
            (title, description, date, time, location, id)
        )
        conn.commit()
        conn.close()

        return redirect(url_for('index'))

    event = conn.execute('SELECT * FROM events WHERE id = ?', (id,)).fetchone()
    conn.close()

    if event is None:
        return redirect(url_for('index'))

    return render_template('edit_event.html', event=event)

@app.route('/delete/<int:id>', methods=['POST'])
def delete_event(id):
    """Delete event"""
    conn = get_db_connection()
    conn.execute('DELETE FROM events WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

@app.route('/api/events')
def api_events():
    """API endpoint to get all events as JSON"""
    conn = get_db_connection()
    events = conn.execute('SELECT * FROM events ORDER BY date, time').fetchall()
    conn.close()

    events_list = []
    for event in events:
        events_list.append({
            'id': event['id'],
            'title': event['title'],
            'description': event['description'],
            'date': event['date'],
            'time': event['time'],
            'location': event['location']
        })

    return jsonify(events_list)

if __name__ == '__main__':
    # Initialize database on first run
    if not os.path.exists(DATABASE):
        init_db()

    # Run the application
    app.run(debug=True, host='0.0.0.0', port=5000)
