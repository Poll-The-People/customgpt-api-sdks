from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.send_message_to_conversation_response_401_status import SendMessageToConversationResponse401Status
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.send_message_to_conversation_response_401_data import SendMessageToConversationResponse401Data


T = TypeVar("T", bound="SendMessageToConversationResponse401")


@attr.s(auto_attribs=True)
class SendMessageToConversationResponse401:
    """
    Attributes:
        status (Union[Unset, SendMessageToConversationResponse401Status]): The status of the response Example: error.
        url (Union[Unset, str]): The URL of the request Example: https://app.customgpt.ai/api/v1/projects/1.
        data (Union[Unset, SendMessageToConversationResponse401Data]):
    """

    status: Union[Unset, SendMessageToConversationResponse401Status] = UNSET
    url: Union[Unset, str] = UNSET
    data: Union[Unset, "SendMessageToConversationResponse401Data"] = UNSET
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
        from ..models.send_message_to_conversation_response_401_data import SendMessageToConversationResponse401Data

        _status = src_dict.get("status")
        status: Union[Unset, SendMessageToConversationResponse401Status]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = SendMessageToConversationResponse401Status(_status)

        url = src_dict.get("url")

        _data = src_dict.get("data")
        data: Union[Unset, SendMessageToConversationResponse401Data]
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = SendMessageToConversationResponse401Data.from_dict(_data)

        send_message_to_conversation_response_401 = cls(
            status=status,
            url=url,
            data=data,
        )

        send_message_to_conversation_response_401.additional_properties = src_dict
        return send_message_to_conversation_response_401

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
