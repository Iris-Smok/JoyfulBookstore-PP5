from django import forms
from .widgets import CustomClearableFileInput
from .models import Book, Category, Review


class CategoryForm(forms.ModelForm):
    """ Category form"""
    class Meta:
        model = Category
        fields = '__all__'


class BookForm(forms.ModelForm):
    """ Book Form """
    class Meta:
        model = Book
        exclude = ('discount', 'rating', 'review_count', 'sort_price')

    image = forms.ImageField(
        label='Image', required=False, widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields['category'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'


class ReviewForm(forms.ModelForm):
    """ Form for leaving rating and review """

    class Meta:
        model = Review
        fields = ['rating', 'body']
        labels = {'body': 'Please Write Your Review'}
