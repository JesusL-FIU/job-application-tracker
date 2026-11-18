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

    cursor.execute('SELECT COUNT(*) as count FROM contacts')
    contacts = cursor.fetchone()

    cursor.execute('SELECT status, COUNT(*) AS count From applications GROUP BY status')
    status = cursor.fetchall()

    conn.close()
    return render_template('dashboard.html', stats=stats, companies=companies, jobs=jobs, contacts=contacts, status=status)

#FLASK ROUTES FOR COMPANIES AND ITS CRUD FUNCTIONS
@app.route('/companies')
def companies():
    companies = database.read_companies()
    edit_company = None
    company_id = request.args.get('load_id')
    if company_id:
        for company in companies:
            if str(company['company_id']) == company_id:
                edit_company = company
                break
    return render_template('companies.html', companies=companies, edit_company=edit_company
    )

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
    industry = request.form['industry'] or None
    website = request.form['website'] or None
    city = request.form['city'] or None
    state = request.form['state'] or None
    notes = request.form['notes'] or None
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
    edit_job = None
    job_id = request.args.get('load_id')
    if job_id:
        for job in jobs:
            if str(job['job_id']) == job_id:
                edit_job = job
                break
    return render_template('jobs.html', jobs=jobs, companies=companies,edit_job=edit_job)

@app.route('/jobs/create', methods=['POST'])
def create_jobs():
    company_id = request.form['company_id']
    job_title = request.form['job_title']
    job_type = request.form['job_type'] or None
    salary_min = request.form['salary_min'] or None
    salary_max = request.form['salary_max'] or None
    job_url = request.form['job_url'] or None
    date_posted = request.form['date_posted'] or None
    requirements = request.form['requirements'] or None
    database.create_jobs(company_id, job_title, job_type, salary_min, salary_max, job_url, date_posted, requirements)
    return redirect('/jobs')

@app.route('/jobs/update', methods=['POST'])
def update_jobs():
    job_id = request.form['job_id']
    company_id = request.form['company_id']
    job_title = request.form['job_title']
    job_type = request.form['job_type'] or None
    salary_min = request.form['salary_min'] or None
    salary_max = request.form['salary_max'] or None
    job_url = request.form['job_url'] or None
    date_posted = request.form['date_posted'] or None
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
    edit_application = None
    application_id = request.args.get('load_id')
    if application_id:
        for application in applications:
            if str(application['application_id']) == application_id:
                edit_application = application
                break

    return render_template('applications.html', applications=applications, jobs=jobs, companies=companies, edit_application=edit_application)


@app.route('/application/create', methods=['POST'])
def create_applications():
    job_id = request.form['job_id']
    application_date = request.form['application_date']
    status = request.form['status'] or None
    resume_version = request.form['resume_version'] or None
    cover_letter_sent = request.form['cover_letter_sent'] or None
    interview_data = request.form['interview_data'] or None
    database.create_applications(job_id, application_date, status, resume_version, cover_letter_sent, interview_data)
    return redirect('/applications')

@app.route('/application/update', methods=['POST'])
def update_applications():
    application_id = request.form['application_id']
    job_id = request.form['job_id']
    application_date = request.form['application_date']
    status = request.form['status'] or None
    resume_version = request.form['resume_version'] or None
    cover_letter_sent = request.form['cover_letter_sent'] or None
    interview_data = request.form['interview_data'] or None
    database.update_applications(application_id, job_id, application_date, status, resume_version, cover_letter_sent, interview_data)
    return redirect('/applications')

@app.route('/application/delete', methods=['POST'])
def delete_application():
    application_id = request.form['application_id']
    database.delete_applications(application_id)
    return redirect('/applications')

#FLASK ROUTES FOR contacts AND ITS CRUD FUNCTIONS@app.route('/contacts')
@app.route('/contacts')
def contacts():
    contacts = database.read_contacts()
    companies = database.read_companies()
    edit_contact = None
    contact_id = request.args.get('load_id')
    if contact_id:
        for contact in contacts:
            if str(contact['contact_id']) == contact_id:
                edit_contact = contact
                break

    return render_template('contacts.html', contacts=contacts, companies=companies, edit_contact=edit_contact)

@app.route('/contacts/create', methods=['POST'])
def create_contact():
    company_id = request.form['company_id']
    contact_name = request.form['contact_name']
    title = request.form['title'] or None
    email = request.form['email'] or None
    phone = request.form['phone'] or None
    linkedin_url = request.form['linkedin_url'] or None
    notes = request.form['notes'] or None
    database.create_contacts(company_id, contact_name, title, email, phone, linkedin_url, notes)
    return redirect('/contacts')

@app.route('/contacts/update', methods=['POST'])
def update_contact():
    contact_id = request.form['contact_id']
    company_id = request.form['company_id']
    contact_name = request.form['contact_name']
    title = request.form['title'] or None
    email = request.form['email'] or None
    phone = request.form['phone'] or None
    linkedin_url = request.form['linkedin_url'] or None
    notes = request.form['notes'] or None
    database.update_contacts(contact_id, company_id, contact_name, title, email, phone, linkedin_url, notes)
    return redirect('/contacts')

@app.route('/contacts/delete', methods=['POST'])
def delete_contact():
    contact_id = request.form['contact_id']
    database.delete_contacts(contact_id)
    return redirect('/contacts')

@app.route('/job_match')
def job_match():
    return render_template('job_match.html')

@app.route('/jobs_match/search', methods=['POST'])
def jobs_search():
    return redirect('/job_match')

if __name__ == '__main__':
    app.run(debug=True)
