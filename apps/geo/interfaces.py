import typing as tp

from example_eshop.interfaces import BaseInterface


class Interface(BaseInterface):
    @classmethod
    def get_cities(
            cls,
            headers: tp.Dict[str, tp.Any],
            *_args: tp.Any,
            **kwargs: tp.Any
    ) -> tp.List[tp.Dict[str, tp.Any]]:
        _path = "geo/locality/search/"
        return cls._get(path=_path, data=kwargs, headers=headers)
