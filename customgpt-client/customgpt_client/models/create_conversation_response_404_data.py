from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.create_conversation_response_404_data_code import CreateConversationResponse404DataCode
from ..models.create_conversation_response_404_data_message import CreateConversationResponse404DataMessage
from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateConversationResponse404Data")


@attr.s(auto_attribs=True)
class CreateConversationResponse404Data:
    """
    Attributes:
        code (Union[Unset, CreateConversationResponse404DataCode]): The error status code Example: 404.
        message (Union[Unset, CreateConversationResponse404DataMessage]): The error message Example: Project with id 1
            not found.
    """

    code: Union[Unset, CreateConversationResponse404DataCode] = UNSET
    message: Union[Unset, CreateConversationResponse404DataMessage] = UNSET
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
        _code = src_dict.get("code")
        code: Union[Unset, CreateConversationResponse404DataCode]
        if isinstance(_code, Unset):
            code = UNSET
        else:
            code = CreateConversationResponse404DataCode(_code)

        _message = src_dict.get("message")
        message: Union[Unset, CreateConversationResponse404DataMessage]
        if isinstance(_message, Unset):
            message = UNSET
        else:
            message = CreateConversationResponse404DataMessage(_message)

        create_conversation_response_404_data = cls(
            code=code,
            message=message,
        )

        create_conversation_response_404_data.additional_properties = src_dict
        return create_conversation_response_404_data

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
