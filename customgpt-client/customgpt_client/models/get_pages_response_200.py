from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.get_pages_response_200_status import GetPagesResponse200Status
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_pages_response_200_data import GetPagesResponse200Data


T = TypeVar("T", bound="GetPagesResponse200")


@attr.s(auto_attribs=True)
class GetPagesResponse200:
    """
    Attributes:
        status (Union[Unset, GetPagesResponse200Status]): The status of the response Example: success.
        data (Union[Unset, GetPagesResponse200Data]):
    """

    status: Union[Unset, GetPagesResponse200Status] = UNSET
    data: Union[Unset, "GetPagesResponse200Data"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        data: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.data, Unset):
            data = self.data.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if status is not UNSET:
            field_dict["status"] = status
        if data is not UNSET:
            field_dict["data"] = data

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.get_pages_response_200_data import GetPagesResponse200Data

        _status = src_dict.get("status")
        status: Union[Unset, GetPagesResponse200Status]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = GetPagesResponse200Status(_status)

        _data = src_dict.get("data")
        data: Union[Unset, GetPagesResponse200Data]
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = GetPagesResponse200Data.from_dict(_data)

        get_pages_response_200 = cls(
            status=status,
            data=data,
        )

        get_pages_response_200.additional_properties = src_dict
        return get_pages_response_200

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
