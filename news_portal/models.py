from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from django.urls import reverse




class Author(models.Model):
    authorUser = models.OneToOneField(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.authorUser.username


    class Meta:
        verbose_name = "Автор"
        verbose_name_plural = "Автор"


class Category(models.Model):
    name = models.CharField(max_length = 255,unique = True,verbose_name = "Категория")
    slug = models.SlugField(max_length = 255,unique = True,verbose_name= "URL")
    subscribers = models.ManyToManyField(User, blank=True, related_name='subscription', verbose_name='Подписчики',through='UserSubscribers')

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_slug': self.slug})

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.name:
            self.name = slugify(str(self.name))
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ['id']

class UserSubscribers(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Подписчик',blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE,verbose_name='Категория',blank=True)

    def __str__(self):
          return f'{self.user} подписан на категорию {self.category}'


class Post(models.Model):
    author = models.ForeignKey(User, on_delete = models.CASCADE,related_name='autor')
    ARTICLE = 'AR'
    NEWS = 'NW'
    CATEGORY_CHOICES = (
        (ARTICLE, 'Статья'),
        (NEWS, 'Новость')
    )
    categoryType = models.CharField(max_length=2,choices=CATEGORY_CHOICES,default=ARTICLE,
                                    verbose_name="Тип категории")
    dateCreation = models.DateTimeField(auto_now_add=True,verbose_name="Время создания")
    postCategory = models.ManyToManyField(Category,through='PostCategory',verbose_name="Категория ")
    title = models.CharField(max_length=128,verbose_name="Заголовок")
    text = models.TextField(verbose_name="Текст статьи")
    likes = models.ManyToManyField(User,related_name='post_like')



    def number_of_likes(self):
        return self.likes.count()

    def __str__(self):
        return f"{self.title} {self.likes}"

    def get_absolute_url(self):  # добавим абсолютный путь, чтобы после создания нас перебрасывало на страницу с новостями
        return f'/news/{self.id}'


    def preview(self):
      return self.text[0:23] +'...'

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = 'Новости'

    def __str__(self):
        return f"{self. author}:{self.title}"

class PostCategory(models.Model):
    postThrough = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name='Пост в категории')
    categoryThrough = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')

    def __str__(self):
        return f'{self.postThrough},Категория: {self.categoryThrough}'

    class Meta:
        verbose_name = 'Связь категории'
        verbose_name_plural = 'Связь категории'

class Comment(models.Model):
    commentPost = models.ForeignKey(Post, on_delete=models.CASCADE)
    commentUser = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    dataCreation = models.DateTimeField(auto_now_add=True)
