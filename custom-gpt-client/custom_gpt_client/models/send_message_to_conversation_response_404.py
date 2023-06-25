from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.send_message_to_conversation_response_404_status import SendMessageToConversationResponse404Status
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.send_message_to_conversation_response_404_data import SendMessageToConversationResponse404Data


T = TypeVar("T", bound="SendMessageToConversationResponse404")


@attr.s(auto_attribs=True)
class SendMessageToConversationResponse404:
    """
    Attributes:
        status (Union[Unset, SendMessageToConversationResponse404Status]): The status of the response Example: error.
        url (Union[Unset, str]): The URL of the request Example: https://app.customgpt.ai/api/v1/projects/1.
        data (Union[Unset, SendMessageToConversationResponse404Data]):
    """

    status: Union[Unset, SendMessageToConversationResponse404Status] = UNSET
    url: Union[Unset, str] = UNSET
    data: Union[Unset, "SendMessageToConversationResponse404Data"] = UNSET
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
        from ..models.send_message_to_conversation_response_404_data import SendMessageToConversationResponse404Data

        d = src_dict.copy()
        _status = d.pop("status", UNSET)
        status: Union[Unset, SendMessageToConversationResponse404Status]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = SendMessageToConversationResponse404Status(_status)

        url = d.pop("url", UNSET)

        _data = d.pop("data", UNSET)
        data: Union[Unset, SendMessageToConversationResponse404Data]
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = SendMessageToConversationResponse404Data.from_dict(_data)

        send_message_to_conversation_response_404 = cls(
            status=status,
            url=url,
            data=data,
        )

        send_message_to_conversation_response_404.additional_properties = d
        return send_message_to_conversation_response_404

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