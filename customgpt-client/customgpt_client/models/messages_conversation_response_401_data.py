from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.messages_conversation_response_401_data_code import MessagesConversationResponse401DataCode
from ..types import UNSET, Unset

T = TypeVar("T", bound="MessagesConversationResponse401Data")


@attr.s(auto_attribs=True)
class MessagesConversationResponse401Data:
    """
    Attributes:
        code (Union[Unset, MessagesConversationResponse401DataCode]): The error status code Example: 401.
        message (Union[Unset, str]):  Example: API Token is either missing or invalid.
    """

    code: Union[Unset, MessagesConversationResponse401DataCode] = UNSET
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
        code: Union[Unset, MessagesConversationResponse401DataCode]
        if isinstance(_code, Unset):
            code = UNSET
        else:
            code = MessagesConversationResponse401DataCode(_code)

        message = src_dict.get("message")

        messages_conversation_response_401_data = cls(
            code=code,
            message=message,
        )

        messages_conversation_response_401_data.additional_properties = src_dict
        return messages_conversation_response_401_data

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
