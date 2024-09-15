from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    follows = models.ManyToManyField("self", related_name="followed_by", symmetrical=False, blank=True)
    # avatar = models.ImageField()

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        user_profile = Profile(user=instance)
        user_profile.save()
        user_profile.follows.add(instance.profile)
        user_profile.save()


class Scrawl(models.Model):
    SCRAWL_TYPES = {
        'Poem': 'Poem',
        'Lyrics': 'Lyrics',
        'Excerpt': 'Excerpt',
        'Drabble': 'Drabble',
    }
    user = models.ForeignKey(User, related_name='scrawls', on_delete=models.CASCADE)
    type = models.CharField(max_length=10, choices=SCRAWL_TYPES)
    body = models.CharField(max_length=3000)
    quilled_by = models.ManyToManyField(User, related_name="quilled_scrawls", blank=True)
    quills = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    saved_by = models.ManyToManyField(User, related_name="saved_scrawls", blank=True)

    def __str__(self):
        return (
            f'{self.user} - '
            f'{self.body[:30]}... '
            f'({self.quills})'
        )


class Comment(models.Model):
    user = models.ForeignKey(User, related_name='comments', on_delete=models.CASCADE)
    scrawl = models.ForeignKey(Scrawl, related_name='comments', on_delete=models.CASCADE)
    body = models.CharField(max_length=500)
    quilled_by = models.ManyToManyField(User, related_name="quilled_comments", blank=True)
    quills = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return (
            f'{self.user} '
            f'({self.created_at:%d-%m-%Y %H:%M}): '
            f'{self.body[:30]}...'
        )
