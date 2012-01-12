"""Admin configuration for regula."""
from django.contrib import admin
from regula.backend.models import Description, Token,\
    RegularisationType, Scope, Regularisation

admin.site.register(Description)
admin.site.register(Token)
admin.site.register(RegularisationType)
admin.site.register(Scope)
admin.site.register(Regularisation)
