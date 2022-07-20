from distutils.command.upload import upload
from django.db import models
from django.forms import CharField

class Network(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    logo = models.URLField(blank=True, null=True)
    # logo = models.FileField(upload_to='logos/', blank=True, null=True)

    def __str__(self):
        return self.name

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254, default='error@nope.com')
    # email = models.CharField(max_length=100)
    password = models.CharField(max_length=30)
    photo = models.URLField(blank=True, null=True)
    # image = models.FileField(upload_to='profileImages/', blank=True, null=True)
    location = models.CharField(max_length=100)
    # socialmedia = models.ForeignKey(SocialMedia, null=True, on_delete=models.SET_NULL, related_name='users')
    linkedin = models.URLField(blank=True, null=True)
    github = models.URLField(blank=True, null=True)
    facebook = models.URLField(blank=True, null=True)
    twitter = models.URLField(blank=True, null=True)
    instagram = models.URLField(blank=True, null=True)
    networks = models.ForeignKey(Network, on_delete=models.PROTECT, related_name='users')
        # can networks be plural? need option for more than one... **MANY TO MANY**
    # on_delete=models.SET_NULL will set this to null if referenced object is deleted
    # on_delete=models.PROTECT will not allow referenced object to be deleted

    def __str__(self):
        return self.name

class Post(models.Model):
    network = models.ForeignKey(Network, on_delete=models.CASCADE, related_name='posts', default=1)
    topic = models.CharField(max_length=100, default='Life')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    body = models.TextField(blank=True, null=True)
    # body field has blank and null in case user posts only an image
    imageURL = models.TextField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True, null=True)
    # image = models.FileField(upload_to='images/', blank=True, null=True)

    class Meta:
        ordering = ['timestamp']

    def __str__(self):
        if len(self.body) < 20:
            return 'Post {} on {} by {}'.format(self.body, self.topic, self.author)
        else:
            return 'Post {} on {} by {}'.format(self.body[:20] + '...', self.topic, self.author)

# class Tweet(models.Model):
#     uuid = models.UUIDField(unique=True, auto_created=True, default=uuid.uuid4)
#     user_string = models.CharField(max_length=100, default='unknown_user')
#     content = models.CharField(max_length=256)

#     def __str__(self):
#         if len(self.content) < 20:
#             return str(self.content)
#         else:
#             return str( self.content[:20] + " ...")

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    body = models.TextField(blank=True, null=True)
    # body field has blank and null in case user posts only an image
    timestamp = models.DateTimeField(auto_now_add=True, null=True)
    # image = models.FileField(upload_to='images/', blank=True, null=True)

    class Meta:
        ordering = ['timestamp']

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.author)

class Event(models.Model):
    name =  models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    dateTime = models.DateTimeField()
    description = models.TextField()
    network = models.ForeignKey(Network, on_delete=models.CASCADE, related_name='events', default='Network Unknown')

    def __str__(self):
        return self.name