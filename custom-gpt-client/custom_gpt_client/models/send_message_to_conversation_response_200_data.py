import datetime
from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="SendMessageToConversationResponse200Data")


@attr.s(auto_attribs=True)
class SendMessageToConversationResponse200Data:
    """
    Attributes:
        id (Union[Unset, int]): The unique identifier of the prompt history. Example: 1.
        user_id (Union[Unset, int]): The unique identifier of the user. Example: 1.
        user_query (Union[Unset, str]): The user prompt query. Example: What is the meaning of life?.
        openai_response (Union[Unset, str]): The OpenAI response to the user prompt query. Example: The meaning of life
            is to be happy..
        created_at (Union[Unset, datetime.datetime]): The date and time the prompt history was created. Example:
            2021-01-01 00:00:00.
        updated_at (Union[Unset, datetime.datetime]): The date and time the prompt history was last updated. Example:
            2021-01-01 00:00:00.
        conversation_id (Union[Unset, int]): The unique identifier of the conversation. Example: 1.
        citations (Union[Unset, List[int]]): The citations for the prompt history. Example: [1, 2, 3].
    """

    id: Union[Unset, int] = UNSET
    user_id: Union[Unset, int] = UNSET
    user_query: Union[Unset, str] = UNSET
    openai_response: Union[Unset, str] = UNSET
    created_at: Union[Unset, datetime.datetime] = UNSET
    updated_at: Union[Unset, datetime.datetime] = UNSET
    conversation_id: Union[Unset, int] = UNSET
    citations: Union[Unset, List[int]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        user_id = self.user_id
        user_query = self.user_query
        openai_response = self.openai_response
        created_at: Union[Unset, str] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        updated_at: Union[Unset, str] = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        conversation_id = self.conversation_id
        citations: Union[Unset, List[int]] = UNSET
        if not isinstance(self.citations, Unset):
            citations = self.citations

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if user_id is not UNSET:
            field_dict["user_id"] = user_id
        if user_query is not UNSET:
            field_dict["user_query"] = user_query
        if openai_response is not UNSET:
            field_dict["openai_response"] = openai_response
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if conversation_id is not UNSET:
            field_dict["conversation_id"] = conversation_id
        if citations is not UNSET:
            for index, field_value in enumerate(citations):
                field_dict[f"citations[]{index}"] = field_value

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        user_id = d.pop("user_id", UNSET)

        user_query = d.pop("user_query", UNSET)

        openai_response = d.pop("openai_response", UNSET)

        _created_at = d.pop("created_at", UNSET)
        created_at: Union[Unset, datetime.datetime]
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = isoparse(_created_at)

        _updated_at = d.pop("updated_at", UNSET)
        updated_at: Union[Unset, datetime.datetime]
        if isinstance(_updated_at, Unset):
            updated_at = UNSET
        else:
            updated_at = isoparse(_updated_at)

        conversation_id = d.pop("conversation_id", UNSET)

        citations = cast(List[int], d.pop("citations", UNSET))

        send_message_to_conversation_response_200_data = cls(
            id=id,
            user_id=user_id,
            user_query=user_query,
            openai_response=openai_response,
            created_at=created_at,
            updated_at=updated_at,
            conversation_id=conversation_id,
            citations=citations,
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
