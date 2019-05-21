from .models import MyUser
from django import  forms

class LoginForm(forms.Form):
    username = forms.CharField(min_length=5,max_length=10,required=True,widget=forms.TextInput,error_messages={"min_length":"不能少于5个字符","max_length":"不能多于十个字符","required":"必填用户名"})


    password = forms.CharField(min_length=5,max_length=10,required=True,widget=forms.PasswordInput)

class RegisterForm(forms.ModelForm):
    class Meta():
        model=MyUser

        fields = ['url']