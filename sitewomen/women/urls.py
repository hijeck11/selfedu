from django.urls import path, re_path, register_converter
from . import views
from . import converters

register_converter(converters.FordigitYearConverter, "year4")
# зарегистрировали конвертер на обрабутку урла archive на 4 цифры

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('addpage/', views.addpage, name='addpage'),
    path('contact/', views.contact, name='contact'),
    path('login/', views.login, name='login'),
    path('post/<slug:post_slug>/', views.show_post, name='post'),
    path('category/<slug:cat_slug>/', views.show_category, name='category'),
    path('tag/<slug:tag_slug>/', views.show_tag_postlist, name='tag')
]