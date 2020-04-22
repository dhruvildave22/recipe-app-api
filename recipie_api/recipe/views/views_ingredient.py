from recipe.models.models_ingredient import Ingredient
from recipe.serializers.serializers_ingredient import IngredientSerializer
from recipe.views.base_recipe_attributes import BaseRecipeAttrViewSet


class IngredientViewSet(BaseRecipeAttrViewSet):
    """Manage Ingredients in the database"""
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer
