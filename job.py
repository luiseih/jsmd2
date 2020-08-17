#!/usr/bin/env python3


# Job menu header
def read(db):
    for row in db.dbconnect.execute('SELECT * FROM company;'):
        print(row)


# Job menu option 1
def add(db, updated_on, from_company, name, requirements):
    db.dbconnect.execute('INSERT INTO job \
            (updated_on,from_company,name,requirements) \
            VALUES(?,?,?,?);',
                         (updated_on, from_company, name, requirements))
    db.dbconnect.commit()


# Job menu option 2
def modify(db, updated_on, from_company, name, requirements, modify_job):
    db.dbconnect.execute('UPDATE company SET \
    updated_on=?,from_company=?,name=?,requirements=? WHERE \
    rowid=?;', (updated_on, from_company, name, requirements, modify_job))
    db.dbconnect.commit()


# Job menu option 2 aux
def get_one(db, modify_job):
    cur = db.cursor()
    cur.execute('SELECT * FROM job WHERE rowid=?', (modify_job,))
    old_company = cur.fetchone()
    return old_company


# Job menu option 3
def delete(db, delete_job):
    db.dbconnect.execute('DELETE FROM job WHERE rowid=?;', delete_job)
    db.dbconnect.commit()


# Job menu option 4
def last_entries(db, how_many):
    for row in db.dbconnect.execute('SELECT * FROM job ORDER BY rowid \
                                     DESC LIMIT ?;', how_many):
        print(row)


# Job menu option 5
def search(db, search_job):
    for row in db.dbconnect.execute("SELECT * FROM company WHERE name LIKE ?;", ('%' + search_job + '%',)):
        print(row)
    input("Press ENTER to continue...")
