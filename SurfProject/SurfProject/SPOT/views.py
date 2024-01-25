from django.shortcuts import render
from rest_framework import viewsets,status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.views import APIView

from .models import Session, Surfer
from .serializers import SessionSerializer, SurferSerializer, CreateSurferSerializer


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

    @action(
        methods=["get"], detail=False, url_path=r"(?P<Surfer>\w+)/all", url_name="all"
    )
    def list_spot_by_surfer(self, request, Surfer=None):
        serializer = SessionSerializer(
            self.queryset.filter(Surfer__Name=Surfer), many=True
        )  # Note the lowercase "surfer"
        return Response(serializer.data)

    @action(
        methods=["get"],
        detail=False,
        url_path=r"(?P<Surfer>\w+)/(?P<Quality>\w+)/all",
        url_name="all",
    )
    def list_spot_by_surfer(self, request, Surfer=None, Quality=None):
        serializer = SessionSerializer(
            self.queryset.filter(Surfer__Name=Surfer, Quality__gte=Quality), many=True
        )  # Note the lowercase "surfer"
        return Response(serializer.data)


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
