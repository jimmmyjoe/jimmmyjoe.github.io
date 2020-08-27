#!/usr/bin/env python3

'''
splashscreen/views.py: super simple call and response via 127 character long strings. I think it's ASCII and UTF-8 not sure. At the moment, it selects a random, pre-written response out of a dict of len 10.
'''

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
            reply = InputStream.reply() #static class method call?
        else:
            print('Form Invalid')
            form = InputStreamForm() #unbound form
            
    elif request.method == 'GET':
        print('GET Request views.py')
        form = InputStreamForm(request.GET)
        if form.is_valid():
            print('Form Valid')
            form.save()
            reply = InputStream.reply() #is this an instance method?
        else:
            print('Form Invalid')
            form = InputStreamForm() #unbound form
        
    else: #not post or get?
        print('Unknown Request views.py')
        form = InputStreamForm() #unboud form

    # Context object: stack of dicts w built-in exception handling
    # c = {} --> # c['form'] = form # basically {'form': form,}
    # context.flatten() (many) or context.pop() (singlular)?
    context = Context({'form': form, 'reply': reply})
    #explicit context, shortcut render(R, T, D) where:
    # R (required) = request object used to generate this response.
    # T (required) = full name of template or sequence of Ts (1st found first used).
    # D = dict of values to add to T context. default=empty. views call callables just-in-time for render.
    return render(request,'splashscreen/skeleton_terminal.html',context.flatten())
