from rest_framework import generics
from .models import News_Table
from .serializers import NewsSerializer
from django.db.models import Q

class News_View(generics.ListCreateAPIView):
    serializer_class = NewsSerializer

    def get_queryset(self):
        queryset = News_Table.objects.all()
        Tags_Data = self.request.query_params.get('News_Tags')
        Keywords = self.request.query_params.get('keywords')
        Nonexist_Keywords = self.request.query_params.get('nonexist')
        
        if Tags_Data:
            queryset = queryset.filter(News_Tags__icontains=Tags_Data)
        
        if Keywords:
            Keywords_List = Keywords.split(',')
            for Keywords in Keywords_List:
                queryset = queryset.filter(
                    Q(News_Content__icontains=Keywords) |
                    Q(News_Title__icontains=Keywords)
                    )
        
        if Nonexist_Keywords:
            Nonexist_Keywords_List = Nonexist_Keywords.split(',')
            for Nonexist_Keywords in Nonexist_Keywords_List:    
                queryset = queryset.exclude(
                    Q(News_Content__icontains=Nonexist_Keywords) |
                    Q(News_Title__icontains=Nonexist_Keywords)
                )

        return queryset

#---------------------------------------------------------------------------------------------

# from rest_framework import generics
# from .models import News_Table
# from .serializers import NewsSerializer
# from django.db.models import Q

# class News_View(generics.ListCreateAPIView):
#     serializer_class = NewsSerializer

#     def get_queryset(self):
#         queryset = News_Table.objects.all()
#         Tags_Data = self.request.query_params.get('News_Tags')
#         Keywords = self.request.query_params.get('News_Content')

#         if Tags_Data:
#             queryset = queryset.filter(News_Tags__icontains=Tags_Data)
        
#         if Keywords:
#             Keywords_List = Keywords.split(',')
#             for Keywords in Keywords_List:
#                 queryset = queryset.filter(
#                     Q(News_Content__icontains=Keywords) |
#                     Q(News_Title__icontains=Keywords)
#                     )
        
#         return queryset

#---------------------------------------------------------------------------------------------

# from rest_framework import generics
# from .models import News_Table
# from .serializers import NewsSerializer

# class News_View(generics.ListCreateAPIView):
#     serializer_class = NewsSerializer

#     def get_queryset(self):
#         queryset = News_Table.objects.all()
#         Tags_Data = self.request.query_params.get('News_Tags')
#         if Tags_Data:
#             queryset = queryset.filter(News_Tags__icontains=Tags_Data)
#         return queryset

#---------------------------------------------------------------------------------------------

# from rest_framework import generics
# from .models import News_Table
# from .serializers import NewsSerializer

# class News_View(generics.ListCreateAPIView):    
#     queryset = News_Table.objects.all()
#     serializer_class = NewsSerializer

#---------------------------------------------------------------------------------------------

# from django.shortcuts import render
# from django.http import HttpResponse
# from django.template import loader
# from .models import News_Table

# def News_View(request):
#     News_Data = News_Table.objects.all().values()
#     Templates_News = loader.get_template("NewsText.html")
#     context = {
#         'News_Data': News_Data,
#     }
#     return HttpResponse(Templates_News.render(context ,request))

