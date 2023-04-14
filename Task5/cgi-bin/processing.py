#!/usr/bin/env python3
import cgi
import sqlite3 as sq
form = cgi.FieldStorage()
n_d = form.getfirst("name_d")
sp = form.getfirst("sp")
n_p = form.getfirst("name_p")
old = form.getfirst("old")
print("Content-type: text/html; charset=utf-8\n")
if (n_d and sp ):
    print(f"{n_d} -> {sp}")
    with sq.connect("medicine.db") as db:
        cursor = db.cursor()
        cursor.execute('INSERT INTO doctors VALUES(NULL,?,?)', (n_d, sp))
        db.commit()
        print("""<!DOCTYPE html>
                        <html lang="en">
                        <head>
                            <meta charset="utf-8">
                            <title>Получилось</title>
                        </head>
                        <body>
                            <a href="../../index.html"><p>Назад</p></a>
                            
                            
                        </body>
                        </html>
                """)
else:
    if (n_p and old ) :
        print(f"{n_p} -> {old}")
        with sq.connect("medicine.db") as db:
            cursor = db.cursor()
            cursor.execute('INSERT INTO patients VALUES(NULL,?,?)', (n_p, old))
            db.commit()
            print("""<!DOCTYPE html>
                            <html lang="en">
                            <head>
                                <meta charset="utf-8">
                                <title>Получилось</title>
                            </head>
                            <body>
                                <a href="../../index.html"><p>Назад</p></a>
                                <p></p>
                            </body>
                            </html>
            """)
            cursor.execute('SELECT *FROM patients')
            print(cursor.fetchall())


    else:
        print("Форма была не полностью заполнена, попробуйте еще раз")
        print("""<!DOCTYPE html>
                <html lang="en">
                <head>
                    <meta charset="utf-8">
                    <title>Не получилось</title>
                </head>
                <body>
                    <a href="../../index.html"><p>Назад</p></a>
                </body>
                </html>
        """)




