import http
import typing as tp

from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets
from rest_framework.request import Request
from rest_framework.response import Response

from . import serializers
from .interfaces import Interface


class ShipmentViewSet(viewsets.GenericViewSet):
    @swagger_auto_schema(
        tags=["shipment"],
        request_body=serializers.ShipmentCreateRequestSerializer,
        responses={201: serializers.ShipmentCreateResponseSerializer()},
    )
    def create(self, request: Request, *_args: tp.Any, **_kwargs: tp.Any) -> Response:
        req_serializer = serializers.ShipmentCreateRequestSerializer(data=request.data)
        if not req_serializer.is_valid(raise_exception=True):
            return Response(status=http.HTTPStatus.UNPROCESSABLE_ENTITY)

        headers = {"X-Token": f"Token {request.token}"} if request.token else None
        resp_serializer = serializers.ShipmentCreateResponseSerializer(
            data=Interface.create_shipment(**req_serializer.data, headers=headers)
        )
        if not resp_serializer.is_valid(raise_exception=True):
            return Response(status=http.HTTPStatus.INTERNAL_SERVER_ERROR)
        return Response(resp_serializer.data, status=http.HTTPStatus.CREATED)

    def get_queryset(self):
        ...

    def get_serializer_class(self):
        ...
