import json
from django.shortcuts import render, redirect
from .forms import NameForm
from .models import Name
from django.contrib import messages

def index(request):
    """Main page"""
    if request.method != 'POST':
        form = NameForm()
    else:
        form = NameForm(data=request.POST)
        if form.is_valid():
            new_name = form.save(commit=False)
            new_name.save()
            messages.success(request, 'Ddoano do wykresu!')
            return redirect('d3app:index')
    return render(request, 'd3app/index.html', {'form': form})


def chart(request):
    """Chart page"""
    data = list(Name.objects.all())
    dataDictionary = []
    for i in data:
        dataDictionary.append({'name': i.name, 'score': i.age})

    dataJSON = json.dumps(dataDictionary)
    context = {'data': dataJSON}
    return render(request, 'd3app/chart.html', context)

