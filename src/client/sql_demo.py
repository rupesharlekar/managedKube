import sqlite3
from employee import Employee

conn = sqlite3.connect('employee.db')

cursor = conn.cursor()


def insert_emp(emp):
    pass


def get_emps_by_name(emp):
    pass


def update_pay(emp, pay):
    pass


def remove_emp(emp):
    pass


# cursor.execute("""CREATE TABLE employees (
#         first text,
#         last text,
#         pay integer
#         )""")

# emp1 = Employee('John', 'Doe', 80000)
# emp1 = Employee('Jane', 'Doe', 40000)

# cursor.execute("INSERT INTO employees VALUES ('Rupesh','Arlekar','5000')")
# cursor.execute("INSERT INTO employees VALUES ( ?, ?, ?)", (emp1.first, emp1.last, emp1.pay))
# cursor.execute("INSERT INTO employees VALUES ( :first, :last, :pay)", {'first': emp1.first, 'last': emp1.last, 'pay': emp1.pay})


# cursor.execute("SELECT * FROM employees WHERE last=?", ('Doe',))
cursor.execute("SELECT * FROM employees WHERE last=:last", {'last': 'Doe'})

print(cursor.fetchall())
conn.commit()
conn.close()
