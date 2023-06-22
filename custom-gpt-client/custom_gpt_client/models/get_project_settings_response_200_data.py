from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.get_project_settings_response_200_data_response_source import (
    GetProjectSettingsResponse200DataResponseSource,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="GetProjectSettingsResponse200Data")


@attr.s(auto_attribs=True)
class GetProjectSettingsResponse200Data:
    """
    Attributes:
        chatbot_avatar (Union[Unset, str]): The chatbot avatar Example: https://example.com/chatbot_avatar.png.
        chatbot_background (Union[Unset, str]): The chatbot background Example:
            https://example.com/chatbot_background.png.
        default_prompt (Union[Unset, str]): The default prompt Example: How can I help you?.
        example_questions (Union[Unset, List[str]]): The example questions Example: ['How do I get started?'].
        response_source (Union[Unset, GetProjectSettingsResponse200DataResponseSource]): The response source Example:
            https://example.com/response_source.json.
        chatbot_msg_lang (Union[Unset, str]): The chatbot message language Example: en.
    """

    chatbot_avatar: Union[Unset, str] = UNSET
    chatbot_background: Union[Unset, str] = UNSET
    default_prompt: Union[Unset, str] = UNSET
    example_questions: Union[Unset, List[str]] = UNSET
    response_source: Union[Unset, GetProjectSettingsResponse200DataResponseSource] = UNSET
    chatbot_msg_lang: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        chatbot_avatar = self.chatbot_avatar
        chatbot_background = self.chatbot_background
        default_prompt = self.default_prompt
        example_questions: Union[Unset, List[str]] = UNSET
        if not isinstance(self.example_questions, Unset):
            example_questions = self.example_questions

        response_source: Union[Unset, str] = UNSET
        if not isinstance(self.response_source, Unset):
            response_source = self.response_source.value

        chatbot_msg_lang = self.chatbot_msg_lang

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if chatbot_avatar is not UNSET:
            field_dict["chatbot_avatar"] = chatbot_avatar
        if chatbot_background is not UNSET:
            field_dict["chatbot_background"] = chatbot_background
        if default_prompt is not UNSET:
            field_dict["default_prompt"] = default_prompt
        if example_questions is not UNSET:
            for index, field_value in enumerate(example_questions):
                field_dict[f"example_questions[]{index}"] = field_value
        if response_source is not UNSET:
            field_dict["response_source"] = response_source
        if chatbot_msg_lang is not UNSET:
            field_dict["chatbot_msg_lang"] = chatbot_msg_lang

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        chatbot_avatar = d.pop("chatbot_avatar", UNSET)

        chatbot_background = d.pop("chatbot_background", UNSET)

        default_prompt = d.pop("default_prompt", UNSET)

        example_questions = cast(List[str], d.pop("example_questions", UNSET))

        _response_source = d.pop("response_source", UNSET)
        response_source: Union[Unset, GetProjectSettingsResponse200DataResponseSource]
        if isinstance(_response_source, Unset):
            response_source = UNSET
        else:
            response_source = GetProjectSettingsResponse200DataResponseSource(_response_source)

        chatbot_msg_lang = d.pop("chatbot_msg_lang", UNSET)

        get_project_settings_response_200_data = cls(
            chatbot_avatar=chatbot_avatar,
            chatbot_background=chatbot_background,
            default_prompt=default_prompt,
            example_questions=example_questions,
            response_source=response_source,
            chatbot_msg_lang=chatbot_msg_lang,
        )

        get_project_settings_response_200_data.additional_properties = d
        return get_project_settings_response_200_data

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
