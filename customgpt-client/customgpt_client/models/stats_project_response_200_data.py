from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="StatsProjectResponse200Data")


@attr.s(auto_attribs=True)
class StatsProjectResponse200Data:
    """
    Attributes:
        pages_found (Union[Unset, int]): Number of pages found for the project Example: 100.
        pages_crawled (Union[Unset, int]): Number of pages crawled for the project Example: 100.
        pages_indexed (Union[Unset, int]): Number of pages indexed for the project Example: 100.
        crawl_credits_used (Union[Unset, int]): Number of crawl credits used for the project Example: 100.
        query_credits_used (Union[Unset, int]): Number of query credits used for the project Example: 100.
        index_credits_used (Union[Unset, int]): Number of index credits used for the project Example: 100.
    """

    pages_found: Union[Unset, int] = UNSET
    pages_crawled: Union[Unset, int] = UNSET
    pages_indexed: Union[Unset, int] = UNSET
    crawl_credits_used: Union[Unset, int] = UNSET
    query_credits_used: Union[Unset, int] = UNSET
    index_credits_used: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        pages_found = self.pages_found
        pages_crawled = self.pages_crawled
        pages_indexed = self.pages_indexed
        crawl_credits_used = self.crawl_credits_used
        query_credits_used = self.query_credits_used
        index_credits_used = self.index_credits_used

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if pages_found is not UNSET:
            field_dict["pages_found"] = pages_found
        if pages_crawled is not UNSET:
            field_dict["pages_crawled"] = pages_crawled
        if pages_indexed is not UNSET:
            field_dict["pages_indexed"] = pages_indexed
        if crawl_credits_used is not UNSET:
            field_dict["crawl_credits_used"] = crawl_credits_used
        if query_credits_used is not UNSET:
            field_dict["query_credits_used"] = query_credits_used
        if index_credits_used is not UNSET:
            field_dict["index_credits_used"] = index_credits_used

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        pages_found = src_dict.get("pages_found")

        pages_crawled = src_dict.get("pages_crawled")

        pages_indexed = src_dict.get("pages_indexed")

        crawl_credits_used = src_dict.get("crawl_credits_used")

        query_credits_used = src_dict.get("query_credits_used")

        index_credits_used = src_dict.get("index_credits_used")

        stats_project_response_200_data = cls(
            pages_found=pages_found,
            pages_crawled=pages_crawled,
            pages_indexed=pages_indexed,
            crawl_credits_used=crawl_credits_used,
            query_credits_used=query_credits_used,
            index_credits_used=index_credits_used,
        )

        stats_project_response_200_data.additional_properties = src_dict
        return stats_project_response_200_data

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
