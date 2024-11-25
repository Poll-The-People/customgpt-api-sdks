from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="AnalysisReportsResponse200DataQueriesPerConversationItem")


@attr.s(auto_attribs=True)
class AnalysisReportsResponse200DataQueriesPerConversationItem:
    """
    Attributes:
        queries_number (Union[Unset, int]):  Example: 1.5.
        created_at_interval (Union[Unset, str]):  Example: Sat.
    """

    queries_number: Union[Unset, int] = UNSET
    created_at_interval: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        queries_number = self.queries_number
        created_at_interval = self.created_at_interval

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if queries_number is not UNSET:
            field_dict["queries_number"] = queries_number
        if created_at_interval is not UNSET:
            field_dict["created_at_interval"] = created_at_interval

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        queries_number = src_dict.get("queries_number")

        created_at_interval = src_dict.get("created_at_interval")

        analysis_reports_response_200_data_queries_per_conversation_item = cls(
            queries_number=queries_number,
            created_at_interval=created_at_interval,
        )

        analysis_reports_response_200_data_queries_per_conversation_item.additional_properties = src_dict
        return analysis_reports_response_200_data_queries_per_conversation_item

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
