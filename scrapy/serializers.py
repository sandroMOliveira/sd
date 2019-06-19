from rest_framework import serializers
from . import models

class Conteudo(serializers.ModelSerializer):

    class Meta:
        model = models.Conteudo
        fields = '__all__'

class Pagina(serializers.ModelSerializer):

    class Meta:
        model = models.Pagina
        fields = ('id', 'titulo', 'link')