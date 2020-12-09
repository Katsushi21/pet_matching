import logging
from django.urls import reverse_lazy    # URLの逆引き機能の追加

from django.views import generic

from .forms import ContactForm

from django.contrib import messages

logger = logging.getLogger(__name__)    # ロガーの取得


class IndexView(generic.TemplateView):
    template_name = "index.html"    # base.pyのtemplate_nameを定義


class ContactView(generic.FormView):
    template_name = "contact.html"
    form_class = ContactForm
    success_url = reverse_lazy('matching:contact')      # 指定URLにリダイレクト

    def form_valid(self, form):
        form.send_email()   # メール送信メソッドの呼び出し
        messages.success(self.request, 'Your message has been sent')
        logger.info('Contact sent by {}'.format(form.cleaned_data['name']))
        return super().form_valid(form)
