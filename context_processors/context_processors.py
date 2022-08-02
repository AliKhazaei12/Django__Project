from Maqalat_app.models import Article,Category



def recent_post(request):
    recent_post = Article.objects.order_by('-updated', '-created')

    return {'recent_post':recent_post}



def category(request):
    category=Category.objects.all()

    return {'category':category}