from django import forms
from django.core.mail import EmailMessage


class ContactForm(forms.Form):      # contactページのフォーム
    name = forms.CharField(label='Full Name', max_length=50)
    email = forms.EmailField(label='Email Address')
    title = forms.CharField(label='Subject', max_length=50)
    message = forms.CharField(label='Message', widget=forms.Textarea)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['name'].widget.attrs['class'] = 'form-control col-md-8'    # 名前入力フォーム
        self.fields['name'].widget.attrs['placeholder'] = 'Name'

        self.fields['email'].widget.attrs['class'] = 'form-control col-md-8'  # メールアドレス入力フォーム
        self.fields['email'].widget.attrs['placeholder'] = 'Email'

        self.fields['title'].widget.attrs['class'] = 'form-control col-md-12'  # タイトル入力フォーム
        self.fields['title'].widget.attrs['placeholder'] = 'Subject'

        self.fields['message'].widget.attrs['class'] = 'form-control col-md-12'  # 本文入力フォーム
        self.fields['message'].widget.attrs['placeholder'] = 'Message'


    def send_email(self):
        name = self.cleaned_data['name']
        email = self.cleaned_data['email']
        title = self.cleaned_data['title']
        message = self.cleaned_data['message']

        subject = 'お問合せ {}'.format(title)
        message = '送信者名: {0}\nメールアドレス: {1}\nメッセージ:\n{2}'.format(name, email, message)
        from_email = 'admin@example.com'
        to_list = [
            'test@example.com'
            ]
        cc_list = [
            email
        ]

        # メール編集〜送信処理
        message = EmailMessage(subject=subject, body=message, from_email=from_email, to=to_list, cc=cc_list)
        message.send()
