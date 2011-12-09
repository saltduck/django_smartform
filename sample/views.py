from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect

from forms import SampleForm

# Create your views here.

def sample1(request):
    """ normal form """
    if request.method == 'GET':
        form = SampleForm()
    else:
        form = SampleForm(request.POST)
        if form.is_valid():
            # do bussiness logic...
            # generate response
            return HttpResponseRedirect('/sample/ok/')
    return render_to_response('sample/sample1.html',
            {'form':form})

def sample2(request):
    """ ajax form """
    if request.method == 'GET':
        form = SampleForm(ajax=True)
    else:
        form = SampleForm(request.POST)
        if form.is_valid():
            # do bussiness logic...
            # generate response
            return form.response_ok()
        else:
            return form.response_bad()
    return render_to_response('sample/sample1.html',
            {'form':form})

def ok(request):
    return HttpResponse('ok')
