from django.db import models
from django.urls import reverse


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_published=LibreAuthors.Status.PUBLISHED)


class LibreAuthors(models.Model):
    class Status(models.IntegerChoices):
        DRAFT = 0, 'DRAFT'
        PUBLISHED = 1, 'PUBLISHED'

    # class Status(models.TextChoices):
    #     DRAFT = 'DF', 'DRAFT'
    #     PUBLISHED = "PB", 'PUBLISHED'

    title = models.CharField(max_length=255, verbose_name='BOOK TITLE')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='SLUG')
    author = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(choices=tuple(map(lambda x: (bool(x[0]), x[1]), Status.choices)),
                                       default=Status.DRAFT, verbose_name='STATUS')
    # is_published = models.CharField(choices=Status.choices, max_length=2,
    #                                 default=Status.DRAFT, verbose_name='STATUS')

    objects = models.Manager()
    published = PublishedManager()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Libres Authors'
        verbose_name_plural = 'Libres Authors'
        ordering = ['-time_create']
        indexes = [
            models.Index(fields=['-time_create'])
        ]

    def get_absolute_url(self):
        return reverse('book', kwargs={'book_slug': self.slug})
