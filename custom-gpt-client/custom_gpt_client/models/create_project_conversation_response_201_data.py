from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_project_conversation_response_201_data_conversation import (
        CreateProjectConversationResponse201DataConversation,
    )


T = TypeVar("T", bound="CreateProjectConversationResponse201Data")


@attr.s(auto_attribs=True)
class CreateProjectConversationResponse201Data:
    """
    Attributes:
        conversation (Union[Unset, CreateProjectConversationResponse201DataConversation]):
    """

    conversation: Union[Unset, "CreateProjectConversationResponse201DataConversation"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        conversation: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.conversation, Unset):
            conversation = self.conversation.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if conversation is not UNSET:
            field_dict["conversation"] = conversation

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.create_project_conversation_response_201_data_conversation import (
            CreateProjectConversationResponse201DataConversation,
        )

        d = src_dict.copy()
        _conversation = d.pop("conversation", UNSET)
        conversation: Union[Unset, CreateProjectConversationResponse201DataConversation]
        if isinstance(_conversation, Unset):
            conversation = UNSET
        else:
            conversation = CreateProjectConversationResponse201DataConversation.from_dict(_conversation)

        create_project_conversation_response_201_data = cls(
            conversation=conversation,
        )

        create_project_conversation_response_201_data.additional_properties = d
        return create_project_conversation_response_201_data

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
