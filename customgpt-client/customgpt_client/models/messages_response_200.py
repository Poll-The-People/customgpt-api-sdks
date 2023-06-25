from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.messages_response_200_status import MessagesResponse200Status
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.messages_response_200_conversation import MessagesResponse200Conversation
    from ..models.messages_response_200_messages import MessagesResponse200Messages


T = TypeVar("T", bound="MessagesResponse200")


@attr.s(auto_attribs=True)
class MessagesResponse200:
    """
    Attributes:
        status (Union[Unset, MessagesResponse200Status]): The status of the response Example: success.
        conversation (Union[Unset, MessagesResponse200Conversation]):
        messages (Union[Unset, MessagesResponse200Messages]):
    """

    status: Union[Unset, MessagesResponse200Status] = UNSET
    conversation: Union[Unset, "MessagesResponse200Conversation"] = UNSET
    messages: Union[Unset, "MessagesResponse200Messages"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        conversation: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.conversation, Unset):
            conversation = self.conversation.to_dict()

        messages: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.messages, Unset):
            messages = self.messages.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if status is not UNSET:
            field_dict["status"] = status
        if conversation is not UNSET:
            field_dict["conversation"] = conversation
        if messages is not UNSET:
            field_dict["messages"] = messages

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.messages_response_200_conversation import MessagesResponse200Conversation
        from ..models.messages_response_200_messages import MessagesResponse200Messages

        d = src_dict.copy()
        _status = d.pop("status", UNSET)
        status: Union[Unset, MessagesResponse200Status]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = MessagesResponse200Status(_status)

        _conversation = d.pop("conversation", UNSET)
        conversation: Union[Unset, MessagesResponse200Conversation]
        if isinstance(_conversation, Unset):
            conversation = UNSET
        else:
            conversation = MessagesResponse200Conversation.from_dict(_conversation)

        _messages = d.pop("messages", UNSET)
        messages: Union[Unset, MessagesResponse200Messages]
        if isinstance(_messages, Unset):
            messages = UNSET
        else:
            messages = MessagesResponse200Messages.from_dict(_messages)

        messages_response_200 = cls(
            status=status,
            conversation=conversation,
            messages=messages,
        )

        messages_response_200.additional_properties = d
        return messages_response_200

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
