import datetime

from django.db import models
from django.utils import timezone


class Post(models.Model):
    post_name = models.CharField(max_length=200, verbose_name='Название поста')
    post_text = models.TextField(verbose_name='Текст')
    pub_date = models.DateTimeField('Дата публикации', default=timezone.now())
    def __str__(self):
        return self.post_text
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Опубликовано недавно?'
    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

class Tag(models.Model):
    tag_name = models.CharField(max_length=200, verbose_name='Наименование')
    def __str__(self):
        return self.tag_name
    class Meta:
        verbose_name = 'Тэг'
        verbose_name_plural = 'Тэги'

class Tags(models.Model):
    tag = models.ForeignKey(Tag)
    post = models.ForeignKey(Post)
    class Meta:
        verbose_name = 'Тэг'
        verbose_name_plural = 'Тэги'

class Comment(models.Model):
    post = models.ForeignKey(Post)
    autor = models.CharField(max_length=200, verbose_name='Автор')
    comment_name = models.CharField(max_length=200, verbose_name='Заголовок')
    comment_text = models.TextField(verbose_name='Комментарий')
    pub_date = models.DateTimeField('Дата публикации', default=timezone.now())
    def __str__(self):
        return self.comment_text
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Опубликовано недавно?'
    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'