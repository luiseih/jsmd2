#!/usr/bin/env python3

def read(db):
    for row in db.dbconnect.execute('SELECT * FROM status;'):
        print(row)
    return


# Status menu option 1
def write_new(db, status):
    db.dbconnect.execute('INSERT INTO status(status) VALUES(?);', status)
    db.dbconnect.commit()
    return


# Status menu option 2
def replace(db, old_status, new_status):
    db.dbconnect.execute('UPDATE status SET status=? WHERE rowid=?;', (new_status, old_status))
    db.dbconnect.commit()
    return


# Status menu option 3
def remove(db, remove_status):
    db.dbconnect.execute('DELETE FROM status WHERE rowid=?;', remove_status)
    db.dbconnect.commit()
    return
