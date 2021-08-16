import typing as tp

from example_eshop.interfaces import BaseInterface


class Interface(BaseInterface):
    @classmethod
    def create_shipment(
            cls,
            headers: tp.Dict[str, tp.Any],
            *_args: tp.Any,
            **kwargs: tp.Any
    ) -> tp.List[tp.Dict[str, tp.Any]]:
        _path = "shipping/create/"
        return cls._post(path=_path, data=kwargs, headers=headers)
