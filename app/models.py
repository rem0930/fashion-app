from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images', verbose_name='イメージ画像', null=True, blank=True) # 追加
    comment = models.TextField("コメント")
    hashtag =models.TextField("ハッシュタグ")
    created = models.DateTimeField("作成日", auto_now=True)

    def __str__(self):
        return str(self.author)