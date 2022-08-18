from django.db import models
from mongoengine import Document, fields, EmbeddedDocumentField, EmbeddedDocument, CASCADE

# Create your models here.
class Doc(models.Model):
	doc_name = models.FileField(upload_to='docs/')

	def __str__(self):
		return self.doc_name






"""  tutorial for mongo dom  """
class User(models.Model):
    email = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)


# class Comment(EmbeddedDocument):
#     content = fields.StringField()
#     name = fields.StringField(max_length=120)


# class User(Document):
#     email = fields.StringField(required=True)
#     first_name = fields.StringField(max_length=50)
#     last_name = fields.StringField(max_length=50)
#     comments = fields.ListField(EmbeddedDocumentField(Comment))


# class Post(Document):
#     title = fields.StringField(max_length=120, required=True)
#     author = fields.ReferenceField(User, reverse_delete_rule=CASCADE)

#     meta = {'allow_inheritance': True}


# class TextPost(Post):
#     content = fields.StringField()

# class ImagePost(Post):
#     image_path = fields.StringField()

# class LinkPost(Post):
#     link_url = fields.StringField()