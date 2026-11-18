from flask import Flask, render_template, request, redirect
import mysql.connector
import database
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
    companies = database.read_companies()
    return render_template('companies.html', companies=companies)

@app.route('/companies/create', methods=['POST'])
def create_company():
    company_name = request.form['company_name']
    industry = request.form['industry'] or None
    website = request.form['website'] or None
    city = request.form['city'] or None
    state = request.form['state'] or None
    notes = request.form['notes']or None
    database.create_companies(company_name, industry, website, city, state, notes)
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
    database.update_companies(company_id, company_name, industry, website, city, state, notes)
    return redirect('/companies')

@app.route('/companies/delete', methods=['POST'])
def delete_company():
    company_id = request.form['company_id']
    database.delete_companies(company_id)
    return redirect('/companies')

#FLASK ROUTES FOR COMPANIES AND ITS CRUD FUNCTIONS
@app.route('/jobs')
def jobs():
    jobs = database.read_jobs()
    companies = database.read_companies()
    return render_template('jobs.html', jobs=jobs, companies=companies)

@app.route('/jobs/create', methods=['POST'])
def create_jobs():
    company_id = request.form['company_id']
    job_title = request.form['job_title']
    job_type = request.form['job_type']
    salary_min = request.form['salary_min']
    salary_max = request.form['salary_max']
    job_url = request.form['job_url'] or None
    date_posted = request.form['date_posted']
    requirements = request.form['requirements'] or None
    database.create_jobs(company_id, job_title, job_type, salary_min, salary_max, job_url, date_posted, requirements)
    return redirect('/jobs')

@app.route('/jobs/update', methods=['POST'])
def update_jobs():
    job_id = request.form['job_id']
    company_id = request.form['company_id']
    job_title = request.form['job_title']
    job_type = request.form['job_type']
    salary_min = request.form['salary_min']
    salary_max = request.form['salary_max']
    job_url = request.form['job_url'] or None
    date_posted = request.form['date_posted']
    requirements = request.form['requirements'] or None
    database.update_jobs(job_id, company_id, job_title, job_type, salary_min, salary_max, job_url, date_posted, requirements)
    return redirect('/jobs')

@app.route('/jobs/delete', methods=['POST'])
def delete_job():
    job_id = request.form['job_id']
    database.delete_jobs(job_id)
    return redirect('/jobs')

#FLASK ROUTES FOR applications AND ITS CRUD FUNCTIONS
@app.route('/applications')
def applications():
    applications = database.read_applications()
    jobs = database.read_jobs()
    companies = database.read_companies()
    return render_template('applications.html', applications=applications, jobs=jobs, comapnies=companies)

@app.route('/application/create', methods=['POST'])
def create_applications():
    job_id = request.form['job_id']
    application_date = request.form['application_date']
    status = request.form['status']
    resume_version = request.form['resume_version']
    cover_letter_sent = request.form['cover_letter_sent'] or None
    interview_data = request.form['interview_data'] or None
    database.create_applications(job_id, application_date, status, resume_version, cover_letter_sent, interview_data)
    return redirect('/applications')

@app.route('/application/update', methods=['POST'])
def update_applications():
    application_id = request.form['application_id']
    job_id = request.form['job_id']
    application_date = request.form['application_date']
    status = request.form['status']
    resume_version = request.form['resume_version']
    cover_letter_sent = request.form['cover_letter_sent']
    interview_data = request.form['interview_data'] or None
    database.update_applications(application_id, job_id, application_date, status, resume_version, cover_letter_sent, interview_data)
    return redirect('/applications')

@app.route('/application/delete', methods=['POST'])
def delete_application():
    application_id = request.form['application_id']
    database.delete_applications(application_id)
    return redirect('/applications')


if __name__ == '__main__':
    app.run(debug=True)
