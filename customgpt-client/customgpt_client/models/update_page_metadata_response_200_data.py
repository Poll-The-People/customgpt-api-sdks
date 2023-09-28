from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdatePageMetadataResponse200Data")


@attr.s(auto_attribs=True)
class UpdatePageMetadataResponse200Data:
    """
    Attributes:
        url (Union[Unset, str]): The URL of the page Example: https://www.example.com.
        title (Union[Unset, str]): The title of the page Example: Example Domain.
        description (Union[Unset, str]): The description of the page Example: This domain is for use in illustrative
            examples in documents. You may use this domain in literature without prior coordination or asking for
            permission..
        image (Union[Unset, str]): The image of the page Example: https://www.example.com/image.png.
    """

    url: Union[Unset, str] = UNSET
    title: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    image: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        url = self.url
        title = self.title
        description = self.description
        image = self.image

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if url is not UNSET:
            field_dict["url"] = url
        if title is not UNSET:
            field_dict["title"] = title
        if description is not UNSET:
            field_dict["description"] = description
        if image is not UNSET:
            field_dict["image"] = image

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        url = src_dict.get("url")

        title = src_dict.get("title")

        description = src_dict.get("description")

        image = src_dict.get("image")

        update_page_metadata_response_200_data = cls(
            url=url,
            title=title,
            description=description,
            image=image,
        )

        update_page_metadata_response_200_data.additional_properties = src_dict
        return update_page_metadata_response_200_data

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
