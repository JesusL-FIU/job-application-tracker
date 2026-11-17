from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)

def get_db():
    return mysql.connector.connect(
        host='localhost', user='root',
        password='root', database='job_tracker'
    )

@app.route('/')
def dashboard():
    conn = get_db()
    cursor = conn.cursor(dictionary=True)
    cursor.execute('SELECT COUNT(*) as count FROM applications')
    stats = cursor.fetchone()

    cursor.execute('SELECT COUNT(*) as count FROM companies')
    companies = cursor.fetchone()

    cursor.execute('SELECT COUNT(*) as count FROM jobs')
    jobs = cursor.fetchone()

    cursor.execute('SELECT COUNT(*) as count FROM jobs')
    jobs = cursor.fetchone()

    cursor.execute('SELECT status, COUNT(*) AS count From applications GROUP BY status')
    status = cursor.fetchall()

    conn.close()
    return render_template('dashboard.html', stats=stats, companies=companies, jobs=jobs, status=status)

if __name__ == '__main__':
    app.run(debug=True)
