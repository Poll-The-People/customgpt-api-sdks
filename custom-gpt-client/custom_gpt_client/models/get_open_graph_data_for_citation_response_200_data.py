from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.open_graph_cache import OpenGraphCache


T = TypeVar("T", bound="GetOpenGraphDataForCitationResponse200Data")


@attr.s(auto_attribs=True)
class GetOpenGraphDataForCitationResponse200Data:
    """
    Attributes:
        open_graph_cache_schema (Union[Unset, OpenGraphCache]):
    """

    open_graph_cache_schema: Union[Unset, "OpenGraphCache"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        open_graph_cache_schema: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.open_graph_cache_schema, Unset):
            open_graph_cache_schema = self.open_graph_cache_schema.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if open_graph_cache_schema is not UNSET:
            field_dict["OpenGraphCacheSchema"] = open_graph_cache_schema

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.open_graph_cache import OpenGraphCache

        d = src_dict.copy()
        _open_graph_cache_schema = d.pop("OpenGraphCacheSchema", UNSET)
        open_graph_cache_schema: Union[Unset, OpenGraphCache]
        if isinstance(_open_graph_cache_schema, Unset):
            open_graph_cache_schema = UNSET
        else:
            open_graph_cache_schema = OpenGraphCache.from_dict(_open_graph_cache_schema)

        get_open_graph_data_for_citation_response_200_data = cls(
            open_graph_cache_schema=open_graph_cache_schema,
        )

        get_open_graph_data_for_citation_response_200_data.additional_properties = d
        return get_open_graph_data_for_citation_response_200_data

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
