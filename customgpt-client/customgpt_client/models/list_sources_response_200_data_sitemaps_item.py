import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.list_sources_response_200_data_sitemaps_item_type import ListSourcesResponse200DataSitemapsItemType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.list_sources_response_200_data_sitemaps_item_pages_item import (
        ListSourcesResponse200DataSitemapsItemPagesItem,
    )
    from ..models.list_sources_response_200_data_sitemaps_item_settings import (
        ListSourcesResponse200DataSitemapsItemSettings,
    )


T = TypeVar("T", bound="ListSourcesResponse200DataSitemapsItem")


@attr.s(auto_attribs=True)
class ListSourcesResponse200DataSitemapsItem:
    """
    Attributes:
        id (Union[Unset, int]): The project source ID Example: 1.
        created_at (Union[Unset, datetime.datetime]): The project source creation date Example: 2021-01-01 00:00:00.
        updated_at (Union[Unset, datetime.datetime]): The project source update date Example: 2021-01-01 00:00:00.
        type (Union[Unset, ListSourcesResponse200DataSitemapsItemType]): The project source type Example: sitemap.
        settings (Union[Unset, ListSourcesResponse200DataSitemapsItemSettings]): The project source settings
        pages (Union[Unset, None, List['ListSourcesResponse200DataSitemapsItemPagesItem']]): The project source pages
    """

    id: Union[Unset, int] = UNSET
    created_at: Union[Unset, datetime.datetime] = UNSET
    updated_at: Union[Unset, datetime.datetime] = UNSET
    type: Union[Unset, ListSourcesResponse200DataSitemapsItemType] = UNSET
    settings: Union[Unset, "ListSourcesResponse200DataSitemapsItemSettings"] = UNSET
    pages: Union[Unset, None, List["ListSourcesResponse200DataSitemapsItemPagesItem"]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        created_at: Union[Unset, str] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        updated_at: Union[Unset, str] = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        settings: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.settings, Unset):
            settings = self.settings.to_dict()

        pages: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.pages, Unset):
            if self.pages is None:
                pages = None
            else:
                pages = []
                for pages_item_data in self.pages:
                    pages_item = pages_item_data.to_dict()

                    pages.append(pages_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if type is not UNSET:
            field_dict["type"] = type
        if settings is not UNSET:
            field_dict["settings"] = settings
        if pages is not UNSET:
            for index, field_value in enumerate(pages):
                field_dict[f"pages[]{index}"] = field_value

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.list_sources_response_200_data_sitemaps_item_pages_item import (
            ListSourcesResponse200DataSitemapsItemPagesItem,
        )
        from ..models.list_sources_response_200_data_sitemaps_item_settings import (
            ListSourcesResponse200DataSitemapsItemSettings,
        )

        id = src_dict.get("id")

        _created_at = src_dict.get("created_at")
        created_at: Union[Unset, datetime.datetime]
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = isoparse(_created_at)

        _updated_at = src_dict.get("updated_at")
        updated_at: Union[Unset, datetime.datetime]
        if isinstance(_updated_at, Unset):
            updated_at = UNSET
        else:
            updated_at = isoparse(_updated_at)

        _type = src_dict.get("type")
        type: Union[Unset, ListSourcesResponse200DataSitemapsItemType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = ListSourcesResponse200DataSitemapsItemType(_type)

        _settings = src_dict.get("settings")
        settings: Union[Unset, ListSourcesResponse200DataSitemapsItemSettings]
        if isinstance(_settings, Unset):
            settings = UNSET
        else:
            settings = ListSourcesResponse200DataSitemapsItemSettings.from_dict(_settings)

        pages = []
        _pages = src_dict.get("pages")
        for pages_item_data in _pages or []:
            pages_item = ListSourcesResponse200DataSitemapsItemPagesItem.from_dict(pages_item_data)

            pages.append(pages_item)

        list_sources_response_200_data_sitemaps_item = cls(
            id=id,
            created_at=created_at,
            updated_at=updated_at,
            type=type,
            settings=settings,
            pages=pages,
        )

        list_sources_response_200_data_sitemaps_item.additional_properties = src_dict
        return list_sources_response_200_data_sitemaps_item

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
