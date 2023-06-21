from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.send_message_to_conversation_response_200_data_message import (
        SendMessageToConversationResponse200DataMessage,
    )


T = TypeVar("T", bound="SendMessageToConversationResponse200Data")


@attr.s(auto_attribs=True)
class SendMessageToConversationResponse200Data:
    """
    Attributes:
        message (Union[Unset, SendMessageToConversationResponse200DataMessage]):
    """

    message: Union[Unset, "SendMessageToConversationResponse200DataMessage"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        message: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.message, Unset):
            message = self.message.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if message is not UNSET:
            field_dict["message"] = message

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.send_message_to_conversation_response_200_data_message import (
            SendMessageToConversationResponse200DataMessage,
        )

        d = src_dict.copy()
        _message = d.pop("message", UNSET)
        message: Union[Unset, SendMessageToConversationResponse200DataMessage]
        if isinstance(_message, Unset):
            message = UNSET
        else:
            message = SendMessageToConversationResponse200DataMessage.from_dict(_message)

        send_message_to_conversation_response_200_data = cls(
            message=message,
        )

        send_message_to_conversation_response_200_data.additional_properties = d
        return send_message_to_conversation_response_200_data

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
