from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String,Column,Integer,MetaData,Date,DateTime,Boolean,ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy_serializer import SerializerMIxin


metadata = MetaData()
db = SQLAlchemy(metadata=metadata)

class Employee(db.Model,SerializerMIxin):
    __tablename__ = 'employees'
    
    # prevent looping back from reviews and on boarding
    serialize_rules = ('-reviews.employee','-onboarding.employee')

    id = Column(Integer(),primary_key=True)
    name = Column(String(),nullable=False)
    hired_date = Column(Date)

    # rship mapping employee to many reviews
    reviews = relationship('Review',back_populates='employee',cascade='all,delete-orphan')
    # note value assigned to backpopulate is the property name assigned to the other rship in this case employee in review class is the property name
    onboarding = relationship('Onboarding',uselist=False,back_populates='employee',cascade='all,delete-orphan')

class Onboarding(db.Model,SerializerMIxin):
    __tablename__ = 'onboardings'
    # Prevent looping back from Employee
    serialize_rules = ('-employee.onboarding',)

    id = Column(Integer(),primary_key=True)
    orientation = Column(DateTime)
    forms_complete = Column(Boolean(),default=False)

    employee_id = Column(Integer(),ForeignKey('employees.id'))

    employee = db.relationship('Employee',back_populates='onboarding')


class Review(db.Model,SerializerMIxin):
    __tablename__ = 'reviews'
    
    # Prevent looping back from Employee
    serialize_rules = ('-employee.reviews',)


 

    id = Column(Integer(),primary_key=True)
    year = db.Column(Integer())
    summary = db.Column(String())
    # foreign key
    employee_id = Column(Integer(),ForeignKey('employees.id'))
    # rship mapping review to the related employee
    employee = relationship('Employee',back_populates='reviews')