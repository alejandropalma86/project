from django.db import models
from django.contrib.auth.models import User


# uno a uno = OneToOne
# uno a muchos = ForeignKey
# muchos a muchos = ManyToMany


class Todo(models.Model):
    title = models.CharField(max_length=100, blank=False, null=True)
    done = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='tudus',
        blank=False,
        null=False,
    )

    def __str__(self):
        return self.title


