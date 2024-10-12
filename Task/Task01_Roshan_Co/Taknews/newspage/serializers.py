from rest_framework import serializers
from .models import News_Table

class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News_Table
        fields = ["id", "News_Title", "News_Content", "News_Tags", "News_Source"]