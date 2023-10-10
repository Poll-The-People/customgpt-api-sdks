from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_source_response_401_data import CreateSourceResponse401Data


T = TypeVar("T", bound="CreateSourceResponse401")


@attr.s(auto_attribs=True)
class CreateSourceResponse401:
    """
    Attributes:
        status (Union[Unset, CreateSourceResponse401Status]): The status of the response Example: error.
        url (Union[Unset, str]): The URL of the request Example: https://app.customgpt.ai/api/v1/projects/1.
        data (Union[Unset, CreateSourceResponse401Data]):
    """

    status: Union[Unset, str] = Unset
    url: Union[Unset, str] = UNSET
    data: Union[Unset, "CreateSourceResponse401Data"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        url = self.url
        data: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.data, Unset):
            data = self.data.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if status is not UNSET:
            field_dict["status"] = status
        if url is not UNSET:
            field_dict["url"] = url
        if data is not UNSET:
            field_dict["data"] = data

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.create_source_response_401_data import CreateSourceResponse401Data

        status = src_dict.get("status")

        url = src_dict.get("url")

        _data = src_dict.get("data")
        data: Union[Unset, CreateSourceResponse401Data]
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = CreateSourceResponse401Data.from_dict(_data)

        create_source_response_401 = cls(
            status=status,
            url=url,
            data=data,
        )

        create_source_response_401.additional_properties = src_dict
        return create_source_response_401

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
