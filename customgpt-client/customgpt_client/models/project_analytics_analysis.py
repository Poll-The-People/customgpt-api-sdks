from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.project_analytics_analysis_conversations_item import ProjectAnalyticsAnalysisConversationsItem
    from ..models.project_analytics_analysis_queries_item import ProjectAnalyticsAnalysisQueriesItem
    from ..models.project_analytics_analysis_queries_per_conversation_item import (
        ProjectAnalyticsAnalysisQueriesPerConversationItem,
    )


T = TypeVar("T", bound="ProjectAnalyticsAnalysis")


@attr.s(auto_attribs=True)
class ProjectAnalyticsAnalysis:
    """
    Attributes:
        queries (Union[Unset, List['ProjectAnalyticsAnalysisQueriesItem']]):
        conversations (Union[Unset, List['ProjectAnalyticsAnalysisConversationsItem']]):
        queries_per_conversation (Union[Unset, List['ProjectAnalyticsAnalysisQueriesPerConversationItem']]):
    """

    queries: Union[Unset, List["ProjectAnalyticsAnalysisQueriesItem"]] = UNSET
    conversations: Union[Unset, List["ProjectAnalyticsAnalysisConversationsItem"]] = UNSET
    queries_per_conversation: Union[Unset, List["ProjectAnalyticsAnalysisQueriesPerConversationItem"]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        queries: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.queries, Unset):
            queries = []
            for queries_item_data in self.queries:
                queries_item = queries_item_data.to_dict()

                queries.append(queries_item)

        conversations: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.conversations, Unset):
            conversations = []
            for conversations_item_data in self.conversations:
                conversations_item = conversations_item_data.to_dict()

                conversations.append(conversations_item)

        queries_per_conversation: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.queries_per_conversation, Unset):
            queries_per_conversation = []
            for queries_per_conversation_item_data in self.queries_per_conversation:
                queries_per_conversation_item = queries_per_conversation_item_data.to_dict()

                queries_per_conversation.append(queries_per_conversation_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if queries is not UNSET:
            for index, field_value in enumerate(queries):
                field_dict[f"queries[{index}]"] = field_value
        if conversations is not UNSET:
            for index, field_value in enumerate(conversations):
                field_dict[f"conversations[{index}]"] = field_value
        if queries_per_conversation is not UNSET:
            for index, field_value in enumerate(queries_per_conversation):
                field_dict[f"queries_per_conversation[{index}]"] = field_value

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.project_analytics_analysis_conversations_item import ProjectAnalyticsAnalysisConversationsItem
        from ..models.project_analytics_analysis_queries_item import ProjectAnalyticsAnalysisQueriesItem
        from ..models.project_analytics_analysis_queries_per_conversation_item import (
            ProjectAnalyticsAnalysisQueriesPerConversationItem,
        )

        queries = []
        _queries = src_dict.get("queries")
        for queries_item_data in _queries or []:
            queries_item = ProjectAnalyticsAnalysisQueriesItem.from_dict(queries_item_data)

            queries.append(queries_item)

        conversations = []
        _conversations = src_dict.get("conversations")
        for conversations_item_data in _conversations or []:
            conversations_item = ProjectAnalyticsAnalysisConversationsItem.from_dict(conversations_item_data)

            conversations.append(conversations_item)

        queries_per_conversation = []
        _queries_per_conversation = src_dict.get("queries_per_conversation")
        for queries_per_conversation_item_data in _queries_per_conversation or []:
            queries_per_conversation_item = ProjectAnalyticsAnalysisQueriesPerConversationItem.from_dict(
                queries_per_conversation_item_data
            )

            queries_per_conversation.append(queries_per_conversation_item)

        project_analytics_analysis = cls(
            queries=queries,
            conversations=conversations,
            queries_per_conversation=queries_per_conversation,
        )

        project_analytics_analysis.additional_properties = src_dict
        return project_analytics_analysis

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
