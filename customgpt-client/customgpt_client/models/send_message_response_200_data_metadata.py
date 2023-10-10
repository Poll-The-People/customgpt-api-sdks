from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="SendMessageResponse200DataMetadata")


@attr.s(auto_attribs=True)
class SendMessageResponse200DataMetadata:
    """
    Example:
        {'user_ip': '127.0.0.1', 'user_agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36
            (KHTML, like Gecko)', 'external_id': 'ext_id_1234567890', 'request_source': 'web'}

    Attributes:
        user_ip (Union[Unset, str]): The IP address of the user. Example: 127.0.0.1.
        user_agent (Union[Unset, str]): The user agent of the user. Example: Mozilla/5.0 (Macintosh; Intel Mac OS X
            10_15_7) AppleWebKit/537.36 (KHTML, like Gecko).
        external_id (Union[Unset, str]): The external ID of the prompt history. Example: ext_id_1234567890.
        request_source (Union[Unset, str]): The source of the request. Example: web.
    """

    user_ip: Union[Unset, str] = UNSET
    user_agent: Union[Unset, str] = UNSET
    external_id: Union[Unset, str] = UNSET
    request_source: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        user_ip = self.user_ip
        user_agent = self.user_agent
        external_id = self.external_id
        request_source = self.request_source

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if user_ip is not UNSET:
            field_dict["user_ip"] = user_ip
        if user_agent is not UNSET:
            field_dict["user_agent"] = user_agent
        if external_id is not UNSET:
            field_dict["external_id"] = external_id
        if request_source is not UNSET:
            field_dict["request_source"] = request_source

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        user_ip = src_dict.get("user_ip")

        user_agent = src_dict.get("user_agent")

        external_id = src_dict.get("external_id")

        request_source = src_dict.get("request_source")

        send_message_response_200_data_metadata = cls(
            user_ip=user_ip,
            user_agent=user_agent,
            external_id=external_id,
            request_source=request_source,
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
