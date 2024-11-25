from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="TrafficReportsResponse200DataSourcesItem")


@attr.s(auto_attribs=True)
class TrafficReportsResponse200DataSourcesItem:
    """
    Attributes:
        request_source (Union[Unset, TrafficReportsResponse200DataSourcesItemRequestSource]):  Example: web.
        request_source_number (Union[Unset, int]):  Example: 20.
    """

    request_source: Union[Unset, str] = UNSET
    request_source_number: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        request_source: Union[Unset, str] = UNSET
        if not isinstance(self.request_source, Unset):
            request_source = self.request_source

        request_source_number = self.request_source_number

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if request_source is not UNSET:
            field_dict["request_source"] = request_source
        if request_source_number is not UNSET:
            field_dict["request_source_number"] = request_source_number

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        request_source = src_dict.get("request_source")

        request_source_number = src_dict.get("request_source_number")

        traffic_reports_response_200_data_sources_item = cls(
            request_source=request_source,
            request_source_number=request_source_number,
        )

        traffic_reports_response_200_data_sources_item.additional_properties = src_dict
        return traffic_reports_response_200_data_sources_item

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
