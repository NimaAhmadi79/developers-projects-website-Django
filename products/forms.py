from django.forms import ModelForm
from django import forms
from .models import Product , Comment

class ProductForm(ModelForm):
    class Meta:
        model = Product
        ##fields = '__all__'
        fields=['title','featured_image','description','demo_link','source_link','tags']
        widgets={
            'tags':forms.CheckboxSelectMultiple(),
        }

    def __init__(self, *args ,**kwargs):
        super().__init__(*args ,**kwargs)
            

        # for name, field in self.fields.items():
        #     field.widget.attrs.update({'class': 'input'})

        self.fields['title'].widget.attrs.update({'class':'input'})  
        self.fields['description'].widget.attrs.update({'class':'input'}) 
        self.fields['demo_link'].widget.attrs.update({'class':'input'}) 
        self.fields['source_link'].widget.attrs.update({'class':'input'})   


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields=['Value','body']
        labels={
            'Value':'voto bezar',
            'body':'add a comment with a vote'
        }
    def __init__(self, *args ,**kwargs):
        super().__init__(*args ,**kwargs)
            

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})        