from django.db import models
from django.utils import timezone

STATUS_TO_DO = 'TDO'
STATUS_DOING = 'DNG'
STATUS_DONE = 'DNE'

STATUS_TODO = (
    (STATUS_TO_DO, 'Por Hacer'),
    (STATUS_DOING, 'Haciendo'),
    (STATUS_DONE, 'Hecho'),
)


class IntegerRangeField(models.IntegerField):
    def __init__(self, verbose_name=None, name=None, min_value=None, max_value=None, **kwargs):
        self.min_value, self.max_value = min_value, max_value
        models.IntegerField.__init__(self, verbose_name, name, **kwargs)

    def formfield(self, **kwargs):
        defaults = {'min_value': self.min_value, 'max_value': self.max_value}
        defaults.update(kwargs)
        return super(IntegerRangeField, self).formfield(**defaults)


class Todo(models.Model):
    title = models.CharField(max_length=45)
    description = models.TextField()
    status = models.CharField(max_length=3, choices=STATUS_TODO)
    position = models.PositiveSmallIntegerField()
    priority = IntegerRangeField(min_value=1, max_value=50)
    active = models.BooleanField(default=False)
    created = models.DateTimeField(editable=False)
    modified = models.DateTimeField()

    def save(self, *args, **kwargs):
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super(Todo, self).save(*args, **kwargs)

    def __str__(self):
        return self.title
