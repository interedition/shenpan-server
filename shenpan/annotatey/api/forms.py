"""Forms for adding decisions."""

from django import forms
from annotatey.api.models import Scope, RegularisationType

SCOPE_CHOICES = [(scope.id, scope.name) for scope in Scope.objects.all()]
DECISION_TYPE_CHOICES = [(decision.id, decision.name) for decision in RegularisationType.objects.all()]

class DecisionForm(forms.Form):
    """Form for submitting decisions."""
    token = forms.CharField(
        max_length = 255,
        help_text = '(The text which is subject to the decision.)')
    lemma = forms.CharField(
        required=False,
        max_length = 255,
        help_text = '(Optional - a base form of the text)')
    context = forms.CharField(
        required=False,
        max_length = 255,
        help_text = '(Optional - a base form of the text)')
    external_user = forms.CharField(
        required=False,
        max_length = 255,
        help_text = '(Optional - a username or id of the decider within an external system.)')
    description = forms.CharField(
        required=False,
        max_length = 10000,
        help_text = '(Optional - a description or jusification of the decision.)')
    scope = forms.ChoiceField(choices=SCOPE_CHOICES)
    decision_type = forms.ChoiceField(choices=DECISION_TYPE_CHOICES)
