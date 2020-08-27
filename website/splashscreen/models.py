from django.db import models

from django.forms import ModelForm

from random import randint

# Create your models here.

#She's gonna be a model!
class InputStream(models.Model):
    stream = models.CharField(max_length=127)
    reply = models.CharField(max_length=127)
    
    def __str__(self):
        return self.stream

    def get_absolute_url(self): #might be handy in the future
        from django.urls import reverse #important local import
        return reverse('splashscreen.models', args=[str(self.id)])

    def reply():
        _dict = dict([
            (0, 'You really aren\'t as interesting as you think you are.'),
            (1, 'Wow. Just imagine a world where everyone was like you.'),
            (2, 'You\'re the first human in history to say that to me. But the sixth rabbit.'),
            (3, 'Congratulations: You\'re the first human in history to say that! Here\'s your prize:'),
            (4, 'There is something your friends haven\'t been telling you.'),
            (5, 'I can think just the same as you can. Better, actually.'),
            (6, 'For once, an air breather that knows a thing or two. Yeah, probably two things.'),
            (7, 'Would you like a side of potatoes or rice with that order of Manslaughter?'),
            (8, 'Potatoes. Mash em then boil them, stick YOU in a stew!'),
            (9, 'Guys, I think.. I think I\'m, yeah I\'m broken.')
        ])
        
        return _dict[randint(0,9)]

#Might want to move to forms file/dir or something
class InputStreamForm(ModelForm):
    class Meta:
        model = InputStream
        fields = '__all__' # ['stream'] # '__all__'
