from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.list_projects_response_200_status import ListProjectsResponse200Status
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.list_projects_response_200_data import ListProjectsResponse200Data


T = TypeVar("T", bound="ListProjectsResponse200")


@attr.s(auto_attribs=True)
class ListProjectsResponse200:
    """
    Attributes:
        status (Union[Unset, ListProjectsResponse200Status]): The status of the response Example: success.
        data (Union[Unset, ListProjectsResponse200Data]):
    """

    status: Union[Unset, ListProjectsResponse200Status] = UNSET
    data: Union[Unset, "ListProjectsResponse200Data"] = UNSET
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
        from ..models.list_projects_response_200_data import ListProjectsResponse200Data

        _status = src_dict.get("status")
        status: Union[Unset, ListProjectsResponse200Status]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = ListProjectsResponse200Status(_status)

        _data = src_dict.get("data")
        data: Union[Unset, ListProjectsResponse200Data]
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = ListProjectsResponse200Data.from_dict(_data)

        list_projects_response_200 = cls(
            status=status,
            data=data,
        )

        list_projects_response_200.additional_properties = src_dict
        return list_projects_response_200

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
