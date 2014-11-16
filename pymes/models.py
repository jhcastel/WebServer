from django.contrib.auth.hashers import make_password, check_password
from djangotoolbox.fields import ListField
import os
from pymongo import MongoClient

def DB_Con():
    xcn = MongoClient(os.environ['MONGOLAB_URI'])
    return xcn

class user():

        def __init_(self):
            xcn = MongoClient(os.environ['MONGOLAB_URI'])
            db = xcn.get_default_database().user
            user = db
            return user

        def save(self, data):
            xcn = MongoClient(os.environ['MONGOLAB_URI'])
            db = xcn.get_default_database().user
            iuser = db.save(data)
            return iuser

        def __unicode__(self):
        	return self.username

        def pk(self):
        	return self.UserID

        def get_user(self, raw_username):
            xcn = MongoClient(os.environ['MONGOLAB_URI'])
            db = xcn.get_default_database().user
            query = db.find_one({'username' : raw_username})
	    return query

        def get_user_all(self, ID_num):
            xcn = MongoClient(os.environ['MONGOLAB_URI'])
            db = xcn.get_default_database().user
            usr2 = db.find_one({'UserID' : int(ID_num)})
            return usr2

        def set_password(self, raw_password):
        	self['password'] = make_password(raw_password)

        def check_password(self, db_pass, raw_password):
        	def setter(raw_password):
        		self.set_password(raw_password)
        		self.save(update_fields=["password"])
 	        return check_password(raw_password, db_pass, setter)

        def is_authenticated(self):
        	return True


class client():
    
    def __init_(self):
        xcn = MongoClient(os.environ['MONGOLAB_URI'])
        db = xcn.get_default_database().client
        cliente = db
        return cliente

    def save(self, data):
        xcn = MongoClient(os.environ['MONGOLAB_URI'])
        db = xcn.get_default_database().client
        icli = db.save(data)
        return icli

    def get_clients(self, raw_idadmin):
        xcn = MongoClient(os.environ['MONGOLAB_URI'])
        db = xcn.get_default_database().client
        query = db.find({'idadmin' : raw_idadmin})
        j = 0
        arr1 = []
        arr2 = []
        datos = {0:'idclient',
		        1:'birthdate',
		        2:'loanamount',
		        3:'loanperiod',
		        4:'loanpurpose',
		        5:'status',
		        6:'risk',
		        7:'created',
		        8:'modified'
		        }

	for q in query:
	    for i in range(9):
		arr2.append(q[datos[i]])
	    	print arr2
	    	arr1.append(arr2)
	    	arr2 = []
	    	j += 1
    	return arr1

    def get_client_all(self, ID_num):
	xcn = MongoClient(os.environ['MONGOLAB_URI'])
        db = xcn.get_default_database().client
        cli = db.find_one({'_id' : ID_num})
	return cli
