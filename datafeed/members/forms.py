from django.forms import ModelForm
from .models import Member


class CustomerForm(ModelForm):
    class Meta:
        model = Member
        fields = '__all__'