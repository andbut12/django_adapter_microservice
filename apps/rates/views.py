import http
import typing as tp

from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets
from rest_framework.request import Request
from rest_framework.response import Response

from . import serializers
from .interfaces import Interface


class RateViewSet(viewsets.GenericViewSet):
    @swagger_auto_schema(
        tags=["rate"],
        request_body=serializers.RateCreateRequestSerializer,
        responses={201: serializers.RateCreateResponseSerializer()},
    )
    def create(self, request: Request, *_args: tp.Any, **_kwargs: tp.Any) -> Response:
        req_serializer = serializers.RateCreateRequestSerializer(data=request.data)
        if not req_serializer.is_valid(raise_exception=True):
            return Response(status=http.HTTPStatus.UNPROCESSABLE_ENTITY)

        headers = {"X-Token": f"Token {request.token}"} if request.token else None
        resp_serializer = serializers.RateCreateResponseSerializer(
            data=Interface.create_rate(**req_serializer.data, headers=headers)
        )
        if not resp_serializer.is_valid(raise_exception=True):
            return Response(status=http.HTTPStatus.INTERNAL_SERVER_ERROR)
        return Response(resp_serializer.data, status=http.HTTPStatus.CREATED)

    @swagger_auto_schema(
        tags=["rate"],
        query_serializer=serializers.RateRetrieveRequestSerializer(),
        responses={200: serializers.RateRetrieveResponseSerializer()}
    )
    def retrieve(self, request: Request, pk=None):
        if not pk:
            return Response(status=http.HTTPStatus.UNPROCESSABLE_ENTITY)

        req_serializer = serializers.RateRetrieveRequestSerializer(data=request.GET)
        if not req_serializer.is_valid(raise_exception=True):
            return Response(status=http.HTTPStatus.UNPROCESSABLE_ENTITY)

        headers = {"X-Token": f"Token {request.token}"} if request.token else None
        resp_serializer = serializers.RateRetrieveResponseSerializer(
            data=Interface.get_rate(key=pk, headers=headers, **req_serializer.data)
        )
        if not resp_serializer.is_valid(raise_exception=True):
            return Response(status=http.HTTPStatus.INTERNAL_SERVER_ERROR)

        return Response(resp_serializer.data)

    def get_queryset(self):
        ...

    def get_serializer_class(self):
        ...
