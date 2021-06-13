from django import forms
from .models import Category, Product


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'

"""class ProductReviewForm(forms.ModelForm):

    class Meta:
       model = ReviewRating
       fields = {'review_headline', 'review_text'}"""
        