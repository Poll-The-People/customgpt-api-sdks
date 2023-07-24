from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.get_user_profile_response_500_data_code import GetUserProfileResponse500DataCode
from ..types import UNSET, Unset

T = TypeVar("T", bound="GetUserProfileResponse500Data")


@attr.s(auto_attribs=True)
class GetUserProfileResponse500Data:
    """
    Attributes:
        code (Union[Unset, GetUserProfileResponse500DataCode]): The error status code Example: 500.
        message (Union[Unset, str]):  Example: Internal Server Error.
    """

    code: Union[Unset, GetUserProfileResponse500DataCode] = UNSET
    message: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        code: Union[Unset, int] = UNSET
        if not isinstance(self.code, Unset):
            code = self.code.value

        message = self.message

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
        _code = src_dict.get("code")
        code: Union[Unset, GetUserProfileResponse500DataCode]
        if isinstance(_code, Unset):
            code = UNSET
        else:
            code = GetUserProfileResponse500DataCode(_code)

        message = src_dict.get("message")

        get_user_profile_response_500_data = cls(
            code=code,
            message=message,
        )

        get_user_profile_response_500_data.additional_properties = src_dict
        return get_user_profile_response_500_data

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