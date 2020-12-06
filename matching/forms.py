from django import forms


class ContactForm(forms.Form):      # contactページのフォーム
    name = forms.CharField(label='Name', max_length=50)
    email = forms.EmailField(label='Email')
    title = forms.CharField(label='Subject', max_length=100)
    message = forms.CharField(label='Message', widget=forms.Textarea)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['name'].widget.attrs['class'] = 'form-control col-md-6'    # 名前入力フォーム
        self.fields['name'].widget.attrs['placeholder'] = 'Name'

        self.fields['email'].widget.attrs['class'] = 'form-control col-md-6'  # メールアドレス入力フォーム
        self.fields['email'].widget.attrs['placeholder'] = 'Email'

        self.fields['title'].widget.attrs['class'] = 'form-control col-md-12'  # タイトル入力フォーム
        self.fields['title'].widget.attrs['placeholder'] = 'Subject'

        self.fields['message'].widget.attrs['class'] = 'form-control col-md-12'  # 本文入力フォーム
        self.fields['message'].widget.attrs['placeholder'] = 'Message'
