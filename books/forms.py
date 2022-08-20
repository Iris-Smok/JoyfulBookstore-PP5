from django import forms
from .widgets import CustomClearableFileInput
from django.core.exceptions import ValidationError
from .models import Book, Category


class CategoryForm(forms.ModelForm):
    """ Category form"""
    class Meta:
        model = Category
        fields = '__all__'


class BookForm(forms.ModelForm):
    """ Book Form """
    class Meta:
        model = Book
        exclude = ('discount', 'rating', 'add_to_whishlist', 'review_count',)

    image = forms.ImageField(
        label='Image', required=False, widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields['category'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'

    def validate_initial_price(self):
        """
        Make sure that the sale_price is never higher
        than the price
        """
        sale_price = self.cleaned_data['sale_price']
        price = self.cleaned_data['price']
        if price and price <= sale_price:
            raise ValidationError(
                "Add an sale_price only if the product is on sale " +
                "and has a lower current price."
            )
