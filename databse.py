import mysql.connector

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
def create_jobs():
    cursor = get_db().cursor()

def read_jobs():
    conn = get_db()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM jobs")
    jobs = cursor.fetchall()
    cursor.close()
    conn.close()
    return jobs

def update_jobs():
    cursor = get_db().cursor()

def delete_jobs():
    cursor = get_db().cursor()

#CRUD TABLE FOR applications
def create_applicants():
    cursor = get_db().cursor()

def read_applicants():
    conn = get_db()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM applicanats")
    applicants = cursor.fetchall()
    cursor.close()
    conn.close()
    return applicants

def update_applications():
    cursor = get_db().cursor()

def delete_applicants():
    cursor = get_db().cursor()

#CRUD JOB FOR contacts
def create_contacts():
    cursor = get_db().cursor()

def read_contacts():
    cursor = get_db().cursor()

def update_contacts():
    conn = get_db()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM contacts")
    contacts = cursor.fetchall()
    cursor.close()
    conn.close()
    return contacts

def delete_contacts():
    cursor = get_db().cursor()







