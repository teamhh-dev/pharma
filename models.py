
from app import db
import datetime
from flask_sqlalchemy import SQLAlchemy



class User(db.Model):  
    id = db.Column(db.Integer, primary_key=True) 
    username = db.Column(db.String(80), unique=True, nullable=False)
    name = db.Column(db.String(80), nullable=False)
    
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)
                                                                                    
    def to_json(self):        
        return {"name": self.name,
                "email": self.email}

    def is_authenticated(self):
        return True

    def is_active(self):   
        return True           

    def is_anonymous(self):
        return False          

    def get_id(self):         
        return str(self.id)
class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Category_name = db.Column(db.String(120), nullable=True)
    Status = db.Column(db.Boolean, default=False, nullable=False)
    Medicine = db.relationship("medicine",backref='category')

class Manufacturer(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    Manufacturer_Name=db.Column(db.String(120),nullable=True)
    Email_Name=db.Column(db.String(30),nullable=True)
    Phone=db.Column(db.Integer,nullable=True)
    Address=db.Column(db.String(200),nullable=True)
    Country=db.Column(db.String(30),nullable=True)
    City=db.Column(db.String(30),nullable=True)
    ZipCode=db.Column(db.Integer,nullable=True)
    Previous_Balance=db.Column(db.Integer,nullable=True)
    date = db.Column(db.DateTime, nullable=False,default=datetime.date.today()) 
    Medicine = db.relationship("medicine",backref='Manufacturer')
    Purchase = db.relationship("purchase",backref='Manufacturer')
    
    
    
class Medicine(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Qr_code=db.Column(db.String(120),nullable=True) 
    Strenth=db.Column(db.String(120),nullable=True) 
    Shelf=db.Column(db.String(120),nullable=True) 
    Category =db.Column(db.String(120),nullable=True) 
    Manufacturer_id=db.Column(db.Integer,db.ForeignKey('manufacturer.id'),nullable=False)
    
    Status=db.Column(db.String(120),nullable=True) 
    Medicine_Name=db.Column(db.String(120),nullable=True) 
    Generic_Name=db.Column(db.String(120),nullable=True) 
    Unit=db.Column(db.String(120),nullable=True) 
    Price =db.Column(db.Integer,nullable=True) 
    Image =db.Column(db.Integer,nullable=True) 
    Manufacturer_Price =db.Column(db.Integer,nullable=True)
    date = db.Column(db.DateTime, nullable=False,default=datetime.date.today()) 
    category_id=db.Column(db.Integer, db.ForeignKey('category.id'),nullable=False)
    Purchase = db.relationship("purchase",backref='Medicine')
class Purchase(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    Manufacturer_id=db.Column(db.Integer,db.ForeignKey('manufacturer.id'),nullable=False)
    Medicine=db.Column(db.Integer,db.ForeignKey('medicine.id'),nullable=False)
    
    date = db.Column(db.DateTime, nullable=False,default=datetime.date.today())
 