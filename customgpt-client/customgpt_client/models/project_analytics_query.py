from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.project_analytics_query_query_status_item import ProjectAnalyticsQueryQueryStatusItem


T = TypeVar("T", bound="ProjectAnalyticsQuery")


@attr.s(auto_attribs=True)
class ProjectAnalyticsQuery:
    """
    Attributes:
        total (Union[Unset, int]): Total number of queries over all conversations Example: 10.
        query_status (Union[Unset, List['ProjectAnalyticsQueryQueryStatusItem']]): Number of successful and failed
            queries over all conversations
    """

    total: Union[Unset, int] = UNSET
    query_status: Union[Unset, List["ProjectAnalyticsQueryQueryStatusItem"]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        total = self.total
        query_status: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.query_status, Unset):
            query_status = []
            for query_status_item_data in self.query_status:
                query_status_item = query_status_item_data.to_dict()

                query_status.append(query_status_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if total is not UNSET:
            field_dict["total"] = total
        if query_status is not UNSET:
            for index, field_value in enumerate(query_status):
                field_dict[f"query_status[{index}]"] = field_value

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.project_analytics_query_query_status_item import ProjectAnalyticsQueryQueryStatusItem

        total = src_dict.get("total")

        query_status = []
        _query_status = src_dict.get("query_status")
        for query_status_item_data in _query_status or []:
            query_status_item = ProjectAnalyticsQueryQueryStatusItem.from_dict(query_status_item_data)

            query_status.append(query_status_item)

        project_analytics_query = cls(
            total=total,
            query_status=query_status,
        )

        project_analytics_query.additional_properties = src_dict
        return project_analytics_query

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
