from datetime import datetime
from django.dispatch import receiver
from django.core.mail import  EmailMultiAlternatives
from django.template.loader import render_to_string
from .apscheduler import itstime
from .models import Post, PostCategory, UserSubscribers
from django.db.models.signals import m2m_changed
import datetime

#
# @receiver(m2m_changed,sender=Post.postCategory.through)
# def notify_post_create(sender,instance,action,**kwargs):
#     if action == 'post_add':
#         for cat in instance.postCategory.all():
#             for subscribe in UserSubscribers.objects.filter(category=cat):
#                 msg = EmailMultiAlternatives(
#                     subject=instance.title,
#                     body=instance.text,
#                     from_email='Django07.22@yandex.ru',
#                     to=[subscribe.user.email],
#                 )
#                 html_content = render_to_string(
#                     'news_portal/post_created.html',
#                 {
#                     'post': instance,
#                     'recipient': subscribe.user.email
#                  }
#                  )
#
#                 msg.attach_alternative(html_content, "text/html")
#                 msg.send()
#
#
#                 print(f'{instance.title} {instance.text}')
#                 print('Уведомление отослано подписчику ', subscribe.user, 'на почту', subscribe.user.email,' на тему ', subscribe.category)
#
#
# @receiver(itstime, sender='Weekly')
# def mailing_list(sender,instance,**kwargs):
#     for post in Post.objects.filter(created__gt=(datetime.date.today() - datetime.timedelta(days=7))):
#         for cat in PostCategory.objects.filter(postThrough=post):
#             for subscribe in UserSubscribers.objects.filter(category=cat.category):
#                 msg = EmailMultiAlternatives(
#                     subject=instance.title,
#                     body=instance.text,
#                     from_email='Django07.22@yandex.ru',
#                     to=[subscribe.user.email],
#                 )
#                 html_content = render_to_string(
#                     'news_portal/mailing_list.html',
#                     {
#                         'post': instance,
#                         'recipient': subscribe.user.email
#                     }
#                 )
#
#                 msg.attach_alternative(html_content, "text/html")
#                 msg.send()
#
#                 print('Уведомление отослано подписчику ', subscribe.subscriber, ' на тему ', subscribe.category)
#




