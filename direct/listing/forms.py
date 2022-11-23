from django.forms import ModelForm, TextInput, NumberInput, CheckboxInput

from .models import Review


class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ('text','rating',)
        widgets = {
            'text': TextInput(
                attrs={
                    'placeholder': 'Напишите свой отзыв сдесь',
                }
            ),
            'rating': NumberInput(
                attrs={
                    'min': 0,
                    'max': 5,
                }
            )
        }