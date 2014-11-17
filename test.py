import os
from pymongo import MongoClient

xcn = MongoClient(os.environ['MONGOLAB_URI'])
db = xcn.get_default_database().client
query = db.find({'idadmin' : 1})
j = 0
arr1 = []
arr2 = []
datos = {0:'_id',
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
    arr1.append(arr2)
    arr2 = []	
print arr1
