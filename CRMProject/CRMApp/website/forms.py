from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Record

class SignUpForm(UserCreationForm):
    email      = forms.EmailField(label="", widget=forms.TextInput(attrs={"class":"form-control", "placeholder":"Ex : user@gmail.com"}))
    first_name = forms.CharField(label="", max_length=120, widget=forms.TextInput(attrs={"class":"form-control","placeholder":"Ex: Jhon"}))
    last_name  = forms.CharField(label="", max_length=120, widget=forms.TextInput(attrs={"class":"form-control", "placeholder":"Ex: Wick"}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')
    
    # initialize 
    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class']       = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'Ex : JhonWick'
        self.fields['username'].label                       = 'Username'
        self.fields['username'].help_text                   = '<span class="form-text text-muted"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>'

        self.fields['password1'].widget.attrs['class']       = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Ex: 12jdpL@'
        self.fields['password1'].label                       = 'Password'
        self.fields['password1'].help_text                   = '<ul class="form-text text-muted small"><li>Your password can\'t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can\'t be a commonly used password.</li><li>Your password can\'t be entirely numeric.</li></ul>'

        self.fields['password2'].widget.attrs['class']       = 'from-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Ex: 12jdpL@'
        self.fields['password2'].label                       = 'Confirm Password'
        self.fields['password2'].help_text                   = '<span class="form-text text-muted"><small>Enter the same password as before, for verification.</small></span>'	

class AddNewUser(forms.ModelForm):
    first_name  = forms.CharField(max_length=120, required=True, widget=forms.TextInput(attrs={"class":"form-control", "placeholder":"Ex: Jhon"}))
    last_name   = forms.CharField(max_length=120, required=True, widget=forms.TextInput(attrs={"class":"form-control", "placeholder":"Ex : Jhon"}))
    email = forms.CharField(max_length=120, required=True, widget=forms.TextInput(attrs={"class": "form-control", "placeholder":"Ex : JhonWick@gmail.com"}))
    phone = forms.CharField(max_length=120, required=True, widget=forms.TextInput(attrs= {"class": "form-control", "placeholder": "Ex : +212110101010"}))
    address = forms.CharField(max_length=160, required=False, widget=forms.TextInput(attrs={"class":"form-control", "placeholder":"Ex : NYC 2 stret 4 "}))
    city = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={"class":"form-control", "placeholder":"Ex : NewYork"}))
    state = forms.CharField(max_length=120, required=True, widget=forms.TextInput(attrs={"class":"form-control", "placeholder": "Ex : NewYork-Boston"}))
    zipcode = forms.CharField(max_length=120, required=True, widget=forms.TextInput(attrs={"class":"form-control", "placeholder":"Ex: 99000"}))

    class Meta:
        model = Record
        exclude = ("user",)












