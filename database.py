import mysql.connector
import json

#ESTABLISH CONNECTION TO DATABASE
def get_db():
    return mysql.connector.connect(
        host='localhost', user='root',
        password='root', database='job_tracker'
    )

#CRUD TABLE FOR Companies
def create_companies(company_name, industry, website, city, state, notes):
    conn = get_db()
    cursor = conn.cursor()
    sql = "INSERT INTO companies (company_name, industry, website, city, state, notes) VALUES (%s, %s, %s, %s, %s, %s)"
    cursor.execute(sql, (company_name, industry, website, city, state, notes))
    conn.commit()
    cursor.close()
    conn.close()

def read_companies():
    conn = get_db()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM companies")
    companies = cursor.fetchall()
    cursor.close()
    conn.close()
    return companies

def update_companies(company_id, company_name, industry, website, city, state, notes):
    conn = get_db()
    cursor = conn.cursor()
    sql = "UPDATE companies SET company_name=%s, industry=%s, website=%s, city=%s, state=%s, notes=%s WHERE company_id=%s"
    cursor.execute(sql, (company_name, industry, website, city, state, notes, company_id))
    conn.commit()
    cursor.close()
    conn.close()

def delete_companies(company_id):
    conn = get_db()
    cursor = conn.cursor()
    sql = "DELETE FROM companies WHERE company_id=%s"
    cursor.execute(sql, (company_id,))
    conn.commit()
    cursor.close()
    conn.close()

#CRUD TABLE FOR job
def create_jobs(company_id, job_title, job_type, salary_min, salary_max, job_url, date_posted, requirements):
    conn = get_db()
    cursor = conn.cursor()
    sql = "INSERT INTO jobs (company_id, job_title, job_type, salary_min, salary_max, job_url, date_posted, requirements) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
    cursor.execute(sql, (company_id, job_title, job_type, salary_min, salary_max, job_url, date_posted, requirements))
    conn.commit()
    cursor.close()
    conn.close()

def read_jobs():
    conn = get_db()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT jobs.*, companies.company_name FROM jobs INNER JOIN companies ON jobs.company_id = companies.company_id")
    jobs = cursor.fetchall()
    cursor.close()
    conn.close()
    return jobs

def update_jobs(job_id, company_id, job_title, job_type, salary_min, salary_max, job_url, date_posted, requirements):
    conn = get_db()
    cursor = conn.cursor()
    sql = "UPDATE jobs SET company_id=%s, job_title=%s, job_type=%s, salary_min=%s, salary_max=%s, job_url=%s, date_posted=%s, requirements=%s WHERE job_id=%s"
    cursor.execute(sql, (company_id, job_title, job_type, salary_min,salary_max, job_url, date_posted, requirements, job_id))
    conn.commit()
    cursor.close()
    conn.close()

def delete_jobs(job_id):
    conn = get_db()
    cursor = conn.cursor()
    sql = "DELETE FROM jobs WHERE job_id=%s"
    cursor.execute(sql, (job_id,))
    conn.commit()
    cursor.close()
    conn.close()

#CRUD TABLE FOR applications
def create_applications(job_id, application_date, status, resume_version, cover_letter_sent, interview_data ):
    conn = get_db()
    cursor = conn.cursor()
    sql = "INSERT INTO applications (job_id, application_date, status, resume_version, cover_letter_sent, interview_data) VALUES (%s, %s, %s, %s, %s, %s)"
    cursor.execute(sql, (job_id, application_date, status, resume_version, cover_letter_sent, interview_data))
    conn.commit()
    cursor.close()
    conn.close()

def read_applications():
    conn = get_db()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT applications.*, jobs.job_title, companies.company_name FROM applications INNER JOIN jobs ON applications.job_id = jobs.job_id INNER JOIN companies ON jobs.company_id = companies.company_id")
    applications = cursor.fetchall()
    cursor.close()
    conn.close()
    return applications

def update_applications(application_id, job_id, application_date, status, resume_version, cover_letter_sent, interview_data):
    conn = get_db()
    cursor = conn.cursor()
    sql = "UPDATE applications SET job_id=%s, application_date=%s, status=%s, resume_version=%s, cover_letter_sent=%s, interview_data=%s WHERE application_id=%s"
    cursor.execute(sql, (job_id, application_date, status, resume_version, cover_letter_sent,interview_data, application_id))
    conn.commit()
    cursor.close()
    conn.close()

def delete_applications(application_id):
    conn = get_db()
    cursor = conn.cursor()
    sql = "DELETE FROM applications WHERE application_id=%s"
    cursor.execute(sql, (application_id,))
    conn.commit()
    cursor.close()
    conn.close()

#CRUD JOB FOR contacts
def create_contacts(company_id, contact_name, title, email, phone, linkedin_url, notes):
    conn = get_db()
    cursor = conn.cursor()
    sql = "INSERT INTO contacts (company_id, contact_name, title, email, phone, linkedin_url, notes) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    cursor.execute(sql, (company_id, contact_name, title, email, phone, linkedin_url, notes))
    conn.commit()
    cursor.close()
    conn.close()

def read_contacts():
    conn = get_db()
    cursor = conn.cursor(dictionary=True)
    sql = "SELECT contacts.*, companies.company_name FROM contacts JOIN companies ON contacts.company_id = companies.company_id"
    cursor.execute(sql)
    contacts = cursor.fetchall()
    cursor.close()
    conn.close()
    return contacts

def update_contacts(contact_id, company_id, contact_name, title, email, phone, linkedin_url, notes):
    conn = get_db()
    cursor = conn.cursor()
    sql = "UPDATE contacts SET company_id=%s, contact_name=%s, title=%s, email=%s, phone=%s, linkedin_url=%s, notes=%s WHERE contact_id=%s"
    cursor.execute(sql, (company_id, contact_name, title, email, phone, linkedin_url, notes, contact_id))
    conn.commit()
    cursor.close()
    conn.close()

def delete_contacts(contact_id):
    conn = get_db()
    cursor = conn.cursor()
    sql = "DELETE FROM contacts WHERE contact_id=%s"
    cursor.execute(sql, (contact_id,))
    conn.commit()
    cursor.close()
    conn.close()

#compare skills to requirements
def job_match(user_skills):
    conn = get_db()
    cursor = conn.cursor(dictionary=True)
    user_skills = [skill.strip().lower() for skill in user_skills.split(',') if skill.strip()]
    sql= ("SELECT jobs.*, companies.company_name FROM jobs JOIN companies ON jobs.company_id = companies.company_id WHERE jobs.requirements IS NOT NULL")
    cursor.execute(sql)
    jobs = cursor.fetchall()

    #AI HELP and wrote the job matching logic and comparing it with entered skills
    matching_jobs = []

    for job in jobs:

        requirements = job['requirements']

        # Convert JSON string into a Python dictionary if necessary
        if isinstance(requirements, str):
            requirements = json.loads(requirements)

        # Get required skills from the JSON
        required_skills = requirements.get('required_skills', [])

        # Find matched skills
        matched_skills = [
            skill for skill in required_skills
            if skill.lower() in user_skills
        ]

        # Find missing skills
        missing_skills = [
            skill for skill in required_skills
            if skill.lower() not in user_skills
        ]

        # Calculate match percentage
        if required_skills:
            percentage = round(
                len(matched_skills) / len(required_skills) * 100
            )
        else:
            percentage = 0

        job['matched_skills'] = matched_skills
        job['missing_skills'] = missing_skills
        job['match_percentage'] = percentage
        job['total_skills'] = len(required_skills)

        matching_jobs.append(job)

    # Sort from highest match to lowest
    matching_jobs.sort(
        key=lambda job: job['match_percentage'],
        reverse=True
    )

    cursor.close()
    conn.close()
    return matching_jobs






