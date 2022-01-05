from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class EditorList(models.Model):
    author=models.ForeignKey(User,on_delete=models.CASCADE,related_name="author")
    editor=models.ForeignKey(User,on_delete=models.CASCADE,related_name="editor")
    status=models.BooleanField(default=True)
    timestamp=models.DateTimeField(auto_now=True,auto_now_add=False)

    def __str__(self):
        return '{}-{}'.format(self.author,self.editor)