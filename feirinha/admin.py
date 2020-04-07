from django.contrib import admin

# Register your models here.
from .models import Feirante, Unidade, Produto

admin.site.register(Feirante)
admin.site.register(Unidade)
admin.site.register(Produto)