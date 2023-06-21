from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.create_project_conversation_response_404_status import CreateProjectConversationResponse404Status
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_project_conversation_response_404_data import CreateProjectConversationResponse404Data


T = TypeVar("T", bound="CreateProjectConversationResponse404")


@attr.s(auto_attribs=True)
class CreateProjectConversationResponse404:
    """
    Attributes:
        status (Union[Unset, CreateProjectConversationResponse404Status]): The status of the response Example: error.
        url (Union[Unset, str]): The URL of the request Example: https://app.customgpt.ai/api/v1/projects/1.
        data (Union[Unset, CreateProjectConversationResponse404Data]):
    """

    status: Union[Unset, CreateProjectConversationResponse404Status] = UNSET
    url: Union[Unset, str] = UNSET
    data: Union[Unset, "CreateProjectConversationResponse404Data"] = UNSET
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
        from ..models.create_project_conversation_response_404_data import CreateProjectConversationResponse404Data

        d = src_dict.copy()
        _status = d.pop("status", UNSET)
        status: Union[Unset, CreateProjectConversationResponse404Status]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = CreateProjectConversationResponse404Status(_status)

        url = d.pop("url", UNSET)

        _data = d.pop("data", UNSET)
        data: Union[Unset, CreateProjectConversationResponse404Data]
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = CreateProjectConversationResponse404Data.from_dict(_data)

        create_project_conversation_response_404 = cls(
            status=status,
            url=url,
            data=data,
        )

        create_project_conversation_response_404.additional_properties = d
        return create_project_conversation_response_404

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
