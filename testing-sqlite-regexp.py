#! /usr/bin/env python3
''' testing regular expresion functions in sqlite3 module '''

import sys

def get_sqliter(db_name):
    import sqlite3
    con = sqlite3.connect(db_name)
    cur = con.cursor()
    return (con,cur)

def _regexp(pattern,input_string):
    import re
    pa = result = re.compile(pattern)
    return pa.search(input_string) is not None
    

def main(argv=sys.argv):
    sqliter = get_sqliter('test3.db')
    q = 'create table if not exists test(a text)'
    sqliter[1].execute(q)
    q2 = 'insert into test(a) values(?)'
    values = [
        'ahmed is here',
        'I am taking half day off today',
        'mostafa dous not belive in planning softwere',
        'I am coding might i think',
    ]
    tuple_list = [(x,) for x in values]
    sqliter[1].executemany(q2,tuple_list)
    r=sqliter[1].execute('select * from test')
    print(r.fetchall())
    sqliter[0].create_function("REGEXP",2,_regexp)
    pattern = r"I"
    q3 = 'select * from test where REGEXP(?,a)'
    r2 = sqliter[1].execute(q3,(r'day',))
    print(type(r2))
    print(list(r2))

def reload():
    import importlib
    importlib.reload()

if __name__ == '__main__':
    main()
    
