from django.contrib.auth.hashers import make_password
from django.contrib.admin import widgets
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext_lazy
from django import forms
import datetime
from bootstrap3_datetime.widgets import DateTimePicker
from django import forms
from pymes.model_Backend import get_cats, get_rates
from iron_mq import *
import pymongo
from pymongo import MongoClient()

class UserForm(forms.Form):
    username = forms.CharField(max_length=20, required=True, label="Username")
    password = forms.CharField(widget=forms.PasswordInput(), required=True, label="Password")
    fname = forms.CharField(max_length=50, required=True, label="First Name")
    lname = forms.CharField(max_length=50, required=True, label="Last Name")
    mail = forms.CharField(max_length=30, required=True, label="e-mail")

    def save(self):
        user1 = {'username' : self.cleaned_data['username'],
        'password' : make_password(self.cleaned_data['password']),
        'firstname' : self.cleaned_data['fname'],
        'lastname' : self.cleaned_data['lname'],
        'email' : self.cleaned_data['mail'],
        'loantype' : []}
        return user1

def getUser(idadmin):
	reg=user()
	reg=user.objects.get(idadmin)
	return reg

def getLoantypes(idadmin):
	reg=user()
	reg=user.objects.get(idadmin)
	loantypes=set(reg.loantype)
	return loantypes	
	 
class LoanForm(forms.Form):
    category = forms.CharField(max_length=20, required=True, label="Category Name")
    rate = forms.DecimalField(required=True, label="Rate")

    def save(self, idadmin):
        user1 = user()
        user2 = user1.get_user_all(idadmin)
        new_ltype=unicode(self.cleaned_data['category'])+":"+unicode(self.cleaned_data['rate'])
        user2.loantype.add(new_ltype)
        return user2
            		

class ClientForm(forms.Form):
        CHOICES = [(1, u'opc1'), (2, u'opc2'), (3, u'opc3'), (4, u'opc4')]
        idclient=forms.CharField(max_length=10, required=True, label="Id Client")
	birthdate=forms.DateField(widget=DateTimePicker(options={"format": "YYYY-MM-DD","pickTime": False}))
	loanpurpose=forms.ChoiceField(choices=CHOICES)#[(1, u'car'), (2, u'house'), (3, u'other'), (4, u'studies')]) #[(x, x) for x in range(0,100)])
	loanamount=forms.CharField(max_length=20, required=True, label="Loan Amount")
	loanperiod=forms.CharField(max_length=2, required=True, label="Loan Period")
	
    	def save(self, idadmin, cat_dict, rate_dict):
		client1 = {
		'idadmin': int(idadmin),
		'_id' : unicode(self.cleaned_data['idclient']),
		'birthdate' : unicode(self.cleaned_data['birthdate']),
		'loanperiod' : int(self.cleaned_data['loanperiod']),
		'loanpurpose' : cat_dict[int(self.cleaned_data['loanpurpose'])],
		'loanamount' : unicode(self.cleaned_data['loanamount']),
		'loanrate' : rate_dict[int(self.cleaned_data['loanpurpose'])],
		'risk': unicode(0),
		'created' : unicode (datetime.datetime.now().strftime('%Y%m%d%H%M%S')),
		'modified': unicode(datetime.datetime.now().strftime('%Y%m%d%H%M%S')),
		'status' : unicode("Pendiente"),
		'record' : []}
		
		xcn=MongoClient(os.environ['MONGOLAB_URI'])
		db=xcn.get_default_database().client
		db.insert(client)

		#arma estructura para la cola id|amount|periodo|rate
		msg=unicode(client1.idclient)+"|"+unicode(client1.loanamount)+"|"+unicode(client1.loanperiod)+"|"+unicode(client1.loanrate)
		#conexion a la cola queue
		mq=IronMQ()
		queue=mq.queue("queue")
		queue.post(msg)
	        return client1
	
	def __init__(self, custom_choices=None, *args, **kwargs):
		idpyme=kwargs.pop('idpyme')
		super(ClientForm, self).__init__(*args, **kwargs)
		if custom_choices:
            		self.fields['loanpurpose'].choices = custom_choices

class LoanAdminAuthForm(AuthenticationForm):
    """
    Same as Django's AdminAuthenticationForm but allows to login
    any user who is not staff.
    """
    this_is_the_login_form = forms.BooleanField(widget=forms.HiddenInput,
                                initial=1,
                                error_messages={'required': ugettext_lazy(
                                "Please log in again, because your session has"
                                " expired.")})
 
    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        message = "Mensaje de error"
         
        if username and password:
            self.user_cache = authenticate(username=username,
            password=password)
            if self.user_cache is None:
                if u'@' in username:
                    # Mistakenly entered e-mail address instead of username?
                    # Look it up.
                    try:
                        user = User.objects.get(email=username)
                    except (User.DoesNotExist, User.MultipleObjectsReturned):
                        # Nothing to do here, moving along.
                        pass
                    else:
                        if user.check_password(password):
                            message = _("Your e-mail address is not your "
                                        "username."
                                        " Try '%s' instead.") % user.username
                raise forms.ValidationError(message)
            # Removed check for is_staff here!
            elif not self.user_cache.is_active:
                raise forms.ValidationError(message)
        self.check_for_test_cookie()
        return self.cleaned_data
