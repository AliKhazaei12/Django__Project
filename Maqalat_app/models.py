
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.text import slugify



class Category(models.Model):
    title=models.CharField(max_length=30,unique=True)
    created=models.DateTimeField(auto_now_add=True)
    

  

    def __str__(self):
        return self.title





class Article(models.Model):
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    category=models.ManyToManyField(Category,related_name='articles')
    title=models.CharField(max_length=50)
    body=models.TextField()
    image=models.ImageField(upload_to='images/articl')
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    slug=models.SlugField(unique=True,blank=True)

    def save(
        self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        self.slug=slugify(self.title)
        super(Article, self).save()


    def get_absolute_ulr(self):
        return reverse('Maqalat:detail',kwargs={'slug':self.slug})


    def __str__(self):
        return f'{self.title} - {self.body[:30]}'




class Comment(models.Model):
    article=models.ForeignKey(Article,on_delete=models.CASCADE,related_name='comment')
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    created=models.DateTimeField(auto_now_add=True)
    text=models.TextField()
    patern=models.ForeignKey('self',null=True,blank=True,on_delete=models.CASCADE ,related_name='repleis')


    class Meta:
        ordering=['-created',]


    def __str__(self):
        return f'{self.user} - {self.text[:15]}'






