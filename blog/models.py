from django.db import models
from django.utils import timezone
from taggit.managers import TaggableManager
from django.core.urlresolvers import reverse


# Create your models here.
class Article(models.Model):
    title = models.CharField('Заголовок статьи', max_length=400)
    articleContent = models.TextField('Текст статьи')
    pub_date = models.DateTimeField('Дата и время публикации', blank=True)
    tags = TaggableManager()  # поле тега

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:article_detail', args=[str(self.id)])

    # заполнение даты при сохранении
    def save(self, *args, **kwargs):
        if not self.pub_date:
            self.pub_date = timezone.now()
        super(Article, self).save(*args, **kwargs)


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE,
                                related_name='comments')
    caption = models.CharField(max_length=200)
    commentText = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.caption
