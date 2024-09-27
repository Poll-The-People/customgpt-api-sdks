from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateMetadataJsonBody")


@attr.s(auto_attribs=True)
class UpdateMetadataJsonBody:
    """
    Attributes:
        title (Union[Unset, None, str]): The title of the page used in citations Example: Title.
        url (Union[Unset, None, str]): The url of the page used in citations Example: https://example.com/.
        description (Union[Unset, None, str]): The description of the page used in citations Example: One to two
            sentences..
        image (Union[Unset, None, str]): The url of the image used in citations Example: https://example.com/image.png.
    """

    title: Union[Unset, None, str] = UNSET
    url: Union[Unset, None, str] = UNSET
    description: Union[Unset, None, str] = UNSET
    image: Union[Unset, None, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        title = self.title
        url = self.url
        description = self.description
        image = self.image

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if title is not UNSET:
            field_dict["title"] = title
        if url is not UNSET:
            field_dict["url"] = url
        if description is not UNSET:
            field_dict["description"] = description
        if image is not UNSET:
            field_dict["image"] = image

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        title = src_dict.get("title")

        url = src_dict.get("url")

        description = src_dict.get("description")

        image = src_dict.get("image")

        update_metadata_json_body = cls(
            title=title,
            url=url,
            description=description,
            image=image,
        )

        update_metadata_json_body.additional_properties = src_dict
        return update_metadata_json_body

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
