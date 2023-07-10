from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr

if TYPE_CHECKING:
    from ..models.list_project_sources_response_200_data_sitemaps_item import (
        ListProjectSourcesResponse200DataSitemapsItem,
    )
    from ..models.list_project_sources_response_200_data_uploads import ListProjectSourcesResponse200DataUploads


T = TypeVar("T", bound="ListProjectSourcesResponse200Data")


@attr.s(auto_attribs=True)
class ListProjectSourcesResponse200Data:
    """
    Attributes:
        sitemaps (List['ListProjectSourcesResponse200DataSitemapsItem']):
        uploads (ListProjectSourcesResponse200DataUploads):
    """

    sitemaps: List["ListProjectSourcesResponse200DataSitemapsItem"]
    uploads: "ListProjectSourcesResponse200DataUploads"
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        sitemaps = []
        for sitemaps_item_data in self.sitemaps:
            sitemaps_item = sitemaps_item_data.to_dict()

            sitemaps.append(sitemaps_item)

        uploads = self.uploads.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "sitemaps": sitemaps,
                "uploads": uploads,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.list_project_sources_response_200_data_sitemaps_item import (
            ListProjectSourcesResponse200DataSitemapsItem,
        )
        from ..models.list_project_sources_response_200_data_uploads import ListProjectSourcesResponse200DataUploads

        sitemaps = []
        _sitemaps = src_dict.get("sitemaps")
        for sitemaps_item_data in _sitemaps:
            sitemaps_item = ListProjectSourcesResponse200DataSitemapsItem.from_dict(sitemaps_item_data)

            sitemaps.append(sitemaps_item)

        uploads = ListProjectSourcesResponse200DataUploads.from_dict(src_dict.get("uploads"))

        list_project_sources_response_200_data = cls(
            sitemaps=sitemaps,
            uploads=uploads,
        )

        list_project_sources_response_200_data.additional_properties = src_dict
        return list_project_sources_response_200_data

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
