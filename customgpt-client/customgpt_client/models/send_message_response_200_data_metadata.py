from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="SendMessageResponse200DataMetadata")


@attr.s(auto_attribs=True)
class SendMessageResponse200DataMetadata:
    """
    Example:
        {'user_ip': '127.0.0.1', 'user_agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36
            (KHTML, like Gecko)'}

    Attributes:
        user_ip (Union[Unset, str]): The IP address of the user. Example: 127.0.0.1.
        user_agent (Union[Unset, str]): The user agent of the user. Example: Mozilla/5.0 (Macintosh; Intel Mac OS X
            10_15_7) AppleWebKit/537.36 (KHTML, like Gecko).
    """

    user_ip: Union[Unset, str] = UNSET
    user_agent: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        user_ip = self.user_ip
        user_agent = self.user_agent

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if user_ip is not UNSET:
            field_dict["user_ip"] = user_ip
        if user_agent is not UNSET:
            field_dict["user_agent"] = user_agent

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        user_ip = src_dict.get("user_ip")

        user_agent = src_dict.get("user_agent")

        send_message_response_200_data_metadata = cls(
            user_ip=user_ip,
            user_agent=user_agent,
        )

        send_message_response_200_data_metadata.additional_properties = src_dict
        return send_message_response_200_data_metadata

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
