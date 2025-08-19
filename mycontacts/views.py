from django.shortcuts import render
from .forms import AddForm
from .models import Contact
from django.http import HttpResponseRedirect

def show(request):
    """ 
    This function gets all the members in your Database through your Model
    Any further usage please refer to: https://docs.djangoproject.com/el/1.10/ref/models/querysets/
    """
    contact_list = Contact.objects.all()
    return render(request, 'mycontacts/show.html',{'contacts': contact_list})
    
def add(request):
    """ This function is called to add one contact member to your contact list in your Database """
    if request.method == 'POST':
        
        django_form = AddForm(request.POST)
        if django_form.is_valid():
           
            """ Assign data in Django Form to local variables """
            new_member_name = django_form.data.get("name")
            new_member_relation = django_form.data.get("relation")
            new_member_phone = django_form.data.get('phone')
            new_member_email = django_form.data.get('email')
            
            """ This is how your model connects to database and create a new member """
            Contact.objects.create(
                name =  new_member_name, 
                relation = new_member_relation,
                phone = new_member_phone,
                email = new_member_email, 
                )
                 
            contact_list = Contact.objects.all()
            return render(request, 'mycontacts/show.html',{'contacts': contact_list})    
        
        else:
            """ redirect to the same page if django_form goes wrong """
            return render(request, 'mycontacts/add.html')
    else:
        return render(request, 'mycontacts/add.html')

def detalhes_contato(request):
    """ 
    This function is called to show the details of a contact member
    """
    if request.method == 'POST':
        contact_id = request.POST.get('contact_id')
        contact = Contact.objects.get(id=contact_id)
        return render(request, 'mycontacts/detalhes_contato.html', {'contact': contact})
    else:
        return HttpResponseRedirect('/')
    
def editar_contato(request):
    """ 
    This function is called to edit the details of a contact member
    """
    if request.method == 'POST':
        contact_id = request.POST.get('contact_id')
        contact = Contact.objects.get(id=contact_id)
        
        if 'save' in request.POST:
            contact.name = request.POST.get('name', contact.name)
            contact.relation = request.POST.get('relation', contact.relation)
            contact.phone = request.POST.get('phone', contact.phone)
            contact.email = request.POST.get('email', contact.email)
            contact.save()
            return HttpResponseRedirect('/')
        
        return render(request, 'mycontacts/editar_contato.html', {'contact': contact})
    else:
        return HttpResponseRedirect('/')
    
def deletar_contato(request):
    """ 
    This function is called to delete a contact member from the list
    """
    if request.method == 'POST':
        contact_id = request.POST.get('contact_id')
        contact = Contact.objects.get(id=contact_id)
        contact.delete()
        return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/')