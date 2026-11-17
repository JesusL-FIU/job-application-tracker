from flask import Flask, render_template, request, redirect
import mysql.connector
import databse
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

    cursor.execute('SELECT status, COUNT(*) AS count From applications GROUP BY status')
    status = cursor.fetchall()

    conn.close()
    return render_template('dashboard.html', stats=stats, companies=companies, jobs=jobs, status=status)

#FLASK ROUTES FOR COMPANIES AND ITS CRUD FUNCTIONS
@app.route('/companies')
def companies():
    companies = databse.read_companies()
    return render_template('companies.html', companies=companies)

@app.route('/companies/create', methods=['POST'])
def create_company():
    company_name = request.form['company_name']
    industry = request.form['industry']
    website = request.form['website']
    city = request.form['city']
    state = request.form['state']
    notes = request.form['notes']
    databse.create_companies(company_name, industry, website, city, state, notes)
    return redirect('/companies')

@app.route('/companies/update', methods=['POST'])
def update_company():
    company_id = request.form['company_id']
    company_name = request.form['company_name']
    industry = request.form['industry']
    website = request.form['website']
    city = request.form['city']
    state = request.form['state']
    notes = request.form['notes']
    databse.update_companies(company_id, company_name, industry, website, city, state, notes)
    return redirect('/companies')

@app.route('/companies/delete', methods=['POST'])
def delete_company():
    company_id = request.form['company_id']
    databse.delete_companies(company_id)
    return redirect('/companies')

if __name__ == '__main__':
    app.run(debug=True)
