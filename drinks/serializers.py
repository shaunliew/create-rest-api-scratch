# serializers is used to convert the data into json format
from rest_framework import serializers
from .models import Drink
# meta is used to define the model and fields
class DrinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Drink
        fields = ['id', 'name', 'description']