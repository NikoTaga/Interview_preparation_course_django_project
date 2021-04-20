
from django.shortcuts import render
from .models import Googs

# Create your views here.


def index(request):
    template_name = 'goods_List.html'
    goods_list = Googs.objects.all()
    goods_str = []
    for i in goods_list:
        goods_str.append(i)
    # goods_str = ['111', '222', '333']

    # goods_str = ', '.join(str(good_one for good_one in goods_list))
    context = {'table_title': 'Все товары',
               'goods': goods_str}
    return render(request, template_name=template_name, context=context)



def add(request):
    pass


