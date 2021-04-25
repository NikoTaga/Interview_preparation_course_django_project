
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic.edit import CreateView
from .models import Googs
from .forms import GoodsForm


# Create your views here.


def index(request):
    template_name = 'goods_list.html'
    goods_list = Googs.objects.all()
    goods_str = []
    for i in goods_list:
        goods_str.append(i)

    context = {'table_title': 'Все товары',
               'goods': goods_str}
    return render(request, template_name=template_name, context=context)


def add(request):
    template_name = 'goods_add.html'
    if request.method == 'POST':
        add_form = GoodsForm(request.POST)
        if add_form.is_valid():
            add_form.save()
            return HttpResponseRedirect('/')
        else:
            context = {'form': add_form}
            return render(request, template_name=template_name, context=context)
    else:
        add_form = GoodsForm()
        context = {'form': add_form}
        return render(request, template_name=template_name, context=context)


class Add(CreateView):
    template_name = 'goods_add.html'
    form_class = GoodsForm
    success_url = '/'







