from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String,Column,Integer,MetaData,Date,DateTime,Boolean,ForeignKey


metadata = MetaData()
db = SQLAlchemy(metadata=metadata)

class Employee(db.Model):
    __tablename__ = 'employees'

    id = Column(Integer(),primary_key=True)
    name = Column(String(),nullable=False)
    hired_date = Column(Date)

class Onboarding(db.Model):
    __tablename__ = 'onboardings'

    id = Column(Integer(),primary_key=True)
    orientation = Column(DateTime)
    forms_complete = Column(Boolean(),default=False)

class Review():
    __tablename__ = 'reviews'

    id = Column(Integer(),primary_key=True)
    year = db.Column(Integer())
    summary = db.Column(String())
    # foreign key
    employee_id = Column(Integer(),ForeignKey('employees.id'))