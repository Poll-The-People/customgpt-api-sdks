from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.update_project_settings_response_500_status import UpdateProjectSettingsResponse500Status
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.update_project_settings_response_500_data import UpdateProjectSettingsResponse500Data


T = TypeVar("T", bound="UpdateProjectSettingsResponse500")


@attr.s(auto_attribs=True)
class UpdateProjectSettingsResponse500:
    """
    Attributes:
        status (Union[Unset, UpdateProjectSettingsResponse500Status]): The status of the response Example: error.
        url (Union[Unset, str]): The URL of the request Example: https://app.customgpt.ai/api/v1/projects/1.
        data (Union[Unset, UpdateProjectSettingsResponse500Data]):
    """

    status: Union[Unset, UpdateProjectSettingsResponse500Status] = UNSET
    url: Union[Unset, str] = UNSET
    data: Union[Unset, "UpdateProjectSettingsResponse500Data"] = UNSET
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
        from ..models.update_project_settings_response_500_data import UpdateProjectSettingsResponse500Data

        d = src_dict.copy()
        _status = d.pop("status", UNSET)
        status: Union[Unset, UpdateProjectSettingsResponse500Status]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = UpdateProjectSettingsResponse500Status(_status)

        url = d.pop("url", UNSET)

        _data = d.pop("data", UNSET)
        data: Union[Unset, UpdateProjectSettingsResponse500Data]
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = UpdateProjectSettingsResponse500Data.from_dict(_data)

        update_project_settings_response_500 = cls(
            status=status,
            url=url,
            data=data,
        )

        update_project_settings_response_500.additional_properties = d
        return update_project_settings_response_500

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