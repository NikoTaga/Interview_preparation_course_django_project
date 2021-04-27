
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.template.loader import render_to_string
from django.views.generic.edit import CreateView
from .models import Googs
from .forms import GoodsForm


# Create your views here.

def ajax_test(request):
    return HttpResponse('<h1>AJAX</h1>')


def index(request):
    template_name = 'goods_list.html'
    goods_list = Googs.objects.all()
    goods_str = []
    for i in goods_list:
        goods_str.append(i)

    context = {'table_title': 'Все товары',
               'goods': goods_str}
    return render(request,
                  template_name=template_name,
                  context=context)


# def add(request):
#     template_name = 'goods_add.html'
#     if request.method == 'POST':
#         add_form = GoodsForm(request.POST)
#         if add_form.is_valid():
#             add_form.save()
#             return HttpResponseRedirect('/')
#         else:
#             context = {'form': add_form}
#             return render(request,
#                           template_name=template_name,
#                           context=context)
#     else:
#         add_form = GoodsForm()
#         context = {'form': add_form}
#         return render(request,
#                       template_name=template_name,
#                       context=context)


def add(request):
    template_name = 'goods_add.html'
    if request.method == 'POST':
        add_form = GoodsForm(request.POST)
        return save_good_form(request, add_form, template_name)
    else:
        add_form = GoodsForm()
        return save_good_form(request, add_form, template_name)


class Add(CreateView):
    template_name = 'goods_add.html'
    form_class = GoodsForm
    success_url = '/'


def save_good_form(request, form, template_name):
    data = {}
    if request.method == 'POST':
        if form.is_valid():
            form.save
            print('form.save')
            goods_list = Googs.objects.all()
            context = {'goods': goods_list}
            data['form_is_valid'] = True
            data['html_good_list'] = render_to_string(template_name='goods_list.html',
                                                      context=context
                                                      )
        else:
            data['form_is_valid'] = False

    context = {'form': form}
    data['html_form'] = render_to_string(template_name=template_name,
                                         context=context,
                                         request=request
                                         )
    return JsonResponse(data)








