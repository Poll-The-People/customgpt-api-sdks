from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.messages_conversation_response_200_data_conversation import (
        MessagesConversationResponse200DataConversation,
    )
    from ..models.messages_conversation_response_200_data_messages import MessagesConversationResponse200DataMessages


T = TypeVar("T", bound="MessagesConversationResponse200Data")


@attr.s(auto_attribs=True)
class MessagesConversationResponse200Data:
    """
    Attributes:
        conversation (Union[Unset, MessagesConversationResponse200DataConversation]):
        messages (Union[Unset, MessagesConversationResponse200DataMessages]):
    """

    conversation: Union[Unset, "MessagesConversationResponse200DataConversation"] = UNSET
    messages: Union[Unset, "MessagesConversationResponse200DataMessages"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        conversation: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.conversation, Unset):
            conversation = self.conversation.to_dict()

        messages: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.messages, Unset):
            messages = self.messages.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if conversation is not UNSET:
            field_dict["conversation"] = conversation
        if messages is not UNSET:
            field_dict["messages"] = messages

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.messages_conversation_response_200_data_conversation import (
            MessagesConversationResponse200DataConversation,
        )
        from ..models.messages_conversation_response_200_data_messages import (
            MessagesConversationResponse200DataMessages,
        )

        _conversation = src_dict.get("conversation")
        conversation: Union[Unset, MessagesConversationResponse200DataConversation]
        if isinstance(_conversation, Unset):
            conversation = UNSET
        else:
            conversation = MessagesConversationResponse200DataConversation.from_dict(_conversation)

        _messages = src_dict.get("messages")
        messages: Union[Unset, MessagesConversationResponse200DataMessages]
        if isinstance(_messages, Unset):
            messages = UNSET
        else:
            messages = MessagesConversationResponse200DataMessages.from_dict(_messages)

        messages_conversation_response_200_data = cls(
            conversation=conversation,
            messages=messages,
        )

        messages_conversation_response_200_data.additional_properties = src_dict
        return messages_conversation_response_200_data

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
