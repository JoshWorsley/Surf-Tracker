from django.shortcuts import render
from rest_framework import viewsets,status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.views import APIView
import pandas as pd

from .models import Session, Surfer
from .serializers import SessionSerializer, SurferSerializer, CreateSurferSerializer,SpotSerializer


class SessionView(viewsets.ViewSet):
    queryset = Session.objects.all()

    def list(self, request):
        serializer = SessionSerializer(self.queryset, many=True)
        return Response(serializer.data)

    @action(
        methods=["get"], detail=False, url_path=r"(?P<Quality>\w+)/all", url_name="all"
    )
    def Wave_Quality(self, request, Quality=None):
        serializer = SessionSerializer(
            self.queryset.filter(Quality__gte=Quality), many=True
        )  # Note the lowercase "surfer"
        return Response(serializer.data)


###The correspondong url is http://127.0.0.1:8000/api/Session/Surfer/Liam/all/
###Returns a list of aqll the sessions had by a surfer
    @action(
        methods=["get"], detail=False, url_path=r"Surfer/(?P<Surfer>\w+)/all", url_name="all"
    )
    def list_spot_by_surfer(self, request, Surfer=None):
        serializer = SessionSerializer(
            self.queryset.filter(Surfer__Name=Surfer), many=True
        )
        serialized_data = serializer.data
        df = pd.DataFrame(serialized_data)
        total_quality = df['rating'].count()
      
        analysis_results = {
        "total_quality": total_quality,}
        serialized_data.append(analysis_results)

        return Response(serialized_data)

    # @action(
    #     methods=["get"],
    #     detail=False,
    #     url_path=r"(?P<Surfer>\w+)/(?P<Quality>\w+)/all",
    #     url_name="all",
    # )
    # def list_spot_by_surfer_and_qality(self, request, Surfer=None, Quality=None):
    #     serializer = SessionSerializer(
    #         self.queryset.filter(Surfer__Name=Surfer, Quality__gte=Quality), many=True
    #     )  
    #     return Response(serializer.data)
    
    ###This is a view to see the spot and see what the best wind is 
    
    @action(
    methods=["get"],
    detail=False,
    url_path=r"Spot/(?P<Spot>\w+)/all",
    url_name="all",
    )
    def filter_by_spot(self, request, Spot=None):
        serializer = SpotSerializer(
            self.queryset.filter(Spot=Spot), many=True
        )  

        serialized_data = serializer.data
        df = pd.DataFrame(serialized_data)
        df['Score'] = [2 if x == "good" else 1 if x == "okay" else -1 for x in df['rating']]
        best_wind = df.groupby("Wind")['Score'].sum()
        best_wind_dict = best_wind.to_dict()
        
      
        serialized_data.append(best_wind_dict)


        return Response(serialized_data)
    



class SurferView(viewsets.ViewSet):
    queryset = Surfer.objects.all()

    def list(self, request):
        serializer = SurferSerializer(self.queryset, many=True)
        return Response(serializer.data)
    


class CreateSurfView(viewsets.ViewSet):
    queryset = Session.objects.all()

    serializer_class = CreateSurferSerializer

    @action(methods=["post"], detail=False,url_path=r"CreateSurfer/all",
        url_name="all",)
    def create_session(self, request):
        serializer = CreateSurferSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
class CreateSurfSessionView(viewsets.ViewSet):
    queryset = Session.objects.all()

    serializer_class = SessionSerializer

    @action(methods=["post"], detail=False,url_path=r"CreateSurfSession/all",
        url_name="all",)
    def create_session(self, request):
        serializer = SessionSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

