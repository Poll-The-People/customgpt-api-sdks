from io import BytesIO
from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, File, FileJsonType, Unset

T = TypeVar("T", bound="UpdateUserMultipartData")


@attr.s(auto_attribs=True)
class UpdateUserMultipartData:
    """
    Attributes:
        profile_photo (Union[Unset, File]): User profile photo Example: avatar.png.
        name (Union[Unset, str]): User name Example: John Doe.
    """

    profile_photo: Union[Unset, File] = UNSET
    name: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        profile_photo: Union[Unset, FileJsonType] = UNSET
        if not isinstance(self.profile_photo, Unset):
            profile_photo = self.profile_photo.to_tuple()

        name = self.name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if profile_photo is not UNSET:
            field_dict["profile_photo"] = profile_photo
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    def to_multipart(self) -> Dict[str, Any]:
        profile_photo: Union[Unset, FileJsonType] = UNSET
        if not isinstance(self.profile_photo, Unset):
            profile_photo = self.profile_photo.to_tuple()

        name = self.name if isinstance(self.name, Unset) else (None, str(self.name).encode(), "text/plain")

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {key: (None, str(value).encode(), "text/plain") for key, value in self.additional_properties.items()}
        )
        field_dict.update({})
        if profile_photo is not UNSET:
            field_dict["profile_photo"] = profile_photo
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        _profile_photo = src_dict.get("profile_photo")
        profile_photo: Union[Unset, File]
        if isinstance(_profile_photo, Unset):
            profile_photo = UNSET
        else:
            profile_photo = File(payload=BytesIO(_profile_photo))

        name = src_dict.get("name")

        update_user_multipart_data = cls(
            profile_photo=profile_photo,
            name=name,
        )

        update_user_multipart_data.additional_properties = src_dict
        return update_user_multipart_data

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
