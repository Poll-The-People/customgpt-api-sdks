from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.create_project_response_500_status import CreateProjectResponse500Status
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_project_response_500_data import CreateProjectResponse500Data


T = TypeVar("T", bound="CreateProjectResponse500")


@attr.s(auto_attribs=True)
class CreateProjectResponse500:
    """
    Attributes:
        status (Union[Unset, CreateProjectResponse500Status]): The status of the response Example: error.
        url (Union[Unset, str]): The URL of the request Example: https://app.customgpt.ai/api/v1/projects/1.
        data (Union[Unset, CreateProjectResponse500Data]):
    """

    status: Union[Unset, CreateProjectResponse500Status] = UNSET
    url: Union[Unset, str] = UNSET
    data: Union[Unset, "CreateProjectResponse500Data"] = UNSET
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
        from ..models.create_project_response_500_data import CreateProjectResponse500Data

        _status = src_dict.get("status")
        status: Union[Unset, CreateProjectResponse500Status]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = CreateProjectResponse500Status(_status)

        url = src_dict.get("url")

        _data = src_dict.get("data")
        data: Union[Unset, CreateProjectResponse500Data]
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = CreateProjectResponse500Data.from_dict(_data)

        create_project_response_500 = cls(
            status=status,
            url=url,
            data=data,
        )

        create_project_response_500.additional_properties = src_dict
        return create_project_response_500

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
