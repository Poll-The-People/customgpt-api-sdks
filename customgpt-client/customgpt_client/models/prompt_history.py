import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.prompt_history_metadata import PromptHistoryMetadata


T = TypeVar("T", bound="PromptHistory")


@attr.s(auto_attribs=True)
class PromptHistory:
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
        metadata (Union[Unset, PromptHistoryMetadata]):  Example: {'user_ip': '127.0.0.1', 'user_agent': 'Mozilla/5.0
            (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko)'}.
    """

    id: Union[Unset, int] = UNSET
    user_id: Union[Unset, int] = UNSET
    user_query: Union[Unset, str] = UNSET
    openai_response: Union[Unset, str] = UNSET
    created_at: Union[Unset, datetime.datetime] = UNSET
    updated_at: Union[Unset, datetime.datetime] = UNSET
    conversation_id: Union[Unset, int] = UNSET
    citations: Union[Unset, List[int]] = UNSET
    metadata: Union[Unset, "PromptHistoryMetadata"] = UNSET
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

        metadata: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

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
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.prompt_history_metadata import PromptHistoryMetadata

        id = src_dict.get("id")

        user_id = src_dict.get("user_id")

        user_query = src_dict.get("user_query")

        openai_response = src_dict.get("openai_response")

        _created_at = src_dict.get("created_at")
        created_at: Union[Unset, datetime.datetime]
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = isoparse(_created_at)

        _updated_at = src_dict.get("updated_at")
        updated_at: Union[Unset, datetime.datetime]
        if isinstance(_updated_at, Unset):
            updated_at = UNSET
        else:
            updated_at = isoparse(_updated_at)

        conversation_id = src_dict.get("conversation_id")

        citations = cast(List[int], src_dict.get("citations"))

        _metadata = src_dict.get("metadata")
        metadata: Union[Unset, PromptHistoryMetadata]
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = PromptHistoryMetadata.from_dict(_metadata)

        prompt_history = cls(
            id=id,
            user_id=user_id,
            user_query=user_query,
            openai_response=openai_response,
            created_at=created_at,
            updated_at=updated_at,
            conversation_id=conversation_id,
            citations=citations,
            metadata=metadata,
        )

        prompt_history.additional_properties = src_dict
        return prompt_history

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
