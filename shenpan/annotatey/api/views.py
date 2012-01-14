"""API calls for frontend to use."""

from djangorestframework.views import View
from djangorestframework.response import Response
from djangorestframework import status
from annotatey.api.models import Description, Token,\
    RegularisationType, Scope, Regularisation
from django.core.urlresolvers import reverse
from django.contrib.contenttypes.models import ContentType

class QueryRoot(View):
    """
    List of related tokens to a token.
    """
    def get(self, request, query):
        query_token = Token.objects.get(text = query)
        token_list = query_token.tokens.values_list('token__text', flat = True)
        lemma_list = query_token.lemmas.values_list('lemma__text', flat = True)

        return {'query': query,
                'tokens': token_list,
                'lemmas': lemma_list}


class DecisionRoot(View):
    """
    A decision about a token.
    """
    def get(self, request):
        return {'scopes': 'http://www.annotation.bham.ac.uk/api/scope/',
                'regularisationtype': 'http://www.annotation.bham.ac.uk/api/regularisationtype/'}

    def post(self, request):
        token, created = Token.objects.get_or_create(text = self.CONTENT['token'])
        if 'lemma' in self.CONTENT:
            lemma, created = Token.objects.get_or_create(text = self.CONTENT['lemma'])
        else:
            lemma = None

        if 'scope' in self.CONTENT:
            scope = Scope.objects.get(name = self.CONTENT['scope'])
        else:
            scope = None

        if 'regularisation_type' in self.CONTENT:
            regularisation_type = RegularisationType.objects.get(name = self.CONTENT['regularisation_type'])
        else:
            regularisation_type

        context = self.CONTENT['context']
        external_user = self.CONTENT['external_user']
        if 'description' in self.CONTENT:
            description = self.CONTENT['description']

        regularisation, created = \
            Regularisation.objects.get_or_create(token = token,
                                                 lemma = lemma,
                                                 scope = scope,
                                                 regularisation_type = regularisation_type,
                                                 context = context,
                                                 external_user = external_user,
                                                 )

        if 'description' in self.CONTENT:
            reg_contenttype = ContentType.objects.get(app_label="api", model="regularisation")
            regularisation_desc = Description(text = description,
                                              external_user = external_user,
                                              content_type = reg_contenttype,
                                              object_id = regularisation.id)
            regularisation_desc.save()

        return Response(status.HTTP_201_CREATED, headers={'Location': reverse('regularisation_instance', args=[regularisation.id])}, content = "hello")

#class DecisionInstance(View):
#    pass



