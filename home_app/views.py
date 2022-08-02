from django.shortcuts import render
from Maqalat_app.models import Article

def home(request):
    articles=Article.objects.all()
    recent_post=Article.objects.all().order_by('-updated','-created')
    return render(request, 'home_app/home.html', {'article':articles})
# Create your views here.



def sidbar(request):
    render(request,'include/sidebar.html',{})
