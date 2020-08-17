#!/usr/bin/env python3

import datetime
import database

def read():
    for row in database.dbconnect.execute('SELECT * FROM company;'):
        print(row)
    return


# Company menu option 1
def add(name, address1, address2, city, state, postal_code, country):
    updated_on = datetime.datetime.now().isoformat()
    conn.execute('INSERT INTO company \
            (updated_on,name,address1,address2,city,state,postal_code,country) \
            VALUES(?,?,?,?,?,?,?,?);',
                 (updated_on, name, address1, address2, city, state, postal_code, country))
    conn.commit()
    return


# Company menu option 2
def modify(modify_company, name, address1, address2, city, state, postal_code, country):
    updated_on = datetime.datetime.now().isoformat()
    conn.execute('UPDATE company SET \
    updated_on=?,name=?,address1=?,address2=?,city=?,state=?,postal_code=?,country=? WHERE \
    rowid=?;', (updated_on, name, address1, address2, city, state, postal_code, country, modify_company))
    conn.commit()
    return


# Company menu option 3
def delete(delete_company):
    conn.execute('DELETE FROM company WHERE rowid=?;', delete_company)
    conn.commit()
    return


# Company menu option 4
def last_entries(how_many):
    for row in conn.execute('SELECT * FROM company ORDER BY rowid DESC LIMIT ?;', how_many):
        print(row)
    input("Press ENTER to continue...")
    return


# Company menu option 5
def search(search_company):
    for row in db.dbconnect.execute("SELECT * FROM company WHERE name LIKE ?;", ('%' + search_company + '%',)):
        print(row)
    input("Press ENTER to continue...")
    return
