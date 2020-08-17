#!/usr/bin/env python3

import datetime


def read(db):
    for row in db.dbconnect.execute('SELECT * FROM company;'):
        print(row)
    return


# Company menu option 1
def add(db, updated_on, name, address1, address2, city, state, postal_code,
        country):
    db.dbconnect.execute('INSERT INTO company \
            (updated_on,name,address1,address2,city,state,postal_code,country) \
            VALUES(?,?,?,?,?,?,?,?);',
                         (updated_on, name, address1, address2, city, state,
                          postal_code, country))
    db.dbconnect.commit()


# Company menu option 2
def modify(db, modify_company, name, address1, address2, city, state, postal_code, country):
    updated_on = datetime.datetime.now().isoformat()
    db.dbconnect.execute('UPDATE company SET \
    updated_on=?,name=?,address1=?,address2=?,city=?,state=?,postal_code=?,country=? WHERE \
    rowid=?;', (updated_on, name, address1, address2, city, state, postal_code, country, modify_company))
    db.dbconnect.commit()


# Company menu option 2 aux
def get_one(db, modify_company):
    cur = db.cursor()
    cur.execute('SELECT * FROM company WHERE rowid=?', (modify_company,))
    old_company = cur.fetchone()
    return old_company


# Company menu option 3
def delete(db, delete_company):
    db.dbconnect.execute('DELETE FROM company WHERE rowid=?;', delete_company)
    db.dbconnect.commit()


# Company menu option 4
def last_entries(db, how_many):
    for row in db.dbconnect.execute('SELECT * FROM company ORDER BY rowid DESC LIMIT ?;', how_many):
        print(row)


# Company menu option 5
def search(db, search_company):
    for row in db.dbconnect.execute("SELECT * FROM company WHERE name LIKE ?;", ('%' + search_company + '%',)):
        print(row)
