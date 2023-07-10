from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.list_project_sources_response_401_status import ListProjectSourcesResponse401Status
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.list_project_sources_response_401_data import ListProjectSourcesResponse401Data


T = TypeVar("T", bound="ListProjectSourcesResponse401")


@attr.s(auto_attribs=True)
class ListProjectSourcesResponse401:
    """
    Attributes:
        status (Union[Unset, ListProjectSourcesResponse401Status]): The status of the response Example: error.
        url (Union[Unset, str]): The URL of the request Example: https://app.customgpt.ai/api/v1/projects/1.
        data (Union[Unset, ListProjectSourcesResponse401Data]):
    """

    status: Union[Unset, ListProjectSourcesResponse401Status] = UNSET
    url: Union[Unset, str] = UNSET
    data: Union[Unset, "ListProjectSourcesResponse401Data"] = UNSET
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
        from ..models.list_project_sources_response_401_data import ListProjectSourcesResponse401Data

        _status = src_dict.get("status")
        status: Union[Unset, ListProjectSourcesResponse401Status]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = ListProjectSourcesResponse401Status(_status)

        url = src_dict.get("url")

        _data = src_dict.get("data")
        data: Union[Unset, ListProjectSourcesResponse401Data]
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = ListProjectSourcesResponse401Data.from_dict(_data)

        list_project_sources_response_401 = cls(
            status=status,
            url=url,
            data=data,
        )

        list_project_sources_response_401.additional_properties = src_dict
        return list_project_sources_response_401

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
