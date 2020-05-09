from django import forms
from django.contrib.auth.models import User
from .models import Todo



class TodoForm(forms.ModelForm):
    title = forms.CharField()
    done = forms.BooleanField(required=False)
    user = forms.ModelChoiceField(
        queryset=User.objects.all(),
        widget=forms.HiddenInput()
        )
    
    title.widget.attrs.update({'class': input})
    done.widget.attrs.update({'class': input})


    class Meta:
        model = Todo
        fields = ['title', 'done', 'user']




