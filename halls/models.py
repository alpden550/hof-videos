from django.db import models


class Hall(models.Model):

    title = models.CharField('Hall Title', max_length=255)

    class Meta:
        verbose_name = 'Hall'
        verbose_name_plural = 'Halls'

    def __str__(self):
        return self.title


class Video(models.Model):

    title = models.CharField('Video Title', max_length=255)
    url = models.URLField('Video URL')
    youtube_id = models.CharField('YouTube ID', max_length=255)
    hall = models.ForeignKey(
        'halls.Hall',
        verbose_name='Hall',
        on_delete=models.CASCADE,
        related_name='videos',
    )

    class Meta:
        verbose_name = 'Video'
        verbose_name_plural = 'Videos'

    def __str__(self):
        return self.title
