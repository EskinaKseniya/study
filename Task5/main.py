import sqlite3 as sq
with sq.connect("medicine.db") as db :
    cursor = db.cursor()

    insert_mh = [
        (1, 1, 6, "Ковид", 6),
        (2, 2, 3, "Перелом ноги", 4),
        (3, 3, 3, "Вывих руки", 5),
        (4, 6, 4, "Острый тонзиллит", 7),
        (5, 4, 1, "Острый Аппендицит", 1),
        (6, 5, 2, "Острый Аппендицит", 2)
    ]
    dep = """INSERT INTO medical_history (id, id_patient, id_regularDoctor, diagnosis, id_room) VALUES(?,?,?,?,?);"""
    cursor.executemany(dep, insert_mh)
    db.commit()
    '''
       cursor.execute("""CREATE TABLE patients (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                old INTEGER DEFAULT 25
               )""")

    cursor.execute("""CREATE TABLE medical_history (
               id INTEGER NOT NULL UNIQUE,
               id_patient INTEGER NOT NULL,
               id_room INTEGER NOT NULL,
               diagnosis TEXT NOT NULL,
               id_regularDoctor INTEGER NOT NULL,
               FOREIGN KEY (id_patient) REFERENCES patients (id),
               FOREIGN KEY (id_room) REFERENCES rooms (id_room),
               FOREIGN KEY (id_regularDoctor) REFERENCES doctors (id),
               PRIMARY KEY (id_patient, id_room, id_regularDoctor)
               )""")

    cursor.execute("""CREATE TABLE rooms (
                id_room INTEGER PRIMARY KEY AUTOINCREMENT,
                number INTEGER NOT NULL, 
                id_department INTEGER NOT NULL,
                FOREIGN KEY (id_department) REFERENCES departments (id)
                )""")
    cursor.execute("""CREATE TABLE departments (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    department TEXT NOT NULL
                    )""")
    cursor.execute("""CREATE TABLE doctors (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    specialization TEXT NOT NULL
                    )""")
                    
                    
    insert_departments = [
        (1, "Хирургия"),
        (2, "Травмпункт"),
        (3, "Терапевтическое отд")
    ]
    dep = """INSERT INTO departments (id, department) VALUES(?,?);"""
    cursor.executemany(dep, insert_departments)
    
     insert_rooms = [
        (1, 101, 1),
        (2, 102, 1),
        (3, 103, 1),
        (4, 201, 2),
        (5, 202, 2),
        (6, 301, 3),
        (7, 302, 3)
    ]
    dep = """INSERT INTO rooms (id_room, number, id_department) VALUES(?,?,?);"""
    cursor.executemany(dep, insert_rooms)
    
    insert_patients = [
        (1, "Омар Анна", 25),
        (2, "Иванов Иван", 13),
        (3, "Игнатов Игнат", 13),
        (4, "Папин Родион", 40),
        (5, "Мамина Лана", 20),
        (6, "Устинова Галина", 61)
    ]
    dep = """INSERT INTO patients (id, name, old) VALUES(?,?,?);"""
    cursor.executemany(dep, insert_patients)
    
     insert_doctors = [
        (1, "Катина Катерина", "Хирург"),
        (2, "Резак Виктор", "Хирург"),
        (3, "Сергеев Саша", "Травматолог"),
        (4, "Хачикова Галина", "Терапевт"),
        (5, "Честнейший Михаил", "Травматолог"),
        (6, "Федорова Анна", "Терапевт")
    ]
    dep = """INSERT INTO doctors (id, name, specialization) VALUES(?,?,?);"""
    cursor.executemany(dep, insert_doctors)
    
     insert_mh = [
        (1, 1, 6, "Ковид", 6),
        (2, 2, 3, "Перелом ноги", 4),
        (3, 3, 3, "Вывих руки", 5),
        (4, 6, 4, "Острый тонзиллит", 7),
        (5, 4, 1, "Острый Аппендицит", 1),
        (6, 5, 2, "Острый Аппендицит", 2)
    ]
    dep = """INSERT INTO medical_history (id, id_patient, id_regularDoctor, diagnosis, id_room) VALUES(?,?,?,?,?);"""
    cursor.executemany(dep, insert_mh)
    db.commit()
    
    
    
  cursor.execute("DROP TABLE medical_history")
    cursor.execute("DROP TABLE patients")
    cursor.execute("DROP TABLE rooms")
    cursor.execute("DROP TABLE departments")
    cursor.execute("DROP TABLE doctors")
    
    
        
 
    '''

