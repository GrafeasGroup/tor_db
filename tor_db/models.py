# noinspection PyUnresolvedReferences
from tor_db import settings

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Volunteer(models.Model):
    """
    We'll let Django handle the user security bits because frankly it's just
    a lot easier. Make sure to set the security key!

    The only thing that changes here is to make sure that when creating a user,
    an instance of the Django User is created first. For example:

    u = User.objects.create_user(username='bob', password='bobiscool')
    v = Volunteer.objects.create(user=u)

    Then we can use v going forward -- we only need to relate to the Django
    User model (for example, to get the username: v.user.username) when we
    need potentially secure information.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    gamma = models.IntegerField(default=0)
    accepted_coc = models.BooleanField(default=False)
    join_date = models.DateField(default=None)
    last_login_time = models.DateTimeField(default=None)

    def __repr__(self):
        # noinspection PyUnresolvedReferences
        return f"<Volunteer - {self.user.username}>"


class Post(models.Model):
    # It is rare, but possible, for a post to have more than one transcription.
    # Therefore, posts are separate from transcriptions, but there will almost
    # always be one transcription per post.

    post_id = models.CharField(max_length=20)
    claimed_by = models.ForeignKey(
        Volunteer, on_delete=models.CASCADE, related_name='claimed_by'
    )
    completed_by = models.ForeignKey(
        Volunteer, on_delete=models.CASCADE, related_name='completed_by'
    )

    # obviously these should be the same, but it makes it a lot easier to
    # perform checks as to who claimed so that we don't have to query reddit
    claim_time = models.DateTimeField(default=None)
    complete_time = models.DateTimeField(default=None)

    # Where does it come from? Reddit? A library?
    source = models.CharField(max_length=20)
    # recommended max length https://stackoverflow.com/a/219664
    url = models.CharField(max_length=2083)

    def __repr__(self):
        return f"<Post - {self.post_id}>"


class Transcription(models.Model):

    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(Volunteer, on_delete=models.CASCADE)
    # reddit comment ID or similar
    transcription_id = models.CharField(max_length=20)
    # "reddit", "api", "tor_app". Leaving extra characters in case we want
    # to expand the options.
    completion_method = models.CharField(max_length=20)
    url = models.CharField(max_length=2083)
    # force SQL longtext type, per https://stackoverflow.com/a/23169977
    text = models.CharField(max_length=4294000000)

    def __repr__(self):
        return f"<Transcription - {self.post}>"


class APIKeys(models.Model):

    volunteer = models.ForeignKey(
        Volunteer, on_delete=models.CASCADE, related_name='volunteer'
    )
    # all API keys are from UUID4
    api_key = models.CharField(max_length=36)
    is_admin = models.BooleanField(default=False)
    date_granted = models.DateField(timezone.now())
    authorized_by = models.ForeignKey(
        Volunteer, on_delete=models.CASCADE, related_name='authorized_by'
    )
