from django import forms
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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields['category'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'
