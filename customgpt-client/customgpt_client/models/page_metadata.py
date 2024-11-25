from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="PageMetadata")


@attr.s(auto_attribs=True)
class PageMetadata:
    """
    Attributes:
        id (Union[Unset, int]): The unique identifier of the page Example: 1.
        url (Union[Unset, None, str]): The URL of the page Example: https://www.example.com.
        title (Union[Unset, None, str]): The title of the page Example: Example Domain.
        description (Union[Unset, None, str]): The description of the page Example: This domain is for use in
            illustrative examples in documents. You may use this domain in literature without prior coordination or asking
            for permission..
        image (Union[Unset, None, str]): The image of the page Example: https://www.example.com/image.png.
    """

    id: Union[Unset, int] = UNSET
    url: Union[Unset, None, str] = UNSET
    title: Union[Unset, None, str] = UNSET
    description: Union[Unset, None, str] = UNSET
    image: Union[Unset, None, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        url = self.url
        title = self.title
        description = self.description
        image = self.image

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
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
        id = src_dict.get("id")

        url = src_dict.get("url")

        title = src_dict.get("title")

        description = src_dict.get("description")

        image = src_dict.get("image")

        page_metadata = cls(
            id=id,
            url=url,
            title=title,
            description=description,
            image=image,
        )

        page_metadata.additional_properties = src_dict
        return page_metadata

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
