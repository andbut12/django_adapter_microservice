import http
import typing as tp

from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets
from rest_framework.request import Request
from rest_framework.response import Response

from . import serializers
from .interfaces import Interface


class GeoViewSet(viewsets.GenericViewSet):
    @swagger_auto_schema(
        tags=["geo"],
        query_serializer=serializers.SearchGeoRequestSerializer,
        responses={200: serializers.SearchGeoResponseSerializer()},
    )
    def list(self, request: Request, *_args: tp.Any, **_kwargs: tp.Any) -> Response:
        req_serializer = serializers.SearchGeoRequestSerializer(data=request.query_params)
        if not req_serializer.is_valid(raise_exception=True):
            return Response(status=http.HTTPStatus.UNPROCESSABLE_ENTITY)

        headers = {"X-Token": f"Token {request.token}"} if request.token else None
        resp_serializer = serializers.SearchGeoResponseSerializer(
            data=Interface.get_cities(**req_serializer.data, headers=headers),
            many=True
        )
        if not resp_serializer.is_valid(raise_exception=True):
            return Response(status=http.HTTPStatus.INTERNAL_SERVER_ERROR)

        return Response(resp_serializer.data)

    def get_queryset(self) -> None:
        ...

    def get_serializer_class(self) -> None:
        ...
