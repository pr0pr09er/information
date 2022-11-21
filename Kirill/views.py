from django.shortcuts import HttpResponse


# Create your views here.
def info(request, name, age, interests):
    return HttpResponse(f"""Обо мне:<br>
                        ФИО: {name}<br>
                        Возраст: {age}<br>
                        Интересы: {interests}""")


def about(request, city, marks, learning):
    return HttpResponse(f"""Дополнительная информация:<br>
                        Город: {city}<br>
                        Успеваемость: {marks}<br>
                        Нравится учиться? {learning}
                        """)


def contacts(request, github, telegram, phone):
    return HttpResponse(f"""Контакты:<br>
                        Гитхаб: {github}<br>
                        Телеграмм: {telegram}<br>
                        Номер телефона: {phone}
                        """)
