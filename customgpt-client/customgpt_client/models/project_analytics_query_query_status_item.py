from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ProjectAnalyticsQueryQueryStatusItem")


@attr.s(auto_attribs=True)
class ProjectAnalyticsQueryQueryStatusItem:
    """
    Attributes:
        status (Union[Unset, ProjectAnalyticsQueryQueryStatusItemStatus]):
        count (Union[Unset, int]):  Example: 2.
    """

    status: Union[Unset, str] = UNSET
    count: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status

        count = self.count

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if status is not UNSET:
            field_dict["status"] = status
        if count is not UNSET:
            field_dict["count"] = count

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        status = src_dict.get("status")

        count = src_dict.get("count")

        project_analytics_query_query_status_item = cls(
            status=status,
            count=count,
        )

        project_analytics_query_query_status_item.additional_properties = src_dict
        return project_analytics_query_query_status_item

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
