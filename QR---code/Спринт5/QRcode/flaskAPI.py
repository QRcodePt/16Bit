import os
from flask import Flask, g
import sqlite3

app = Flask(__name__)

DATABASE = os.path.join(app.root_path, 'work_time_tracking.db')

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


@app.route('/')
def index():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Сотрудники')
    data1 = cursor.fetchall()
    cursor.execute('SELECT * FROM time_entries')
    data2 = cursor.fetchall()
    conn.close()

    html = "<h2>Data from Сотрудники:</h2>"
    html += "<table border='1'>"
    html += "<tr>"
    if data1:  # Проверяем, есть ли данные
        for col in cursor.description:
            html += f"<th>{col[0]}</th>"
        html += "</tr>"
        for row in data1:
            html += "<tr>"
            for val in row:
                html += f"<td>{val}</td>"
            html += "</tr>"
    html += "</table>"

    html += "<h2>Data from time_entries:</h2>"
    html += "<table border='1'>"
    html += "<tr>"
    if data2:  # Проверяем, есть ли данные
        for col in cursor.description:
            html += f"<th>{col[0]}</th>"
        html += "</tr>"
        for row in data2:
            html += "<tr>"
            for val in row:
                html += f"<td>{val}</td>"
            html += "</tr>"
    html += "</table>"

    return html

if __name__ == '__main__':
    app.run(host='0.0.0.0')
