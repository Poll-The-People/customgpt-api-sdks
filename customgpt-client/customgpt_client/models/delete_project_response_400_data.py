from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.delete_project_response_400_data_code import DeleteProjectResponse400DataCode
from ..types import UNSET, Unset

T = TypeVar("T", bound="DeleteProjectResponse400Data")


@attr.s(auto_attribs=True)
class DeleteProjectResponse400Data:
    """
    Attributes:
        code (Union[Unset, DeleteProjectResponse400DataCode]): The error status code Example: 400.
        message (Union[Unset, str]): The error message Example: Project id must be integer.
    """

    code: Union[Unset, DeleteProjectResponse400DataCode] = UNSET
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
        code: Union[Unset, DeleteProjectResponse400DataCode]
        if isinstance(_code, Unset):
            code = UNSET
        else:
            code = DeleteProjectResponse400DataCode(_code)

        message = src_dict.get("message")

        delete_project_response_400_data = cls(
            code=code,
            message=message,
        )

        delete_project_response_400_data.additional_properties = src_dict
        return delete_project_response_400_data

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
