import io

import json
from rest_framework import serializers
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

from tour.models import Tour


# class TourModel:
#     def __init__(self,title,content):
#         self.title = title
#         self.content = content
class TourSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Tour
        fields = "__all__"







# def encode():
#     model = TourModel('Burabay', 'Content: Burabay')
#     model_sr = TourSerializer(model)
#     print(model_sr.data,type(model_sr.data), sep='\n')
#     json = JSONRenderer().render(model_sr.data)
#     print(json)
#
# def decode():
#     stream = io.BytesIO(b'{"title":"Burabay","content":"Content: Burabay"}')
#     data = JSONParser().parse(stream)
#     serializer = TourSerializer(data=data)
#     serializer.is_valid()
#     print(serializer.validated_data)

