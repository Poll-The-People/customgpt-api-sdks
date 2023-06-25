from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.update_project_settings_response_400_data_code import UpdateProjectSettingsResponse400DataCode
from ..models.update_project_settings_response_400_data_message import UpdateProjectSettingsResponse400DataMessage
from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateProjectSettingsResponse400Data")


@attr.s(auto_attribs=True)
class UpdateProjectSettingsResponse400Data:
    """
    Attributes:
        code (Union[Unset, UpdateProjectSettingsResponse400DataCode]): The error status code Example: 400.
        message (Union[Unset, UpdateProjectSettingsResponse400DataMessage]): The error message Example: Please upload a
            valid image file for avatar.
    """

    code: Union[Unset, UpdateProjectSettingsResponse400DataCode] = UNSET
    message: Union[Unset, UpdateProjectSettingsResponse400DataMessage] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        code: Union[Unset, int] = UNSET
        if not isinstance(self.code, Unset):
            code = self.code.value

        message: Union[Unset, str] = UNSET
        if not isinstance(self.message, Unset):
            message = self.message.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if code is not UNSET:
            field_dict["code"] = code
        if message is not UNSET:
            field_dict["message"] = message

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _code = d.pop("code", UNSET)
        code: Union[Unset, UpdateProjectSettingsResponse400DataCode]
        if isinstance(_code, Unset):
            code = UNSET
        else:
            code = UpdateProjectSettingsResponse400DataCode(_code)

        _message = d.pop("message", UNSET)
        message: Union[Unset, UpdateProjectSettingsResponse400DataMessage]
        if isinstance(_message, Unset):
            message = UNSET
        else:
            message = UpdateProjectSettingsResponse400DataMessage(_message)

        update_project_settings_response_400_data = cls(
            code=code,
            message=message,
        )

        update_project_settings_response_400_data.additional_properties = d
        return update_project_settings_response_400_data

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
