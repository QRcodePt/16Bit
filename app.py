from flask import Flask, jsonify
import sqlite3

app = Flask(__name__)

# Функция для подключения к базе данных
def get_db_connection():
    conn = sqlite3.connect('DB_workhour.db')
    conn.row_factory = sqlite3.Row
    return conn

# Маршрут для получения данных из таблицы Employees
@app.route('/employees', methods=['GET'])
def get_employees():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Employees')
    employees = cursor.fetchall()
    conn.close()
    return jsonify({'employees': [dict(emp) for emp in employees]})

# Маршрут для получения данных из таблицы QRCode
@app.route('/qrcodes', methods=['GET'])
def get_qrcodes():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM QRCode')
    qrcodes = cursor.fetchall()
    conn.close()
    return jsonify({'qrcodes': [dict(qr) for qr in qrcodes]})

# Маршрут для получения данных из таблицы WorkHours
@app.route('/workhours', methods=['GET'])
def get_workhours():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM WorkHours')
    workhours = cursor.fetchall()
    conn.close()
    return jsonify({'workhours': [dict(wh) for wh in workhours]})


@app.route('/')
def index():
    conn = get_db_connection()

    # Получаем данные из таблицы Employees
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Employees')
    employees = cursor.fetchall()

    # Получаем данные из таблицы QRCode
    cursor.execute('SELECT * FROM QRCode')
    qrcodes = cursor.fetchall()

    # Получаем данные из таблицы WorkHours
    cursor.execute('SELECT * FROM WorkHours')
    workhours = cursor.fetchall()

    conn.close()

    # Формируем HTML-страницу с данными из всех таблиц
    html_content = """
        <html>
        <head>
            <title>Информация из БД</title>
        </head>
        <body>
            <h1>Employees</h1>
            <table border="1">
                <tr>
                    <th>employee_id</th>
                    <th>username</th>
                    <th>full_name</th>
                </tr>
                {% for emp in employees %}
                <tr>
                    <td>{{ emp['employee_id'] }}</td>
                    <td>{{ emp['username'] }}</td>
                    <td>{{ emp['full_name'] }}</td>
                </tr>
                {% endfor %}
            </table>

            <h1>QR Codes</h1>
            <table border="1">
                <tr>
                    <th>ID</th>
                    <th>QR Code</th>
                </tr>
                {% for qr in qrcodes %}
                <tr>
                    <td>{{ qr['id'] }}</td>
                    <td>{{ qr['qrcode'] }}</td>
                </tr>
                {% endfor %}
            </table>

            <h1>Work Hours</h1>
            <table border="1">
                <tr>
                    <th>ID</th>
                    <th>Date</th>
                    <th>Hours</th>
                </tr>
                {% for wh in workhours %}
                <tr>
                    <td>{{ wh['id'] }}</td>
                    <td>{{ wh['date'] }}</td>
                    <td>{{ wh['hours'] }}</td>
                </tr>
                {% endfor %}
            </table>
        </body>
        </html>
        """

    return html_content

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
