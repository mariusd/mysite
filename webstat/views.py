import webstat
from django.shortcuts import render_to_response
from django.forms.util import ErrorList
from forms import WebstatForm

def index(request):
    webstat_result = None
    if request.method == 'POST':
        form = WebstatForm(request.POST)
        if form.is_valid():
            try:
                webstat_result = webstat.webstat(form.cleaned_data['url'])
            except IOError, e:
                error_msg = "Could not connect to website (wrong address?)"
                form._errors['url'] = ErrorList([error_msg])
    else:
        form = WebstatForm()
    return render_to_response('webstat/index.html', {
        'form' : form,
        'result' : webstat_result,
    })
