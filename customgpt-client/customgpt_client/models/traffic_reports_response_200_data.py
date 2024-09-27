from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.traffic_reports_response_200_data_sources_item import TrafficReportsResponse200DataSourcesItem


T = TypeVar("T", bound="TrafficReportsResponse200Data")


@attr.s(auto_attribs=True)
class TrafficReportsResponse200Data:
    """
    Attributes:
        sources (Union[Unset, List['TrafficReportsResponse200DataSourcesItem']]):
    """

    sources: Union[Unset, List["TrafficReportsResponse200DataSourcesItem"]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        sources: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.sources, Unset):
            sources = []
            for sources_item_data in self.sources:
                sources_item = sources_item_data.to_dict()

                sources.append(sources_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if sources is not UNSET:
            for index, field_value in enumerate(sources):
                field_dict[f"sources[{index}]"] = field_value

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.traffic_reports_response_200_data_sources_item import TrafficReportsResponse200DataSourcesItem

        sources = []
        _sources = src_dict.get("sources")
        for sources_item_data in _sources or []:
            sources_item = TrafficReportsResponse200DataSourcesItem.from_dict(sources_item_data)

            sources.append(sources_item)

        traffic_reports_response_200_data = cls(
            sources=sources,
        )

        traffic_reports_response_200_data.additional_properties = src_dict
        return traffic_reports_response_200_data

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
