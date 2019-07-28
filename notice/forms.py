from django import forms
from .models import Notice,Comment

class SearchForm(forms.Form):
    search_word = forms.CharField(label='Search Word')

#제목,글,첨부파일
class NewNotice(forms.ModelForm):
    class Meta:
        model=Notice
        fields=['title','writer','body']

class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        fields=['comment_writer','comment_contents']




