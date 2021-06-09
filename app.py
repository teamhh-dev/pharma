from html.entities import html5
from flask import Flask, json,render_template,redirect,jsonify
# from flask_sqlalchemy import SQLAlchemy
# from flask_admin import Admin 
# from flask_admin.contrib.sqla import ModelView
from os import remove
from os.path import join
from flask.globals import request
from DBHandler import *
from werkzeug.utils import secure_filename

ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = './images'
#for database configration
#app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sqlite3.db'
app.config.from_object("config")
#db = SQLAlchemy(app)
# from models import *
#db.create_all()
#end Configration

"""
set FLASK_APP=app.py
set FLASK_ENV=development
flask run

"""

@app.route('/')
def home():
    """user = User.objects(name='admin',password='admin@example.com').first()
    if user:
        login_user(user)
        print("Admin")
    """

    return render_template("dashboard.html")

@app.route('/availableStock')
def availableStock():
    return render_template("availableStock.html")
@app.route('/addInvoice')
def addInvoice():
    return render_template("addInvoice.html")
@app.route('/addPurchase')
def addPurchase():
    return render_template("addPurchase.html")

@app.route('/return_list')
def return_list():
    return render_template("return_list.html")

@app.route('/invoiceList')
def invoiceList():
    return render_template("invoiceList.html")

@app.route('/purchaseList')
def purchaseList():
    return render_template("purchaseList.html")

@app.route('/addMedicine',methods=['POST','GET'])
def addMedicine():
    db=DBHandler(app.config['DB_HOST'],app.config['DB_ID'],app.config['DB_PASSWORD'],app.config['DB_NAME'])

    if request.method=="POST":
        if request.form['Submit']=="Save":
            imageExtensionFlag=True

            name=request.form['name']
            category=request.form['category']
            unit=request.form['unit']
            details=request.form['details']
            price=request.form['price']
            manufacturerName=request.form['manufacturername']
            manufacturerPrice=request.form['manufacturerprice']
            image=request.files['image']
            imageName=None
            if image:
                imageName=secure_filename(str(db.getImageName())+"."+image.filename.split(".")[1])

            if imageName and not imageName.split(".")[1] in app.config['ALLOWED_EXTENSIONS']:
                imageExtensionFlag=False

            print(name,category,unit,details,price,manufacturerName,manufacturerPrice,imageName,imageExtensionFlag)
            if imageExtensionFlag:
                if not imageName:
                    imageName="None"
                if db.addMedicine(name,category,unit,details,price,manufacturerName,manufacturerPrice,imageName):
                    try:
                        image.save(app.config['UPLOAD_FOLDER']+imageName)
                    except Exception as e:
                        print(e.__str__())
                    return render_template("addMedicine.html",status="Added Medicine!")
                else:
                    return render_template("addMedicine.html",status="Error Adding Medicine!")

    return render_template("addMedicine.html")

@app.route('/medicineList',methods=['GET','POST'])
def medicineList():
    db=DBHandler(app.config['DB_HOST'],app.config['DB_ID'],app.config['DB_PASSWORD'],app.config['DB_NAME'])
    # print(db.getAllMedicines())
    if request.method=="POST":
        id=request.form['ide']
        name=request.form['name']
        category=request.form['category']
        unit=request.form['unit']
        details=request.form['details']
        price=request.form['price']
        manufacturerName=request.form['manufacturername']
        manufacturerPrice=request.form['manufacturerprice']
        print(name,category,unit,details,price,manufacturerName,manufacturerPrice,id)
        image=request.files['image']
        imageName=id+"."+"jpg"
        print(image.filename)
        if not image.filename:
            print("No Image!")
            # image.save(app.config['UPLOAD_FOLDER']+imageName)

        else:
            path=join(app.config['UPLOAD_FOLDER'],imageName)
            try:
                remove(path)
            except Exception as e:
                print("No Image")
            finally:
                if image.filename:
                    image.save(path)

        db.updateMedicine(name,category,unit,details,price,manufacturerName,manufacturerPrice,imageName,id)
        
    # updated=db.updateMedicine(name,category,unit,detail
    medicines_list=db.getAllMedicines()
    for medicine in medicines_list:
        medicine['image']="medicine-images/"+medicine['image']
    return render_template("medicineList.html",medicines=medicines_list)


@app.route("/getMedicine",methods=["GET","POST"])
def getMedicine():
    db=DBHandler(app.config['DB_HOST'],app.config['DB_ID'],app.config['DB_PASSWORD'],app.config['DB_NAME'])
    medicine=db.getMedicine(request.args.get("id"))

    return jsonify(medicine)
@app.route("/deleteMedicine",methods=["DELETE"])
def deleteMedicine():
    db=DBHandler(app.config['DB_HOST'],app.config['DB_ID'],app.config['DB_PASSWORD'],app.config['DB_NAME'])
    id=request.form['id']
    medicine=db.getMedicine(id)
    deleted=db.deleteMedicine(id)

    if deleted:
        try:
            remove(join(app.config['UPLOAD_FOLDER'],medicine['image']))
        except Exception as e:
            print("No File Detected!")
        return jsonify({"msg":"Deleted Successfully!"})
    else:
        return jsonify({"msg":"Not Deleted Error 404!"})
@app.route("/updateMedicine",methods=["PUT"])
def updateMedicine():
    print("update Call")
    db=DBHandler(app.config['DB_HOST'],app.config['DB_ID'],app.config['DB_PASSWORD'],app.config['DB_NAME'])
    
    id=request.form['id']
    name=request.form['name']
    category=request.form['category']
    unit=request.form['unit']
    details=request.form['details']
    price=request.form['price']
    manufacturerName=request.form['manufacturername']
    manufacturerPrice=request.form['manufacturerprice']
    
    image=request.files['image']
    imageName=id+"."+"jpg"
    
    if image.filename==None:
        image.save(app.config['UPLOAD_FOLDER']+imageName)

    else:
        path=join(app.config['UPLOAD_FOLDER'],imageName)
        remove(path)
        image.save(path)

    print(name,category,unit,details,price,manufacturerName,manufacturerPrice,imageName,id)
    # updated=db.updateMedicine(name,category,unit,details,price,manufacturerName,manufacturerPrice,imageName,id)

    if True:
        return jsonify({"msg":"Updated Successfully!"})
    else:
        return jsonify({"msg":"Not Updated Error 404!"})


@app.route("/getAllMedicines",methods=["GET"])
def getAllMedicines():
    db=DBHandler(app.config['DB_HOST'],app.config['DB_ID'],app.config['DB_PASSWORD'],app.config['DB_NAME'])
    medicines=db.getAllMedicines()
    return jsonify(medicines)
    # if medicines:
    #     return jsonify(medicines)
    # else:
    #     return jsonify({"msg":"Not Medicine Found!"})


if __name__ == '__main__':
    #db=DBHandler(app.config['DB_HOST'],app.config['DB_ID'],app.config['DB_PASSWORD'],app.config['DB_NAME'])
    #print(db.getAllMedicines())
    app.run(debug=True)
    
    
"""<input class="select2-search__field" type="search" tabindex="0" autocorrect="off" autocapitalize="none" spellcheck="false" role="searchbox" aria-autocomplete="list" autocomplete="off" aria-controls="select2-unit-12-results">
"""
