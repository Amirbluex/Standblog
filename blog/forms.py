from django import forms
from django.core.validators import ValidationError

from blog.models import Message


class ContactUSForm(forms.Form):
    YEARS = ['2000', '2001', '2002']
    COLORS = [
        ('blue', 'Blue'),
        ('green', 'Green'),
        ('red', 'Red')
    ]
    name = forms.CharField(max_length=10)
    text = forms.CharField(max_length=15)
    birth_year = forms.DateField(widget=forms.SelectDateWidget(years=YEARS))
    favorite_color = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple(), choices=COLORS)

    def clean(self):
        name = self.cleaned_data.get('name')
        text = self.cleaned_data.get('text')

        if name == text:
            raise ValidationError('name and text are the same', code="name_text_same")


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = '__all__'
        widgets = {
            "title": forms.TextInput(attrs={
                "class": 'form-control',
                "placeholder": 'Enter your title'
            }),
            "text": forms.Textarea(attrs={
                "class": 'form-control',
                "placeholder": 'Enter your message'
            }),
        }
