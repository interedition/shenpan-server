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
    def get(self, request, query = None):
        if not query:
            return {"detail": "Provide a token in the URL. E.g. http://www.annotation.bham.ac.uk/api/query/cat/"}

        query_token = Token.objects.get(text = query)
        token_list = query_token.tokens.values_list('token__text', flat = True)
        lemma_list = query_token.lemmas.values_list('lemma__text', flat = True)

        return {'query': query,
                'tokens': token_list,
                'lemmas': lemma_list}

class DumpRoot(View):
    """
    Outputs all the rules.
    """
    def get(self, request):
        return [{
            'token': reg.token.text,
            'lemma': reg.lemma.text,
            'regularisation_type': reg.regularisation_type.name,
            'scope': reg.scope.name,
            'context': reg.context,
            'external_user': reg.external_user,
            'system_user': reg.system_user.username,
        } for reg in Regularisation.objects.all()]

class ApplyRoot(View):
    """
    Apply decision on given witness json input
    """

    def post(self, request):
        if 'witnesses' not in self.CONTENT:
            return Response(status.HTTP_200_OK)
        witnesses = self.CONTENT['witnesses']
        context = self.CONTENT.get('context')

        for witness in witnesses:
            for token_dict in witness['tokens']:
                token_dict['t'] = Regularisation.regularise(
                        token_dict['t'], context)
        return witness

class DecisionRoot(View):
    """
    A decision about a token.
    """
    def get(self, request):
        return {
            '/': ['http://www.annotation.bham.ac.uk/api/', 'Add a new rule (POST)'],
            'scopes': ['http://www.annotation.bham.ac.uk/api/scope/', 'How far the decision applies'],
            'regularisationtype': ['http://www.annotation.bham.ac.uk/api/regularisationtype/', 'The type of decision'],
            'query': ['http://www.annotation.bham.ac.uk/api/query/', 'Gives all the relations for a term',],
            'dump': ['http://www.annotation.bham.ac.uk/api/dump/', 'Output all the decisions'],
            'apply': ['http://www.annotation.bham.ac.uk/api/apply/', 'Apply the decisions to the given input (POST)'],
                }

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

        if 'description' in self.CONTENT:
            description = self.CONTENT['description']
            reg_contenttype = ContentType.objects.get(app_label="api", model="regularisation")
            regularisation_desc = Description(text = description,
                                              external_user = external_user,
                                              content_type = reg_contenttype,
                                              object_id = regularisation.id)
            regularisation_desc.save()

        return Response(status.HTTP_201_CREATED, headers={'Location': reverse('regularisation_instance', args=[regularisation.id])}, content = "hello")

#class DecisionInstance(View):
#    pass



