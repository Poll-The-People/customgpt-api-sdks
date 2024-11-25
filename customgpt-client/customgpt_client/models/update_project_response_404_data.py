from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateProjectResponse404Data")


@attr.s(auto_attribs=True)
class UpdateProjectResponse404Data:
    """
    Attributes:
        code (Union[Unset, UpdateProjectResponse404DataCode]): The error status code Example: 404.
        message (Union[Unset, UpdateProjectResponse404DataMessage]): The error message Example: Project with id 1 not
            found.
    """

    code: Union[Unset, str] = UNSET
    message: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        code: Union[Unset, int] = UNSET
        if not isinstance(self.code, Unset):
            code = self.code

        message: Union[Unset, str] = UNSET
        if not isinstance(self.message, Unset):
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
        code = src_dict.get("code")

        message = src_dict.get("message")

        update_project_response_404_data = cls(
            code=code,
            message=message,
        )

        update_project_response_404_data.additional_properties = src_dict
        return update_project_response_404_data

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
