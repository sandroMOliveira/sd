from rest_framework import views, generics
from . import serializers, models, filters, pagination
from django_filters.rest_framework import DjangoFilterBackend

class ListPagesAndConteudo(generics.ListAPIView):
    queryset = models.Pagina.objects.select_related('conteudo').all()
    serializer_class = serializers.Pagina
    filter_backends = [DjangoFilterBackend, filters.ConteudoFilter, ]
    filterset_fields = ('conteudo', )
    pagination_class = pagination.ScrapyPagination