import sevenseg
from django.shortcuts import render_to_response
from django.forms.util import ErrorList
from django.http import HttpResponseRedirect
from forms import SevensegForm

def index(request):
    if request.method == 'POST':
        form = SevensegForm(request.POST)
        if form.is_valid():
            number = form.cleaned_data['number'].strip()
            result = '\n'.join(sevenseg.generate_sevenseg([int(d) for d in number]))
            data = { 'number' : number, 'sevenseg' : result }
            return render_to_response('sevenseg/number.html', data)
    else:
        form = SevensegForm()
    return render_to_response('sevenseg/index.html', { 'form' : form, })