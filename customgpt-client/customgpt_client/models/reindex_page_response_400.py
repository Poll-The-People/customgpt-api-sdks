from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.reindex_page_response_400_status import ReindexPageResponse400Status
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.reindex_page_response_400_data import ReindexPageResponse400Data


T = TypeVar("T", bound="ReindexPageResponse400")


@attr.s(auto_attribs=True)
class ReindexPageResponse400:
    """
    Attributes:
        status (Union[Unset, ReindexPageResponse400Status]): The status of the response Example: error.
        url (Union[Unset, str]): The URL of the request Example: https://app.customgpt.ai/api/v1/projects/1.
        data (Union[Unset, ReindexPageResponse400Data]):
    """

    status: Union[Unset, ReindexPageResponse400Status] = UNSET
    url: Union[Unset, str] = UNSET
    data: Union[Unset, "ReindexPageResponse400Data"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        url = self.url
        data: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.data, Unset):
            data = self.data.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if status is not UNSET:
            field_dict["status"] = status
        if url is not UNSET:
            field_dict["url"] = url
        if data is not UNSET:
            field_dict["data"] = data

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.reindex_page_response_400_data import ReindexPageResponse400Data

        _status = src_dict.get("status")
        status: Union[Unset, ReindexPageResponse400Status]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = ReindexPageResponse400Status(_status)

        url = src_dict.get("url")

        _data = src_dict.get("data")
        data: Union[Unset, ReindexPageResponse400Data]
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = ReindexPageResponse400Data.from_dict(_data)

        reindex_page_response_400 = cls(
            status=status,
            url=url,
            data=data,
        )

        reindex_page_response_400.additional_properties = src_dict
        return reindex_page_response_400

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
