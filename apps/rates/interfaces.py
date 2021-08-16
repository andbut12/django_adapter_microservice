import typing as tp

from apps.rates.models import RateRequest
from example_eshop.interfaces import BaseInterface


class Interface(BaseInterface):
    @classmethod
    def create_rate(
            cls,
            headers: tp.Dict[str, tp.Any],
            *_args: tp.Any,
            **kwargs: tp.Any
    ) -> tp.List[tp.Dict[str, tp.Any]]:
        _path = "rates/create/"

        RateRequest.objects.create(
            sender_contact_id=kwargs.get("sender_contact_id"),
            receiver_contact_id=kwargs.get("receiver_contact_id"),
            cargoes=', '.join(str(x) for x in kwargs["cargoes"]) if kwargs.get("cargoes") else None,
        )

        return cls._post(path=_path, data=kwargs, headers=headers)

    @classmethod
    def get_rate(
            cls,
            key: str,
            headers: tp.Dict[str, tp.Any],
            shipping_type_filter: str = "d2d",
            *_args: tp.Any,
            **kwargs: tp.Any
    ) -> tp.List[tp.Dict[str, tp.Any]]:
        _path = f"rates/result/{key}/list"

        data = cls._get(path=_path, data=kwargs, headers=headers)
        results = [x for x in data.get("results") if x.get("shipping_type") == shipping_type_filter]
        data.update({
            "count": len(results),
            "results": results,
        })

        return data
