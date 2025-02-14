from django.db.models import Prefetch
from rest_framework.generics import ListAPIView
from rest_framework.response import Response

from .models import Food, FoodCategory
from .serializers import FoodListSerializer


class FoodCategoryListView(ListAPIView):
    serializer_class = FoodListSerializer

    def get_queryset(self):
        published_foods = Food.objects.filter(is_publish=True)
        return (
            FoodCategory.objects.prefetch_related(
                Prefetch("food", queryset=published_foods)
            )
            .filter(food__isnull=False)
            .distinct()
        )

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
