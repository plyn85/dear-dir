from django.shortcuts import render, redirect,get_object_or_404
from .models import Entry
from .forms import EntryForm



def index(request):
    entries = Entry.objects.order_by('-date_posted')
# anything in context will be avaliable in the templete
    context = { 'entries' : entries }
    return render(request,'entries/index.html',context)

def add(request): 
    if request.method == "POST":
    # instanchiating the form
        form = EntryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:    
        form = EntryForm()
    context = {'form': form}
   
    return render(request,'entries/add.html',context)

def delete_entry(request,entry_id):
    entry = get_object_or_404(Entry,pk=entry_id)
    form = EntryForm(request.POST,instance=entry)
    entry.delete()
    return redirect('home')

