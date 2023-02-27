from django.urls import path

from blog.views import blog, single

app_name = 'blog'

urlpatterns = [
    path('blog/', blog, name='blog'),
    path('single/', single, name='single'),

]
