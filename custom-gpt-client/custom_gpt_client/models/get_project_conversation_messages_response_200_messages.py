from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_project_conversation_messages_response_200_messages_data_item import (
        GetProjectConversationMessagesResponse200MessagesDataItem,
    )
    from ..models.get_project_conversation_messages_response_200_messages_links import (
        GetProjectConversationMessagesResponse200MessagesLinks,
    )


T = TypeVar("T", bound="GetProjectConversationMessagesResponse200Messages")


@attr.s(auto_attribs=True)
class GetProjectConversationMessagesResponse200Messages:
    """
    Attributes:
        current_page (Union[Unset, int]): The current page number Example: 1.
        data (Union[Unset, List['GetProjectConversationMessagesResponse200MessagesDataItem']]):
        first_page_url (Union[Unset, str]): The first page url Example: https://app.customgpt.ai/api/v1/users?page=1.
        from_ (Union[Unset, int]): The first item number of the current page Example: 1.
        last_page (Union[Unset, int]): The last page number Example: 1.
        last_page_url (Union[Unset, str]): The last page url Example: https://app.customgpt.ai/api/v1/users?page=1.
        links (Union[Unset, GetProjectConversationMessagesResponse200MessagesLinks]):
        next_page_url (Union[Unset, str]): The next page url Example: https://app.customgpt.ai/api/v1/users?page=1.
        path (Union[Unset, str]): The current page url Example: https://app.customgpt.ai/api/v1/users?page=1.
        per_page (Union[Unset, int]): The number of items per page Example: 10.
        prev_page_url (Union[Unset, str]): The previous page url Example: https://app.customgpt.ai/api/v1/users?page=1.
        to (Union[Unset, int]): The last item number of the current page Example: 1.
        total (Union[Unset, int]): The total number of items Example: 1.
    """

    current_page: Union[Unset, int] = UNSET
    data: Union[Unset, List["GetProjectConversationMessagesResponse200MessagesDataItem"]] = UNSET
    first_page_url: Union[Unset, str] = UNSET
    from_: Union[Unset, int] = UNSET
    last_page: Union[Unset, int] = UNSET
    last_page_url: Union[Unset, str] = UNSET
    links: Union[Unset, "GetProjectConversationMessagesResponse200MessagesLinks"] = UNSET
    next_page_url: Union[Unset, str] = UNSET
    path: Union[Unset, str] = UNSET
    per_page: Union[Unset, int] = UNSET
    prev_page_url: Union[Unset, str] = UNSET
    to: Union[Unset, int] = UNSET
    total: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        current_page = self.current_page
        data: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.data, Unset):
            data = []
            for data_item_data in self.data:
                data_item = data_item_data.to_dict()

                data.append(data_item)

        first_page_url = self.first_page_url
        from_ = self.from_
        last_page = self.last_page
        last_page_url = self.last_page_url
        links: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.links, Unset):
            links = self.links.to_dict()

        next_page_url = self.next_page_url
        path = self.path
        per_page = self.per_page
        prev_page_url = self.prev_page_url
        to = self.to
        total = self.total

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if current_page is not UNSET:
            field_dict["current_page"] = current_page
        if data is not UNSET:
            for index, field_value in enumerate(data):
                field_dict[f"data[]{index}"] = field_value
        if first_page_url is not UNSET:
            field_dict["first_page_url"] = first_page_url
        if from_ is not UNSET:
            field_dict["from"] = from_
        if last_page is not UNSET:
            field_dict["last_page"] = last_page
        if last_page_url is not UNSET:
            field_dict["last_page_url"] = last_page_url
        if links is not UNSET:
            field_dict["links"] = links
        if next_page_url is not UNSET:
            field_dict["next_page_url"] = next_page_url
        if path is not UNSET:
            field_dict["path"] = path
        if per_page is not UNSET:
            field_dict["per_page"] = per_page
        if prev_page_url is not UNSET:
            field_dict["prev_page_url"] = prev_page_url
        if to is not UNSET:
            field_dict["to"] = to
        if total is not UNSET:
            field_dict["total"] = total

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.get_project_conversation_messages_response_200_messages_data_item import (
            GetProjectConversationMessagesResponse200MessagesDataItem,
        )
        from ..models.get_project_conversation_messages_response_200_messages_links import (
            GetProjectConversationMessagesResponse200MessagesLinks,
        )

        d = src_dict.copy()
        current_page = d.pop("current_page", UNSET)

        data = []
        _data = d.pop("data", UNSET)
        for data_item_data in _data or []:
            data_item = GetProjectConversationMessagesResponse200MessagesDataItem.from_dict(data_item_data)

            data.append(data_item)

        first_page_url = d.pop("first_page_url", UNSET)

        from_ = d.pop("from", UNSET)

        last_page = d.pop("last_page", UNSET)

        last_page_url = d.pop("last_page_url", UNSET)

        _links = d.pop("links", UNSET)
        links: Union[Unset, GetProjectConversationMessagesResponse200MessagesLinks]
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = GetProjectConversationMessagesResponse200MessagesLinks.from_dict(_links)

        next_page_url = d.pop("next_page_url", UNSET)

        path = d.pop("path", UNSET)

        per_page = d.pop("per_page", UNSET)

        prev_page_url = d.pop("prev_page_url", UNSET)

        to = d.pop("to", UNSET)

        total = d.pop("total", UNSET)

        get_project_conversation_messages_response_200_messages = cls(
            current_page=current_page,
            data=data,
            first_page_url=first_page_url,
            from_=from_,
            last_page=last_page,
            last_page_url=last_page_url,
            links=links,
            next_page_url=next_page_url,
            path=path,
            per_page=per_page,
            prev_page_url=prev_page_url,
            to=to,
            total=total,
        )

        get_project_conversation_messages_response_200_messages.additional_properties = d
        return get_project_conversation_messages_response_200_messages

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
