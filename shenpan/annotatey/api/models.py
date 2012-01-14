"""Models for the regularisation backend."""
from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic


class Description(models.Model):
    """Description of something, suitable for comments and so on."""
    text = models.TextField(blank=True)
    external_user = models.CharField(max_length=30,
                                     blank = True,
                                     null = True,
                                     help_text="Required. 30 characters or fewer. Letters, numbers and @/./+/-/_ characters")
    system_user = models.ForeignKey(User, null=True, blank=True)
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = generic.GenericForeignKey('content_type', 'object_id')

    def __unicode__(self):
        return "Comment on %s %s." % \
            (self.content_object, self.content_type)


class Token(models.Model):
    """A word or sentence that can be regularised."""
    text = models.CharField(max_length=255)
    descriptions = generic.GenericRelation(Description)

    def __unicode__(self):
        return self.text


class RegularisationType(models.Model):
    """User defined type of regularisation."""
    name = models.CharField(max_length=255)
    descriptions = generic.GenericRelation(Description)

    def __unicode__(self):
        return self.name


class Scope(models.Model):
    """How far the regularisation applies."""
    name = models.CharField(max_length=255)
    descriptions = generic.GenericRelation(Description)

    def __unicode__(self):
        return self.name

class Regularisation(models.Model):
    """A mapping between the token and the lemma."""
    token = models.ForeignKey(Token, related_name = 'tokens')
    lemma = models.ForeignKey(Token, related_name = 'lemmas')
    regularisation_type = models.ForeignKey(RegularisationType)
    scope = models.ForeignKey(Scope)
    context = models.CharField(max_length=255)
    external_user = models.CharField(max_length=30,
                                     blank = True,
                                     null = True,
                                     help_text="Required. 30 characters or fewer. Letters, numbers and @/./+/-/_ characters")
    system_user = models.ForeignKey(User, null=True, blank=True)
    date_utc = models.DateTimeField(auto_now_add=True)

    descriptions = generic.GenericRelation(Description)
    
    def __unicode__(self):
        return "%s to %s" % \
            (self.token, self.lemma)
