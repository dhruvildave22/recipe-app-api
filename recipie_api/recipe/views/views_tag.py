from recipe.models.models_tag import Tag
from recipe.serializers.serializers_tag import TagSerializer
from recipe.views.base_recipe_attributes import BaseRecipeAttrViewSet


class TagViewSet(BaseRecipeAttrViewSet):
    """Manage tags in the database"""
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
