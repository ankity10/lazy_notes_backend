from mongoengine import Document, EmbeddedDocument, fields
# from django.contrib.auth.models import AbstractUserModel
from django.contrib.auth.models import AbstractUser

class ToolInput(EmbeddedDocument):
    name = fields.StringField(required=True)
    value = fields.DynamicField(required=True)

class Tool(Document):
    label = fields.StringField(required=True)
    description = fields.StringField(required=True, null=True)
    inputs = fields.ListField(fields.EmbeddedDocumentField(ToolInput))