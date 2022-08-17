from celery import shared_task
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from .models import Post, UserSubscribers, PostCategory
import datetime



@shared_task
def notify_post_create(user, title, text):
    instance = Post.objects.get(author=user, title=title, text=text)
    for cat in instance.postCategory.all():
            for subscribe in UserSubscribers.objects.filter(category=cat):
                msg = EmailMultiAlternatives(
                    subject=instance.title,
                    body=instance.text,
                    from_email='Django07.22@yandex.ru',
                    to=[subscribe.user.email],
                )
                html_content = render_to_string(
                    'news_portal/post_created.html',
                {
                    'post': instance,
                    'recipient': subscribe.user.email
                 }
                 )

                msg.attach_alternative(html_content, "text/html")
                msg.send()

            print(f'{instance.title} {instance.text}')
            print('Уведомление отослано подписчику ', subscribe.user, 'на почту', subscribe.user.email,' на тему ', subscribe.category)

@shared_task
def weekly_mailing_list():
    for post in Post.objects.filter(created__gt=(datetime.date.today() - datetime.timedelta(days=7))):
        for cat in PostCategory.objects.filter(post=post):
            for subscribe in UserSubscribers.objects.filter(category=cat.category):
                msg = EmailMultiAlternatives(
                    subject=post.title,
                    body=post.text,
                    from_email='Django07.22@yandex.ru',
                    to=[subscribe.user.email],
                )
                html_content = render_to_string(
                    'news_portal/mailing_list.html',
                    {
                        'post': post,
                    'recipient': subscribe.user.email
                    }
                )
                msg.attach_alternative(html_content, "text/html")
                msg.send()

                print('Уведомление отослано подписчику ', subscribe.subscriber, ' на тему ', subscribe.category)