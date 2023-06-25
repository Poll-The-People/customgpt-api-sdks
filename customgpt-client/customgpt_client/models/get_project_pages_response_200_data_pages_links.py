from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetProjectPagesResponse200DataPagesLinks")


@attr.s(auto_attribs=True)
class GetProjectPagesResponse200DataPagesLinks:
    """
    Attributes:
        first (Union[Unset, str]): The first page url Example: https://app.customgpt.ai/api/v1/users?page=1.
        last (Union[Unset, str]): The last page url Example: https://app.customgpt.ai/api/v1/users?page=1.
        prev (Union[Unset, str]): The previous page url Example: https://app.customgpt.ai/api/v1/users?page=1.
        next_ (Union[Unset, str]): The next page url Example: https://app.customgpt.ai/api/v1/users?page=1.
    """

    first: Union[Unset, str] = UNSET
    last: Union[Unset, str] = UNSET
    prev: Union[Unset, str] = UNSET
    next_: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        first = self.first
        last = self.last
        prev = self.prev
        next_ = self.next_

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if first is not UNSET:
            field_dict["first"] = first
        if last is not UNSET:
            field_dict["last"] = last
        if prev is not UNSET:
            field_dict["prev"] = prev
        if next_ is not UNSET:
            field_dict["next"] = next_

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        first = d.pop("first", UNSET)

        last = d.pop("last", UNSET)

        prev = d.pop("prev", UNSET)

        next_ = d.pop("next", UNSET)

        get_project_pages_response_200_data_pages_links = cls(
            first=first,
            last=last,
            prev=prev,
            next_=next_,
        )

        get_project_pages_response_200_data_pages_links.additional_properties = d
        return get_project_pages_response_200_data_pages_links

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
