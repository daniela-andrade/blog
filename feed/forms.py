from django import forms


class PostForm(forms.Form):
    title = forms.CharField(label='Title', max_length=80)
    text = forms.CharField(label='Post', max_length=140)
