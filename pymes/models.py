from django.db import models
from django.contrib.auth.hashers import make_password, check_password
from djangotoolbox.fields import ListField

class user(models.Model):
        UserID = models.AutoField(primary_key=True, unique=True)
        username = models.CharField(max_length=200)
        password = models.CharField(max_length=200)
        firstname = models.CharField(max_length=200)
        lastname = models.CharField(max_length=200)
        email = models.CharField(max_length=100)
        loantype = ListField()

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


class client(models.Model):
    idclient = models.IntegerField(primary_key=True,unique=True)
    idadmin = models.IntegerField()
    birthdate = models.DateField()
    loanamount = models.CharField(max_length=50)
    loanperiod = models.IntegerField()
    loanpurpose = models.CharField(max_length=50)
    loanrate = models.CharField(max_length=5)
    status = models.CharField(max_length=15)
    risk = models.CharField(max_length=5)
    created = models.DateField()
    modified = models.DateField()
    record = ListField()

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
