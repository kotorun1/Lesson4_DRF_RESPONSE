from rest_framework.serializers import ModelSerializer
from .models import Workers, Orders, JobTitles


class WorkersSerializer(ModelSerializer):
    class Meta:
        model = Workers
        fields = '__all__'

class OrdersSerializer(ModelSerializer):
    class Meta:
        model = Orders
        fields = '__all__'

class JobTitlesSerializer(ModelSerializer):
    class Meta:
        model = JobTitles
        fields = '__all__'

