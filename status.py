#!/usr/bin/env python3


# Status menu option 1
def write_new(db, status):
    db.database_connect.execute('INSERT INTO status(status) VALUES(?);', status)
    db.database_connect.commit()


# Status menu option 2
def replace(db, old_status, new_status):
    db.database_connect.execute('UPDATE status SET status=? WHERE rowid=?;', (new_status, old_status))
    db.database_connect.commit()


# Status menu option 3
def remove(db, remove_status):
    db.database_connect.execute('DELETE FROM status WHERE rowid=?;', remove_status)
    db.database_connect.commit()
