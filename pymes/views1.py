from django.shortcuts import render, render_to_response, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse   
from django.contrib import auth, admin
from django.core.context_processors import csrf 
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
import datetime
from forms import UserForm, LoanForm, ClientForm
from pymes.models import client, user
from pymes.model_Backend import get_cats, get_rates, load_cli_info, organize_records, id_cats

def loan_req(request,slug):
	context=RequestContext(request)
	created = False
        cli = ""
        idclient = ""
        birthdate = ""
        loanpurpose = ""
        loanamount = ""
        loanperiod = ""
        risk = ""
        status = ""
	to_url = 'pymes/loan_req.html'
	if request.method == 'POST':
		idpyme=int(slug)
		form=ClientForm(data=request.POST, idpyme=idpyme)
		if form.is_valid():
			rate_dict = get_rates(int(slug))
			cat_dict = id_cats(int(slug))
			clidata = form.save(idpyme, cat_dict, rate_dict)
			client1 = client()
			client1.save(clidata)
			created = True
	        	clinum = request.POST['idclient']
	        	cli = load_cli_info(clinum)
	        	to_url = 'pymes/client_details.html'
	else:
		cat_choices = get_cats(int(slug))
		rate_dict = get_rates(int(slug))
		form = ClientForm(idpyme=int(slug),custom_choices= cat_choices)
		to_url = 'pymes/loan_req.html'
	return render_to_response(to_url, {'form': form, 'created': created, 'idclient': idclient, 'birthdate': birthdate, 'loanpurpose': loanpurpose, 'loanamount': loanamount, 'loanperiod': loanperiod, 'risk': risk, 'status': status}, context)

def cliupdate(request):
    	context=RequestContext(request)
	clinum=request.POST["idclient"]
	cli = load_cli_info(clinum)
    idclient = cli['_id']
    birthdate = cli['birthdate']
    loanpurpose = cli['loanpurpose']
    loanamount = cli['loanamount']
    loanperiod = cli['loanperiod']
    risk = cli['risk']
    status = cli['status']
    recs = organize_records(cli['record'])
	return render_to_response('pymes/client_details.html', {'records': recs, 'idclient': idclient, 'birthdate': birthdate, 'loanpurpose': loanpurpose, 'loanamount': loanamount, 'loanperiod': loanperiod, 'risk': risk, 'status': status }, context)
