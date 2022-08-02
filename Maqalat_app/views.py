from django.shortcuts import render
from Maqalat_app.models import Article,Category
from django.core.paginator import Paginator



def post_detail(request,slug):
    article=Article.objects.get(slug=slug)
    return render(request, 'Maqalat_app/post-details.html',{'article':article})





def post_list(request):
     article=Article.objects.all()
     paginator=Paginator(article,2)
     page_number=request.GET.get('page')
     article_list=paginator.get_page(page_number)
     return render(request,'Maqalat_app/post_list.html',{'articles':article_list})



def category_list(request,pk=None):
    category= Category.objects.get(id=pk)
    article=category.articles.all()
    return render(request,'Maqalat_app/post_list.html',{'article':article})

def search(request):
    q = request.GET.get('q')
    article = Article.objects.filter(title__icontains=q)
    page_num = request.GET.get('page')
    paginator = Paginator(article, 1)
    articles = paginator.get_page(page_num)
    return render(request, 'Maqalat_app/post_list.html', {'articles': articles})


def Contact_us(request):
    return render(request,'Maqalat_app/contact_us.html',{})


