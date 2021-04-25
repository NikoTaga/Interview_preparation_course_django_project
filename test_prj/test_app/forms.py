
from django.forms import ModelForm
from .models import Googs


class GoodsForm(ModelForm):
    class Meta:
        model = Googs
        fields = ('title', 'price', 'measurements', 'vendor')