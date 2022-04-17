from django.shortcuts import render,redirect
from .forms import NameForm
from .models import Name
# Create your views here.
def index(request):
    if request.method != 'POST':
        form =NameForm()
    else:
        form = NameForm(data=request.POST)
        if form.is_valid():
            new_name=form.save(commit=False)
            new_name.save()
            return redirect('d3app:chart')
    return render(request,'d3app/index.html',{'form':form})


def chart(request):
    data = Name.objects.all()
    context= {'data':data}
    return  render(request,'d3app/chart.html',context)