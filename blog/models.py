from django.db import models
from django.utils import timezone

class Post(models.Model):
	##models.Model makes Django know is a django model and thus stores in the database
	author = models.ForeignKey('auth.User')	##Auth must be another model and user must be attribute
	title = models.CharField(max_length = 200)
	text = models.TextField()
	created_date = models.DateTimeField(default=timezone.now)
	published_date = models.DateTimeField(null=True,blank=True)

	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def approved_comments(self):
		return self.comments.filter(approved_comment=True)

	def __str__(self):
		return self.title

class Comment(models.Model):
	post = models.ForeignKey('blog.Post',related_name='comments')
	##The related_name in models.ForeignKey allows us to have access to 
	##comments from whithin the post model
	author = models.CharField(max_length=200)
	text = models.TextField()
	created_date = models.DateTimeField(default = timezone.now)
	approved_comment = models.BooleanField(default = False)

	def approve(self):
		self.approved_comment=True
		self.save()

	def __str__(self):
		return self.text







