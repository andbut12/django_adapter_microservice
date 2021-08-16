import typing as tp
from json import JSONDecodeError

import requests
from django.conf import settings
from rest_framework.exceptions import ValidationError


class BaseInterface:
    base_url: str = settings.INTERFACE_BASE_URL

    @classmethod
    def __build_url(cls, path: str = "") -> str:
        return f"{cls.base_url}/{path}"

    @classmethod
    def _post(cls, data: tp.Any, path: str = "", headers: tp.Dict[str, tp.Any] = None) -> tp.Any:
        req = requests.post(url=cls.__build_url(path=path), data=data, headers=headers)

        try:
            data = req.json()
        except (JSONDecodeError, ValueError):
            data = req.text

        if not req.ok:
            raise ValidationError(data)

        return data

    @classmethod
    def _put(cls, data: tp.Any, path: str = "", headers: tp.Dict[str, tp.Any] = None) -> tp.Any:
        req = requests.put(url=cls.__build_url(path=path), data=data, headers=headers)
        try:
            data = req.json()
        except (JSONDecodeError, ValueError):
            data = req.text

        if not req.ok:
            raise ValidationError(data)

        return data

    @classmethod
    def _get(cls, data: tp.Any, path: str = "", headers: tp.Dict[str, tp.Any] = None) -> tp.Any:
        req = requests.get(url=cls.__build_url(path=path), params=data, headers=headers)
        try:
            data = req.json()
        except (JSONDecodeError, ValueError):
            data = req.text

        if not req.ok:
            raise ValidationError(data)

        return data
