# SqlAlchemy
 
import sqlalchemy as sa
import sqlalchemy.orm as orm

from models import Base, Darbuotojas
 
engine = sa.create_engine('sqlite:///Darbuotojai_new2.db') # greitkelis
Session = orm.sessionmaker(bind=engine) # Automobiliu gamykla
session = Session() # Automobilis
 
 
 
# # create the table
# Base.metadata.create_all(engine) # sukuria lentelę pagal modelį
 
#CRUD
 
# Create
new_employee = Darbuotojas(vardas='Jonas', pavarde='Jonaitis', alga=2500)
session.add(new_employee)
session.commit()
 
# Read
def read_employees():
    stm = sa.select(Darbuotojas)
    for employee in session.scalars(stm):
        print(employee.id, employee.vardas, employee.pavarde, employee.alga)
read_employees()
 
# Update
def update_employee(employee_id, new_salary):
    stm = sa.update(Darbuotojas).where(Darbuotojas.id == employee_id).values(alga=new_salary)
    session.execute(stm)
    session.commit()
 
def alternate_update_employee(employee_id, new_salary):
    employee = session.get(Darbuotojas, employee_id)
    if employee:
        employee.alga = new_salary
        session.commit()
# Delete
def delete_employee(employee_id):
    stm = sa.delete(Darbuotojas).where(Darbuotojas.id == employee_id)
    session.execute(stm)
    session.commit()

# hello
print("Hello, world!")