from django import forms
from .models import Contact,Rent,Payment


class ContactForm(forms.ModelForm):
    Name = forms.CharField(required=True)
    From_Email = forms.EmailField(required=True)
    Message = forms.CharField(widget=forms.Textarea,required=True)

    class Meta:
        model = Contact
        fields = ('Name','From_Email','Message',)


class RentedForm(forms.ModelForm):

    Name = forms.EmailField(required=True)


    class Meta:
        model = Rent
        fields = ('Name',)

class PurchaseForm(forms.ModelForm):
    choice = (
    ("Gpay", "Gpay"),
    ("PayPal", "PayPal"),
    ("Amazon Pay", "Amazon Pay"),
    ("Paytm","Paytm"),
    )

    F_Name = forms.CharField(required=True)
    L_Name = forms.CharField(required=True)
    Phone = forms.IntegerField(required=True)
    Payment = forms.ChoiceField(choices = choice)

    class Meta:
        model = Payment
        fields = ('F_Name','L_Name','Phone','Payment')
