import typing as tp

from example_eshop.interfaces import BaseInterface


class Interface(BaseInterface):
    @classmethod
    def create_contact(
            cls,
            headers: tp.Dict[str, tp.Any],
            *_args: tp.Any,
            **kwargs: tp.Any
    ) -> tp.List[tp.Dict[str, tp.Any]]:
        _path = "users/contact/create/"
        return cls._post(path=_path, data=kwargs, headers=headers)

    @classmethod
    def edit_contact(
            cls,
            key: str,
            headers: tp.Dict[str, tp.Any],
            *_args: tp.Any,
            **kwargs: tp.Any
    ) -> tp.List[tp.Dict[str, tp.Any]]:
        _path = f"users/contact/update/{key}/"
        return cls._put(path=_path, data=kwargs, headers=headers)
