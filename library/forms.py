from django import forms
from .models import Car
from django.core.exceptions import ValidationError

class CarForm(forms.ModelForm):

    class Meta:

        model = Car
        fields="__all__"


    #
    # def clean_price(self):
    #     # price = int(self.cleaned_data['price']) * 1.2
    #     # self.cleaned_data['price'] = price
    #     # print(self.cleaned_data['price'])
    #     return float(self.cleaned_data['price'])*1.2

class GetPost(forms.Form):
    brand = forms.CharField(max_length=100)
    model = forms.CharField(max_length=100)
    price = forms.DecimalField(max_digits=8, decimal_places=2)
#
def user_can(name):
    if name.isupper() and len(name) < 5:
        return name
    else:
        raise ValidationError('Привет !!')

BIRTH_YEAR_CHOICES = ['1980', '1981', '1982']
FAVORITE_COLORS_CHOICES = [
    ('blue', 'Blue'),
    ('green', 'Green'),
    ('black', 'Black'),
]
class MyFormNew(forms.Form):
    username = forms.CharField(validators=[user_can], help_text='1',widget=forms.TextInput(attrs ={'class' : 'tool'}))
    email = forms.EmailField(help_text='2', widget=forms.TextInput(attrs ={'class' : 'tool'}))
    note = forms.CharField(help_text='3',widget=forms.NumberInput(attrs ={'class' : 'tool'}))

    # def clean_recipients(self):
    #     data = self.cleaned_data['username']
    #     if "fred" not in data:
    #         raise ValidationError("sdsf")
    #     return data
    birth_year = forms.DateField(widget=forms.SelectDateWidget(years=BIRTH_YEAR_CHOICES))
    favorite_colors = forms.MultipleChoiceField(
        required=False,
        widget=forms.CheckboxSelectMultiple,
        choices=FAVORITE_COLORS_CHOICES,
    )

def validator_dim(value):
    if value < 0:
        raise ValidationError('value should be positive number ')


class DimCarForm(forms.ModelForm):
    price = forms.DecimalField(validators=[validator_dim])

    class Meta:

        model = Car
        fields = '__all__'

    def clean_brand(self):
        data = self.cleaned_data('brand')
        if Car.objects.filter(brand=data):
            raise ValidationError('brand exists')
        if data.isupper():
            raise ValidationError('все должно быть большим')
        return data
    # def clean(self):
    #      cleaned_data = super(DimCarForm, self).clean()