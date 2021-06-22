from django import forms
from .models import Category, Product, ProductReview
from .widgets import CustomClearableFileInput


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'
    
    image = forms.ImageField(label='Image', required=False, widget=CustomClearableFileInput)

   
class ProductReviewForm(forms.ModelForm):

    class Meta:
       model = ProductReview
       fields = {'rating','review_headline', 'review_text'}
        