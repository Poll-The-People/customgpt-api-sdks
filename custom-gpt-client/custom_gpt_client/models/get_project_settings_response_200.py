from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.get_project_settings_response_200_status import GetProjectSettingsResponse200Status
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_project_settings_response_200_data import GetProjectSettingsResponse200Data


T = TypeVar("T", bound="GetProjectSettingsResponse200")


@attr.s(auto_attribs=True)
class GetProjectSettingsResponse200:
    """
    Attributes:
        status (Union[Unset, GetProjectSettingsResponse200Status]): The status of the response Example: success.
        data (Union[Unset, GetProjectSettingsResponse200Data]):
    """

    status: Union[Unset, GetProjectSettingsResponse200Status] = UNSET
    data: Union[Unset, "GetProjectSettingsResponse200Data"] = UNSET
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
        from ..models.get_project_settings_response_200_data import GetProjectSettingsResponse200Data

        d = src_dict.copy()
        _status = d.pop("status", UNSET)
        status: Union[Unset, GetProjectSettingsResponse200Status]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = GetProjectSettingsResponse200Status(_status)

        _data = d.pop("data", UNSET)
        data: Union[Unset, GetProjectSettingsResponse200Data]
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = GetProjectSettingsResponse200Data.from_dict(_data)

        get_project_settings_response_200 = cls(
            status=status,
            data=data,
        )

        get_project_settings_response_200.additional_properties = d
        return get_project_settings_response_200

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
