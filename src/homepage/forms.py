from django import forms
from homepage.models import UpcomingTrip


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"}))


class RegisterForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    email = forms.EmailField(widget=forms.TextInput(attrs={"class":"form-control"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"}))


class TravelFreeForm(forms.Form):
    name = forms.CharField(required = True, max_length = 50)
    email = forms.CharField(required = True)
    contact = forms.IntegerField(required = False)
    number_of_people = forms.IntegerField()
    destination = forms.CharField(max_length= 50)
    comment = forms.CharField(required= False, widget=forms.Textarea)

class HotSellingForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={"class":"form-control"}))
    query = forms.CharField(widget=forms.Textarea(attrs={"class":"form-control"}))


class UpcomingtripForm(forms.ModelForm):
    class Meta:
        model = UpcomingTrip
        fields = ('title','logo','departure','destination','start_date','end_date','head_description','associated_adventures','price','duration','itenary','inclusions',)
