from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.get_project_conversation_messages_response_200_status import (
    GetProjectConversationMessagesResponse200Status,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_project_conversation_messages_response_200_conversation import (
        GetProjectConversationMessagesResponse200Conversation,
    )
    from ..models.get_project_conversation_messages_response_200_messages import (
        GetProjectConversationMessagesResponse200Messages,
    )


T = TypeVar("T", bound="GetProjectConversationMessagesResponse200")


@attr.s(auto_attribs=True)
class GetProjectConversationMessagesResponse200:
    """
    Attributes:
        status (Union[Unset, GetProjectConversationMessagesResponse200Status]): The status of the response Example:
            success.
        conversation (Union[Unset, GetProjectConversationMessagesResponse200Conversation]):
        messages (Union[Unset, GetProjectConversationMessagesResponse200Messages]):
    """

    status: Union[Unset, GetProjectConversationMessagesResponse200Status] = UNSET
    conversation: Union[Unset, "GetProjectConversationMessagesResponse200Conversation"] = UNSET
    messages: Union[Unset, "GetProjectConversationMessagesResponse200Messages"] = UNSET
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
        from ..models.get_project_conversation_messages_response_200_conversation import (
            GetProjectConversationMessagesResponse200Conversation,
        )
        from ..models.get_project_conversation_messages_response_200_messages import (
            GetProjectConversationMessagesResponse200Messages,
        )

        d = src_dict.copy()
        _status = d.pop("status", UNSET)
        status: Union[Unset, GetProjectConversationMessagesResponse200Status]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = GetProjectConversationMessagesResponse200Status(_status)

        _conversation = d.pop("conversation", UNSET)
        conversation: Union[Unset, GetProjectConversationMessagesResponse200Conversation]
        if isinstance(_conversation, Unset):
            conversation = UNSET
        else:
            conversation = GetProjectConversationMessagesResponse200Conversation.from_dict(_conversation)

        _messages = d.pop("messages", UNSET)
        messages: Union[Unset, GetProjectConversationMessagesResponse200Messages]
        if isinstance(_messages, Unset):
            messages = UNSET
        else:
            messages = GetProjectConversationMessagesResponse200Messages.from_dict(_messages)

        get_project_conversation_messages_response_200 = cls(
            status=status,
            conversation=conversation,
            messages=messages,
        )

        get_project_conversation_messages_response_200.additional_properties = d
        return get_project_conversation_messages_response_200

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
