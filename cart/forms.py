from django import forms
from .models import Coupon

class CouponForm(forms.ModelForm):
    code = forms.CharField(widget= forms.TextInput
                           (attrs={'placeholder':'Enter your coupon code here',
                                    'class':'code-text'}))
    class Meta:
        model = Coupon
        fields = ('code',)        