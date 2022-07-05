from django import forms
from article_module.models import Article


class ContactUsModelForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'slug', 'image', 'selected_categories', 'author', 'is_active']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'slug': forms.TextInput(attrs={
                'class': 'form-control'
            }),
        }

        labels = {
            'title': 'نام و نام خانوادگی شما',
            'email': 'ایمیل شما'
        }

        error_messages = {
            'full_name': {
                'required': 'نام و نام خانوادگی اجباری می باشد. لطفا وارد کنید'
            }
        }
