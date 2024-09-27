from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ConversationsReportsResponse200Data")


@attr.s(auto_attribs=True)
class ConversationsReportsResponse200Data:
    """
    Attributes:
        total (Union[Unset, int]): Total number of conversations Example: 10.
        average_queries_per_conversation (Union[Unset, int]): Average number of queries per conversations Example: 1.2.
    """

    total: Union[Unset, int] = UNSET
    average_queries_per_conversation: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        total = self.total
        average_queries_per_conversation = self.average_queries_per_conversation

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if total is not UNSET:
            field_dict["total"] = total
        if average_queries_per_conversation is not UNSET:
            field_dict["average_queries_per_conversation"] = average_queries_per_conversation

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        total = src_dict.get("total")

        average_queries_per_conversation = src_dict.get("average_queries_per_conversation")

        conversations_reports_response_200_data = cls(
            total=total,
            average_queries_per_conversation=average_queries_per_conversation,
        )

        conversations_reports_response_200_data.additional_properties = src_dict
        return conversations_reports_response_200_data

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
