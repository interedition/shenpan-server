"""API calls for frontend to use."""

from djangorestframework.views import View
from djangorestframework.response import Response
from djangorestframework import status
from annotatey.api.models import Description, Token,\
    RegularisationType, Scope, Regularisation
from django.core.urlresolvers import reverse

class DecisionRoot(View):
    """
    A decision about a token.
    """
    def get(self, request):
        return {'hello': 'world'}

    def post(self, request):
        print dir(self.user)
        print self.user
        token, created = Token.objects.get_or_create(text = self.CONTENT['token'])
        if self.CONTENT['lemma']:
            lemma, created = Token.objects.get_or_create(text = self.CONTENT['lemma'])
        else:
            lemma = None

        if self.CONTENT['scope']:
            scope = Scope.objects.get(name = self.CONTENT['scope'])
        else:
            scope = None

        if self.CONTENT['regularisation_type']:
            regularisation_type = RegularisationType.objects.get(name = self.CONTENT['regularisation_type'])
        else:
            regularisation_type

        context = self.CONTENT['context']
        external_user = self.CONTENT['external_user']
        system_user = self.user

        regularisation, created = \
            Regularisation.objects.get_or_create(token = token,
                                                 lemma = lemma,
                                                 scope = scope,
                                                 regularisation_type = regularisation_type,
                                                 context = context,
                                                 external_user = external_user,
                                                 system_user = system_user,
                                                 )

        return Response(status.HTTP_201_CREATED, headers={'Location': reverse('regularisation_instance', args=[regularisation.id])}, content = "hello")

#class DecisionInstance(View):
#    pass



