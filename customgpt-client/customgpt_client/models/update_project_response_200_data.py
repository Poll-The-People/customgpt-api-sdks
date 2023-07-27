import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.update_project_response_200_data_type import UpdateProjectResponse200DataType
from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateProjectResponse200Data")


@attr.s(auto_attribs=True)
class UpdateProjectResponse200Data:
    """
    Attributes:
        id (Union[Unset, int]): Project ID Example: 1.
        project_name (Union[Unset, str]): Project name Example: My Project.
        sitemap_path (Union[Unset, str]): Project sitemap Example: https://www.example.com/sitemap.xml.
        is_chat_active (Union[Unset, bool]): Whether the chat bot is active or not Example: True.
        user_id (Union[Unset, int]): User ID of the project owner Example: 1.
        created_at (Union[Unset, datetime.datetime]): Date and time when the project was created Default:
            isoparse('2023-05-08 13:06:55'). Example: 2021-01-01 00:00:00.
        updated_at (Union[Unset, datetime.datetime]): Date and time when the project was last updated Default:
            isoparse('2023-05-08 13:06:55'). Example: 2021-01-01 00:00:00.
        deleted_at (Union[Unset, None, datetime.datetime]): Date and time when the project was deleted Example:
            2021-01-01 00:00:00.
        type (Union[Unset, UpdateProjectResponse200DataType]): Project type Default:
            UpdateProjectResponse200DataType.SITEMAP. Example: SITEMAP.
        is_shared (Union[Unset, bool]): Whether the project is shared or not Example: True.
        shareable_slug (Union[Unset, None, str]): Shareable slug that can be used to share the project Example:
            1234567890abcdef1234567890abcdef.
        shareable_link (Union[Unset, None, str]): Shareable link that can be used to share the project
        embed_code (Union[Unset, None, str]): Embed code that can be used to embed the project
        live_chat_code (Union[Unset, None, str]): Live chat code that can be used to embed the live chat
    """

    id: Union[Unset, int] = UNSET
    project_name: Union[Unset, str] = UNSET
    sitemap_path: Union[Unset, str] = UNSET
    is_chat_active: Union[Unset, bool] = False
    user_id: Union[Unset, int] = UNSET
    created_at: Union[Unset, datetime.datetime] = isoparse("2023-05-08 13:06:55")
    updated_at: Union[Unset, datetime.datetime] = isoparse("2023-05-08 13:06:55")
    deleted_at: Union[Unset, None, datetime.datetime] = UNSET
    type: Union[Unset, UpdateProjectResponse200DataType] = UpdateProjectResponse200DataType.SITEMAP
    is_shared: Union[Unset, bool] = False
    shareable_slug: Union[Unset, None, str] = UNSET
    shareable_link: Union[Unset, None, str] = UNSET
    embed_code: Union[Unset, None, str] = UNSET
    live_chat_code: Union[Unset, None, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        project_name = self.project_name
        sitemap_path = self.sitemap_path
        is_chat_active = self.is_chat_active
        user_id = self.user_id
        created_at: Union[Unset, str] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        updated_at: Union[Unset, str] = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        deleted_at: Union[Unset, None, str] = UNSET
        if not isinstance(self.deleted_at, Unset):
            deleted_at = self.deleted_at.isoformat() if self.deleted_at else None

        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        is_shared = self.is_shared
        shareable_slug = self.shareable_slug
        shareable_link = self.shareable_link
        embed_code = self.embed_code
        live_chat_code = self.live_chat_code

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if project_name is not UNSET:
            field_dict["project_name"] = project_name
        if sitemap_path is not UNSET:
            field_dict["sitemap_path"] = sitemap_path
        if is_chat_active is not UNSET:
            field_dict["is_chat_active"] = is_chat_active
        if user_id is not UNSET:
            field_dict["user_id"] = user_id
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if deleted_at is not UNSET:
            field_dict["deleted_at"] = deleted_at
        if type is not UNSET:
            field_dict["type"] = type
        if is_shared is not UNSET:
            field_dict["is_shared"] = is_shared
        if shareable_slug is not UNSET:
            field_dict["shareable_slug"] = shareable_slug
        if shareable_link is not UNSET:
            field_dict["shareable_link"] = shareable_link
        if embed_code is not UNSET:
            field_dict["embed_code"] = embed_code
        if live_chat_code is not UNSET:
            field_dict["live_chat_code"] = live_chat_code

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        id = src_dict.get("id")

        project_name = src_dict.get("project_name")

        sitemap_path = src_dict.get("sitemap_path")

        is_chat_active = src_dict.get("is_chat_active")

        user_id = src_dict.get("user_id")

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

        _deleted_at = src_dict.get("deleted_at")
        deleted_at: Union[Unset, None, datetime.datetime]
        if _deleted_at is None:
            deleted_at = None
        elif isinstance(_deleted_at, Unset):
            deleted_at = UNSET
        else:
            deleted_at = isoparse(_deleted_at)

        _type = src_dict.get("type")
        type: Union[Unset, UpdateProjectResponse200DataType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = UpdateProjectResponse200DataType(_type)

        is_shared = src_dict.get("is_shared")

        shareable_slug = src_dict.get("shareable_slug")

        shareable_link = src_dict.get("shareable_link")

        embed_code = src_dict.get("embed_code")

        live_chat_code = src_dict.get("live_chat_code")

        update_project_response_200_data = cls(
            id=id,
            project_name=project_name,
            sitemap_path=sitemap_path,
            is_chat_active=is_chat_active,
            user_id=user_id,
            created_at=created_at,
            updated_at=updated_at,
            deleted_at=deleted_at,
            type=type,
            is_shared=is_shared,
            shareable_slug=shareable_slug,
            shareable_link=shareable_link,
            embed_code=embed_code,
            live_chat_code=live_chat_code,
        )

        update_project_response_200_data.additional_properties = src_dict
        return update_project_response_200_data

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
