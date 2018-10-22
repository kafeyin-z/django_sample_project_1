from django import forms
from blog.models import blogModel


class blogForms(forms.ModelForm):
    class Meta:
        model = blogModel
        fields = ['title', 'content', 'image']

    def __init__(self, *args, **kwargs):
        super(blogForms, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs = {'class': 'form-control'}
