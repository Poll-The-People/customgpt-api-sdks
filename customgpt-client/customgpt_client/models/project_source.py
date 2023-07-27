import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.project_source_type import ProjectSourceType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.project_source_pages_item import ProjectSourcePagesItem
    from ..models.project_source_settings import ProjectSourceSettings


T = TypeVar("T", bound="ProjectSource")


@attr.s(auto_attribs=True)
class ProjectSource:
    """
    Attributes:
        id (Union[Unset, int]): The project source ID Example: 1.
        created_at (Union[Unset, datetime.datetime]): The project source creation date Example: 2021-01-01 00:00:00.
        updated_at (Union[Unset, datetime.datetime]): The project source update date Example: 2021-01-01 00:00:00.
        type (Union[Unset, ProjectSourceType]): The project source type Example: sitemap.
        settings (Union[Unset, ProjectSourceSettings]): The project source settings
        pages (Union[Unset, None, List['ProjectSourcePagesItem']]): The project source pages
    """

    id: Union[Unset, int] = UNSET
    created_at: Union[Unset, datetime.datetime] = UNSET
    updated_at: Union[Unset, datetime.datetime] = UNSET
    type: Union[Unset, ProjectSourceType] = UNSET
    settings: Union[Unset, "ProjectSourceSettings"] = UNSET
    pages: Union[Unset, None, List["ProjectSourcePagesItem"]] = UNSET
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
        from ..models.project_source_pages_item import ProjectSourcePagesItem
        from ..models.project_source_settings import ProjectSourceSettings

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
        type: Union[Unset, ProjectSourceType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = ProjectSourceType(_type)

        _settings = src_dict.get("settings")
        settings: Union[Unset, ProjectSourceSettings]
        if isinstance(_settings, Unset):
            settings = UNSET
        else:
            settings = ProjectSourceSettings.from_dict(_settings)

        pages = []
        _pages = src_dict.get("pages")
        for pages_item_data in _pages or []:
            pages_item = ProjectSourcePagesItem.from_dict(pages_item_data)

            pages.append(pages_item)

        project_source = cls(
            id=id,
            created_at=created_at,
            updated_at=updated_at,
            type=type,
            settings=settings,
            pages=pages,
        )

        project_source.additional_properties = src_dict
        return project_source

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
