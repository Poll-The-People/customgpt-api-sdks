from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.list_sources_response_200_data_sitemaps_item import ListSourcesResponse200DataSitemapsItem
    from ..models.list_sources_response_200_data_uploads import ListSourcesResponse200DataUploads


T = TypeVar("T", bound="ListSourcesResponse200Data")


@attr.s(auto_attribs=True)
class ListSourcesResponse200Data:
    """
    Attributes:
        sitemaps (Union[Unset, List['ListSourcesResponse200DataSitemapsItem']]):
        uploads (Union[Unset, ListSourcesResponse200DataUploads]):
    """

    sitemaps: Union[Unset, List["ListSourcesResponse200DataSitemapsItem"]] = UNSET
    uploads: Union[Unset, "ListSourcesResponse200DataUploads"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        sitemaps: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.sitemaps, Unset):
            sitemaps = []
            for sitemaps_item_data in self.sitemaps:
                sitemaps_item = sitemaps_item_data.to_dict()

                sitemaps.append(sitemaps_item)

        uploads: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.uploads, Unset):
            uploads = self.uploads.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if sitemaps is not UNSET:
            for index, field_value in enumerate(sitemaps):
                field_dict[f"sitemaps[]{index}"] = field_value
        if uploads is not UNSET:
            field_dict["uploads"] = uploads

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.list_sources_response_200_data_sitemaps_item import ListSourcesResponse200DataSitemapsItem
        from ..models.list_sources_response_200_data_uploads import ListSourcesResponse200DataUploads

        sitemaps = []
        _sitemaps = src_dict.get("sitemaps")
        for sitemaps_item_data in _sitemaps or []:
            sitemaps_item = ListSourcesResponse200DataSitemapsItem.from_dict(sitemaps_item_data)

            sitemaps.append(sitemaps_item)

        _uploads = src_dict.get("uploads")
        uploads: Union[Unset, ListSourcesResponse200DataUploads]
        if isinstance(_uploads, Unset):
            uploads = UNSET
        else:
            uploads = ListSourcesResponse200DataUploads.from_dict(_uploads)

        list_sources_response_200_data = cls(
            sitemaps=sitemaps,
            uploads=uploads,
        )

        list_sources_response_200_data.additional_properties = src_dict
        return list_sources_response_200_data

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
