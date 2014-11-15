from django.contrib.auth.hashers import make_password, check_password
from djangotoolbox.fields import ListField
import os
from pymongo import MongoClient

def DB_Con():
    db = MongoClient(os.environ['MONGOLAB_URI'])
    return db

class user():
        db = MongoClient(os.environ['MONGOLAB_URI'])

        def __init_(self):
            user = db.user
            return user

        def save(self, data):
            iuser = self.insert(data)
            return iuser

        def __unicode__(self):
        	return self.username

        def pk(self):
        	return self.UserID

        def get_user(self, raw_username): 
        	query = user.objects.get(username = raw_username)
        	return query

        def get_user_all(self, ID_num):
            usr2 = user.objects.get(UserID = int(ID_num))
            return usr2

        def set_password(self, raw_password):
        	self.password = make_password(raw_password)

        def check_password(self, raw_password):
        	def setter(raw_password):
        		self.set_password(raw_password)
        		self.save(update_fields=["password"])
        	return check_password(raw_password, self.password, setter)

        def is_authenticated(self):
        	return True


class client():
    db = MongoClient(os.environ['MONGOLAB_URI'])

    def __init_(self):
        cliente = db.client
        return cliente

    def save(self, data):
        icli = self.insert(data)
        return icli

    def get_clients(self, raw_idadmin):
        query = client.objects.get(idadmin = raw_idadmin)
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
	cli = client.objects.get(idclient = ID_num)
	return cli
