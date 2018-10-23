from django import forms
from blog.models import blogModel
from ckeditor.widgets import CKEditorWidget

class blogForms(forms.ModelForm):
    content = forms.CharField(widget=CKEditorWidget())
    class Meta:
        model = blogModel
        fields = ['title', 'content', 'image']

    def __init__(self, *args, **kwargs):
        super(blogForms, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs = {'class': 'form-control'}
