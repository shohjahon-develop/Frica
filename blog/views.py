from django.http import Http404, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import UpdateView, DeleteView, CreateView

from .forms import ContactForms
from .models import Sale,Add,Lap,Laptop
# Create your views here.
def index(request):
    sales = Sale.objects.all()
    adds = Add.objects.all()
    laps = Lap.objects.all()
    context = {
        "sales":sales,
        "adds":adds,
        "laps":laps
    }
    return render(request,"index.html",context=context)

def contact(request):
    contact = ContactForms(request.POST or None)
    if request.method == "POST" and contact.is_valid():
        contact.save()
        return HttpResponse("<h2>MUVOFIQYIATLI BAJARILDI  !!! <h2/> ")
    context = {
        "contact":contact
    }
    return render(request,"contact.html",context=context)


def computers(request):
    laptops = Laptop.objects.all()
    context = {
        "laptops":laptops
    }
    return render(request,"computers.html",context=context)


def mans_clothes(request):
    return render(request,"mans_clothes.html",context={})


def womans_clothes(request):
    return render(request,"womans_clothes.html",context={})


def addsdetailview(request,id):
    try:
        adds=Add.objects.get(id=id)
        context = {
            "adds":adds
        }
    except adds.DoesNotExist:
        raise Http404("No adds found")
    return render(request,"adds_Detail.html",context=context)

def lapsdetailview(request,id):
    try:
        laps=Lap.objects.get(id=id)
        context = {
            "laps":laps
        }
    except laps.DoesNotExist:
        raise Http404("No laps found")
    return render(request,"laps_Detail.html",context=context)


def laptopsdetailview(request,id):
    try:
        laptops=Laptop.objects.get(id=id)
        context = {
            "laptops":laptops
        }
    except laptops.DoesNotExist:
        raise Http404("No laptops found")
    return render(request,"laptops_Detail.html",context=context)




class LapUpdateView(UpdateView):
    model = Lap
    fields = ('name', 'price','slug','img')
    template_name = 'lapsEdit.html'



class LapDeleteView(DeleteView):
    model = Lap
    template_name = 'laps_Delete.html'
    success_url = reverse_lazy('index')



class LapCreateView(CreateView):
    model = Lap
    template_name = "laps_Create.html"
    fields = ("name","price", "img","slug" )

def lapsDetail(request, laps):
    laps = get_object_or_404(Lap,slug=laps)
    context ={
        "laps":laps
    }
    return render(request,"lapsDetail.html",context=context)





























































































