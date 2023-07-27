from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="OpenGraphCache")


@attr.s(auto_attribs=True)
class OpenGraphCache:
    """
    Attributes:
        page_url (Union[Unset, str]): The URL of the page Example: https://www.example.com.
        title (Union[Unset, str]): The title of the page Example: Example Domain.
        description (Union[Unset, str]): The description of the page Example: This domain is for use in illustrative
            examples in documents. You may use this domain in literature without prior coordination or asking for
            permission..
        image (Union[Unset, str]): The image of the page Example: https://www.example.com/image.png.
        image_width (Union[Unset, int]): The width of the image of the page Example: 1200.
        image_height (Union[Unset, int]): The height of the image of the page Example: 630.
        url (Union[Unset, str]): The URL of the page Example: https://www.example.com.
        favicon (Union[Unset, str]): The favicon of the page Example: https://www.example.com/favicon.ico.
        site_name (Union[Unset, str]): The site name of the page Example: Example Domain.
    """

    page_url: Union[Unset, str] = UNSET
    title: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    image: Union[Unset, str] = UNSET
    image_width: Union[Unset, int] = UNSET
    image_height: Union[Unset, int] = UNSET
    url: Union[Unset, str] = UNSET
    favicon: Union[Unset, str] = UNSET
    site_name: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        page_url = self.page_url
        title = self.title
        description = self.description
        image = self.image
        image_width = self.image_width
        image_height = self.image_height
        url = self.url
        favicon = self.favicon
        site_name = self.site_name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if page_url is not UNSET:
            field_dict["page_url"] = page_url
        if title is not UNSET:
            field_dict["title"] = title
        if description is not UNSET:
            field_dict["description"] = description
        if image is not UNSET:
            field_dict["image"] = image
        if image_width is not UNSET:
            field_dict["image_width"] = image_width
        if image_height is not UNSET:
            field_dict["image_height"] = image_height
        if url is not UNSET:
            field_dict["url"] = url
        if favicon is not UNSET:
            field_dict["favicon"] = favicon
        if site_name is not UNSET:
            field_dict["site_name"] = site_name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        page_url = src_dict.get("page_url")

        title = src_dict.get("title")

        description = src_dict.get("description")

        image = src_dict.get("image")

        image_width = src_dict.get("image_width")

        image_height = src_dict.get("image_height")

        url = src_dict.get("url")

        favicon = src_dict.get("favicon")

        site_name = src_dict.get("site_name")

        open_graph_cache = cls(
            page_url=page_url,
            title=title,
            description=description,
            image=image,
            image_width=image_width,
            image_height=image_height,
            url=url,
            favicon=favicon,
            site_name=site_name,
        )

        open_graph_cache.additional_properties = src_dict
        return open_graph_cache

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
