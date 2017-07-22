from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from .models import Contact
from ContactManagerApp.forms import ContactForm
from django.http.response import HttpResponseRedirect
from django.core.urlresolvers import reverse

def contacts(request):
    contact_list = Contact.objects.all()
    context = {'contact_list': contact_list}
    return render(request, 'ContactManagerApp/contacts.html', context)

def create_contact(request):
    if request.method == 'GET':
        form = ContactForm();
        return render(request, 'ContactManagerApp/manage_contacts.html',{'form':form})

    if request.method == 'POST':
        form = ContactForm(request.POST)
        form.save()
        return HttpResponseRedirect(reverse('contacts') )
       
def edit_contact(request,pk):
    if request.method == 'GET':
        contact = Contact.objects.get(pk=pk)
        form = ContactForm(instance=contact)
        return render(request, 'ContactManagerApp/manage_contacts.html',{'form':form})

    if request.method == 'POST':
        contact = Contact.objects.get(pk=pk)
        form = ContactForm(request.POST, instance=contact)
        form.save() 
        return HttpResponseRedirect(reverse('contacts') )
               
def delete_contact(request,pk):
        contact = Contact.objects.get(pk=pk)
        contact.delete()  
        return HttpResponseRedirect(reverse('contacts') )   