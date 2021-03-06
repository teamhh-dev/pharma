import pymysql
from pymysql.cursors import DictCursor
from werkzeug.datastructures import cache_property
from werkzeug.utils import ArgumentValidationError

class DBHandler:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        try:
            self.connect()
        except Exception as e:
            raise Exception("<h1>No Db Connection</h1>")
    def connect(self):
        try:
            self.db=pymysql.connect(host=self.host,user=self.user,password=self.password,database=self.database)
            self.cursor=self.db.cursor(DictCursor)
            self.cursor.execute("CREATE TABLE if not exists `medicine_list` ( `id` INT NOT NULL AUTO_INCREMENT , `name` VARCHAR(100) NOT NULL ,`generic_name` VARCHAR(100) NOT NULL , `category` VARCHAR(20) NOT NULL , `unit` VARCHAR(20) NOT NULL , `details` VARCHAR(1000) NOT NULL , `price` FLOAT(10,2) NOT NULL , `manufacturer_name` VARCHAR(50) NOT NULL , `manufacturer_price` FLOAT(10,2) NOT NULL , `image` VARCHAR(200) NOT NULL , PRIMARY KEY (`id`)) ENGINE = InnoDB;")
            self.db.commit()
        except Exception as e:
            raise Exception("<h1>No Db Connection</h1>")
    def getImageName(self):
        query="SELECT `AUTO_INCREMENT` as imagename FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_SCHEMA = 'pharma' AND TABLE_NAME = 'medicine_list'"
        self.cursor.execute(query)
        name=self.cursor.fetchone()
        return name['imagename']

    def addMedicine(self,name,generic_name,category,unit,details,price,manufacturerName,manufacturerPrice,imageName):
        query="INSERT INTO `medicine_list` (`id`, `name`,`generic_name`, `category`, `unit`, `details`, `price`, `manufacturer_name`, `manufacturer_price`, `image`) VALUES (NULL, %s,%s, %s, %s,%s, %s,%s,%s,%s)"
        args=(name,generic_name,category,unit,details,price,manufacturerName,manufacturerPrice,imageName)
        try:
            self.cursor.execute(query,args)
            self.db.commit()
        except Exception as e:
            print(e.__str__())
            return False
        return True
    def getMedicine(self,id):
        query="Select * from medicine_list where id=%s"
        args=(id)
        try:
            self.cursor.execute(query,args)
        except Exception as e:
            return False
        return self.cursor.fetchone()
    def getAllMedicines(self):

        medicine_list=[]
        self.cursor.execute("Select * from medicine_list")

        for medicine in self.cursor:
            medicine_list.append(medicine)

        return medicine_list
    def deleteMedicine(self,id):
        query="Delete From `medicine_list` where `id`=%s"
        args=(id)

        try:
            self.cursor.execute(query,args)
            self.db.commit()

        except Exception as e:
            return False
        return True

    def updateMedicine(self,name,generic_name,category,unit,details,price,manufacturerName,manufacturerPrice,imageName,id):
        query="UPDATE `medicine_list` set `name`=%s,`generic_name`=%s,, `category`=%s, `unit`=%s, `details`=%s, `price`=%s, `manufacturer_name`=%s, `manufacturer_price`=%s, `image`=%s where `id`=%s"
        args=(name,generic_name,category,unit,details,price,manufacturerName,manufacturerPrice,imageName,id)
        try:
            self.cursor.execute(query,args)
            self.db.commit()
        except Exception as e:
            print(e.__str__())
            return False
        return True
    def getMedicinesByFilteredNames(self,searchInput):
        query="Select * from `medicine_list` where lower(name) like (%s)"
        args=("%"+searchInput.lower()+"%")
        result=None
        try:
            self.cursor.execute(query,args)
            result=self.cursor.fetchall()
            return result
        except Exception as e:
            print(e.__str__())
            return False
        