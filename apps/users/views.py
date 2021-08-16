import http
import typing as tp

from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets
from rest_framework.request import Request
from rest_framework.response import Response

from . import serializers
from .interfaces import Interface


class ContactViewSet(viewsets.GenericViewSet):
    @swagger_auto_schema(
        tags=["contact"],
        request_body=serializers.ContactCreateRequestSerializer,
        responses={201: serializers.ContactCreateResponseSerializer()},
    )
    def create(self, request: Request, *_args: tp.Any, **_kwargs: tp.Any) -> Response:
        req_serializer = serializers.ContactCreateRequestSerializer(data=request.data)
        if not req_serializer.is_valid(raise_exception=True):
            return Response(status=http.HTTPStatus.UNPROCESSABLE_ENTITY)

        headers = {"X-Token": f"Token {request.token}"} if request.token else None
        resp_serializer = serializers.ContactCreateResponseSerializer(
            data=Interface.create_contact(**req_serializer.data, headers=headers)
        )
        if not resp_serializer.is_valid(raise_exception=True):
            return Response(status=http.HTTPStatus.INTERNAL_SERVER_ERROR)
        return Response(resp_serializer.data, status=http.HTTPStatus.CREATED)

    @swagger_auto_schema(
        tags=["contact"],
        request_body=serializers.ContactUpdateRequestSerializer,
        responses={200: serializers.ContactUpdateResponseSerializer()}
    )
    def update(self, request: Request, pk=None):
        if not pk:
            return Response(status=http.HTTPStatus.UNPROCESSABLE_ENTITY)
        req_serializer = serializers.ContactUpdateRequestSerializer(data=request.data)
        if not req_serializer.is_valid(raise_exception=True):
            return Response(status=http.HTTPStatus.UNPROCESSABLE_ENTITY)

        headers = {"X-Token": f"Token {request.token}"} if request.token else None
        resp_serializer = serializers.ContactUpdateResponseSerializer(
            data=Interface.edit_contact(**req_serializer.data, key=pk, headers=headers)
        )
        if not resp_serializer.is_valid(raise_exception=True):
            return Response(status=http.HTTPStatus.INTERNAL_SERVER_ERROR)

        return Response(resp_serializer.data)

    def get_queryset(self) -> None:
        ...

    def get_serializer_class(self) -> None:
        ...
