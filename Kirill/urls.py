from django.urls import path
from Kirill import views

urlpatterns = [
    path('', views.info, kwargs={"name": "Моргунов Кирилл Витальевич",
                                 "age": 16,
                                 "interests": "программирование"}),
    path('about', views.about, kwargs={"city": "Набережные Челны",
                                       "marks": "ударник",
                                       "learning": "нравится"}),
    path('contacts', views.contacts, kwargs={"github": "https://github.com/pr0pr09er",
                                             "telegram": "@kirich12321",
                                             "phone": "+79393057478"})
]
