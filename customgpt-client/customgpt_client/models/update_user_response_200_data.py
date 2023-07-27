import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateUserResponse200Data")


@attr.s(auto_attribs=True)
class UpdateUserResponse200Data:
    """
    Attributes:
        created_at (Union[Unset, datetime.datetime]): When was this user created? Example: 2023-04-30 16:43:53.
        email (Union[Unset, str]): User email Example: user@domain.com.
        id (Union[Unset, int]): User ID Example: 1.
        name (Union[Unset, str]): User name Example: John Doe.
        profile_photo_url (Union[Unset, str]): User profile photo URL Example:
            https://app.customgpt.ai/user/1/profile_photo_url.
        updated_at (Union[Unset, datetime.datetime]): When was this user updated? Example: 2023-04-30 16:43:53.
    """

    created_at: Union[Unset, datetime.datetime] = UNSET
    email: Union[Unset, str] = UNSET
    id: Union[Unset, int] = UNSET
    name: Union[Unset, str] = UNSET
    profile_photo_url: Union[Unset, str] = UNSET
    updated_at: Union[Unset, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        created_at: Union[Unset, str] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        email = self.email
        id = self.id
        name = self.name
        profile_photo_url = self.profile_photo_url
        updated_at: Union[Unset, str] = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if email is not UNSET:
            field_dict["email"] = email
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if profile_photo_url is not UNSET:
            field_dict["profile_photo_url"] = profile_photo_url
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        _created_at = src_dict.get("created_at")
        created_at: Union[Unset, datetime.datetime]
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = isoparse(_created_at)

        email = src_dict.get("email")

        id = src_dict.get("id")

        name = src_dict.get("name")

        profile_photo_url = src_dict.get("profile_photo_url")

        _updated_at = src_dict.get("updated_at")
        updated_at: Union[Unset, datetime.datetime]
        if isinstance(_updated_at, Unset):
            updated_at = UNSET
        else:
            updated_at = isoparse(_updated_at)

        update_user_response_200_data = cls(
            created_at=created_at,
            email=email,
            id=id,
            name=name,
            profile_photo_url=profile_photo_url,
            updated_at=updated_at,
        )

        update_user_response_200_data.additional_properties = src_dict
        return update_user_response_200_data

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
