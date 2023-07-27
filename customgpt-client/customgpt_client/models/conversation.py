import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="Conversation")


@attr.s(auto_attribs=True)
class Conversation:
    """
    Attributes:
        created_at (Union[Unset, datetime.datetime]): When was this conversation created? Example: 2023-04-30 16:43:53.
        updated_at (Union[Unset, datetime.datetime]): When was this conversation updated? Example: 2023-04-30 16:43:53.
        deleted_at (Union[Unset, None, datetime.datetime]): When was this conversation deleted? Example: 2023-04-30
            16:43:53.
        id (Union[Unset, int]): Conversation ID Example: 1.
        name (Union[Unset, str]): Conversation name Example: Conversation 1.
        project_id (Union[Unset, str]): Project ID for this conversation Example: 1.
        created_by (Union[Unset, str]): User ID for the user who created this conversation Example: 1.
        session_id (Union[Unset, str]): Session ID for this conversation Example: f1b9aaf0-5e4e-11eb-ae93-0242ac130002.
    """

    created_at: Union[Unset, datetime.datetime] = UNSET
    updated_at: Union[Unset, datetime.datetime] = UNSET
    deleted_at: Union[Unset, None, datetime.datetime] = UNSET
    id: Union[Unset, int] = UNSET
    name: Union[Unset, str] = UNSET
    project_id: Union[Unset, str] = UNSET
    created_by: Union[Unset, str] = UNSET
    session_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        created_at: Union[Unset, str] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        updated_at: Union[Unset, str] = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        deleted_at: Union[Unset, None, str] = UNSET
        if not isinstance(self.deleted_at, Unset):
            deleted_at = self.deleted_at.isoformat() if self.deleted_at else None

        id = self.id
        name = self.name
        project_id = self.project_id
        created_by = self.created_by
        session_id = self.session_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if deleted_at is not UNSET:
            field_dict["deleted_at"] = deleted_at
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if project_id is not UNSET:
            field_dict["project_id"] = project_id
        if created_by is not UNSET:
            field_dict["created_by"] = created_by
        if session_id is not UNSET:
            field_dict["session_id"] = session_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
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

        id = src_dict.get("id")

        name = src_dict.get("name")

        project_id = src_dict.get("project_id")

        created_by = src_dict.get("created_by")

        session_id = src_dict.get("session_id")

        conversation = cls(
            created_at=created_at,
            updated_at=updated_at,
            deleted_at=deleted_at,
            id=id,
            name=name,
            project_id=project_id,
            created_by=created_by,
            session_id=session_id,
        )

        conversation.additional_properties = src_dict
        return conversation

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
