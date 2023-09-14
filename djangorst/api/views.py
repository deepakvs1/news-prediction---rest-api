# import myapp.model_creation
from api.model_creation import model_load

# Create your views here.
from django.shortcuts import render
from django.http import JsonResponse
from django.http.response import HttpResponse
from django.template import loader    #user defined  for define "template" folder
from rest_framework import status

from rest_framework.views import APIView
from rest_framework.response import Response
from .models import TextData
from .serializers import TextDataSerializer
import pickle
# from pyspark import SparkContext, SparkConf
# from pyspark.sql import SparkSession



def index(request):   #with data .. display html page
    it= "                                                    ...."
    # it= "Unleashing the Power of AI: Your Futuristic News Content Predictor"
    return render(request, 'index.html') 



class TextDataView(APIView):
    def get(self, request, format=None):
        text_data = TextData.objects.last()
        serializer = TextDataSerializer(text_data)
        return Response(serializer.data)
    #     # pass

    def post(self, request, format=None):
        serializer = TextDataSerializer(data=request.data)
        if serializer.is_valid():
            # print("test 1")
            serializer.save()
            text_data = serializer.data['text']
            model_filepath = 'C:\\Users\\user\\Desktop\\restapi\\REstapinew\\logisticmodel.pkl'
            vectorizer_filepath='C:\\Users\\user\\Desktop\\restapi\\REstapinew\\logisticvectorizer.pkl'
            
            output_json=model_load(model_filepath,vectorizer_filepath,text_data)


            print(output_json)
  
            return render(request, 'index.html',{'textdata':text_data,'result': output_json}) #its render the page in webpage
        # print("test2")
        
        return Response(serializer.errors)
    
        
            
