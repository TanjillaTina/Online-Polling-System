from django.shortcuts import render
from polling import forms
from polling.models import SetChoices,Voter,MyAdmin
from polling.forms import AdminForm,ChoiceForm,VoterForm
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
# Create your views here.




def index(request):
	ChoiceList=SetChoices.objects.all()
	form=VoterForm()
	if request.method=='POST':
		form=VoterForm(request.POST)
		if form.is_valid():
			form.save(commit=True)
			print("Added")

		else:
			print('Form is Invalid')
	return render(request,'index.html',context={'Choices':ChoiceList,'form':form})




'''
def login(request):
	form=AdminLogin()
	if request.method=='POST':
		form=AdminLogin(request.POST)
		if form.is_valid():
			print("Validation Succes")
			return render(request,'logout.html')
		else:
			messages.error(request, form.errors)
			return HttpResponseRedirect(reverse('login'))

	return render(request,'login.html',{'form':form})
	#return render(request,'login.html')

'''
def login(request):
	form=forms.AdminForm()
	if request.method=='POST':
		form=forms.AdminForm(request.POST)
		if form.is_valid():
			print("Validation Succes")
			name=form.cleaned_data['name']
			password=form.cleaned_data['password']
			if password=='admintest' and name=='admin':
				print("jgjjjhgjg")
				ChoiceList=SetChoices.objects.order_by('place_name')
				return render(request,'adminHome.html',context={'form':form,'Choices':ChoiceList,})

	
	return render(request,'login.html',{'form':form})



def AddVotingOptions(request):
	form=ChoiceForm()
	if request.method=='POST':
		form=ChoiceForm(request.POST)
		if form.is_valid():
			form.save(commit=True)
			print("Added")

		else:
			print('Form is Invalid')
	ChoiceList=SetChoices.objects.order_by('approx_cost')
	#Choices={'Choices':ChoiceList}
	#context={'form':form,'Choices'=Choices}
	return render(request,'adminHome.html',context={'form':form,'Choices':ChoiceList,})


def AddDate(request):
	form=ChoiceForm()
	if request.method=='POST':
		form=ChoiceForm(request.POST)
		if form.is_valid():
			form.save(commit=True)
			print("Added")

		else:
			print('Form is Invalid')

	ChoiceList=SetChoices.objects.order_by('place_name')
	return render(request,'adminHome.html',context={'form':form,'Choices':ChoiceList,})



def SubmitForm(request,choice_pk):
	form=VoterForm()
	if request.method=='POST':
		form=VoterForm(request.POST)
		if form.is_valid():
			form.save(commit=True)
			print("Added")

		else:
			print('Form is Invalid')

	return render(request,'regiform.html',context={'form':form,})

