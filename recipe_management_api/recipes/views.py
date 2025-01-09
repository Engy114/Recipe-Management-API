# recipes/views.py
from rest_framework import viewsets, permissions
from rest_framework.pagination import PageNumberPagination
from .models import Recipe
from .serializers import RecipeSerializer
from rest_framework import filters
from django.http import JsonResponse
from django.views import View

class RecipePagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 20

class RecipeViewSet(viewsets.ModelViewSet):
    serializer_class = RecipeSerializer
    queryset = Recipe.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    pagination_class = RecipePagination
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title', 'category', 'ingredients']
    ordering_fields = ['preparation_time', 'cooking_time', 'servings']

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class RecipeListView(View):
    def get(self, request):
        recipes = list(Recipe.objects.values())
        return JsonResponse({"recipes": recipes})
