import typing as tp

from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.request import Request
from rest_framework.response import Response

from . import serializers


class SignInViewSet(viewsets.GenericViewSet):
    @swagger_auto_schema(
        methods=["POST"],
        tags=["authentication"],
        request_body=serializers.SignInRequestSerializer,
        responses={200: serializers.SignInResponseSerializer()},
    )
    @action(methods=("POST",), detail=False, url_path="sign-in")
    def sign_in(self, request: Request, *_args: tp.Any, **_kwargs: tp.Any):
        return Response(
            serializers.SignInResponseSerializer(
                {'id': 129364, 'token': '4317833d5a1003b58f54a077b68fd79d9b625df3'}
            ).data
        )

    def get_queryset(self):
        ...

    def get_serializer_class(self):
        ...
