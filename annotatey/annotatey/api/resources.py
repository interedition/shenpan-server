from django.core.urlresolvers import reverse
from djangorestframework.resources import ModelResource
from annotatey.api.models import Description, Token,\
    RegularisationType, Scope, Regularisation

class DescriptionResource(ModelResource):
    """A user added description."""
    model = Description

class TokenResource(ModelResource):
    """A user added description."""
    model = Token

class RegularisationTypeResource(ModelResource):
    """A user added description."""
    model = RegularisationType

class ScopeResource(ModelResource):
    """A user added description."""
    model = Scope

class RegularisationResource(ModelResource):
    """A user added description."""
    model = Regularisation


