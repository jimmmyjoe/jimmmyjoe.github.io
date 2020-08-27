#from django.http import HttpResponse as httpr
#from django.template import loader
from django.template import Context
from django.shortcuts import render

from .models import InputStream, InputStreamForm

# Create your views here.

# Landing page for splashscreen (and currently root)
def index(request):
    reply = ''
    if request.method == 'POST':
        print('POST Request views.py')
        form = InputStreamForm(request.POST)
        if form.is_valid():
            print('Form Valid')
            form.save()
            reply = InputStream.reply()
        else:
            print('Form Invalid')
            form = InputStreamForm() #unbound form
            
    elif request.method == 'GET':
        print('GET Request views.py')
        form = InputStreamForm(request.GET)
        if form.is_valid():
            print('Form Valid')
            form.save()
            reply = InputStream.reply()
        else:
            print('Form Invalid')
            form = InputStreamForm() #unbound form
        
    else: #not post or get
        print('Unknown Request views.py')
        form = InputStreamForm()

    # Context object is stack of dicts w built-in exception handling
    context = Context({'form': form, 'reply': reply}) #context.flatten() or pop()
#    c = {}
#    c['form'] = form # {'form': form,}
    return render(request,'splashscreen/skeleton_terminal.html',context.flatten())
