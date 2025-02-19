import sqlite3

# Database setup
connection=sqlite3.connect("student.db")

# Create cursor
cursor=connection.cursor()

# Create the table
create_table_query="""
CREATE TABLE IF NOT EXISTS STUDENT (
    NAME    VARCHAR(25),
    COURSE   VARCHAR(25),
    SECTION VARCHAR(25),
    MARKS   INT
);
"""

cursor.execute(create_table_query)

# Insert Records
sql_query = """INSERT INTO STUDENT (NAME, COURSE, SECTION, MARKS) VALUES (?, ?, ?, ?)"""
values = [
    ('Daniyal Ahmed', 'Data Science', 'A', 90),
    ('Bilal', 'Data Science', 'B', 100),
    ('Ahmed', 'Data Science', 'A', 86),
    ('Daniyal', 'DEVOPS', 'A', 50),
    ('Bilal', 'DEVOPS', 'B', 35),
    ('Umair', 'DEVOPS', 'C', 35),
]

cursor.executemany(sql_query, values)
connection.commit()

# Display the records
data=cursor.execute("""Select * from STUDENT""")

for row in data:
    print(row)

if connection:
    connection.close()