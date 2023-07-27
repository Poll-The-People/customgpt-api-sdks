from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.get_settings_response_200_data_response_source import GetSettingsResponse200DataResponseSource
from ..types import UNSET, Unset

T = TypeVar("T", bound="GetSettingsResponse200Data")


@attr.s(auto_attribs=True)
class GetSettingsResponse200Data:
    """
    Attributes:
        chatbot_avatar (Union[Unset, str]): The chatbot avatar Example: https://example.com/chatbot_avatar.png.
        chatbot_background (Union[Unset, str]): The chatbot background Example:
            https://example.com/chatbot_background.png.
        default_prompt (Union[Unset, str]): The default prompt Example: How can I help you?.
        example_questions (Union[Unset, List[str]]): The example questions Example: ['How do I get started?'].
        response_source (Union[Unset, GetSettingsResponse200DataResponseSource]): The response source Example:
            https://example.com/response_source.json.
        chatbot_msg_lang (Union[Unset, str]): The chatbot message language Example: en.
        chatbot_color (Union[Unset, str]): The chatbot color in hex format Example: #000000.
        persona_instructions (Union[Unset, None, str]): Role instructions for persona or null if persona must be delete
            Example: You are a custom chatbot assistant called CustomGPT, a friendly lawyer who answers questions based on
            the given context..
    """

    chatbot_avatar: Union[Unset, str] = UNSET
    chatbot_background: Union[Unset, str] = UNSET
    default_prompt: Union[Unset, str] = UNSET
    example_questions: Union[Unset, List[str]] = UNSET
    response_source: Union[Unset, GetSettingsResponse200DataResponseSource] = UNSET
    chatbot_msg_lang: Union[Unset, str] = UNSET
    chatbot_color: Union[Unset, str] = UNSET
    persona_instructions: Union[Unset, None, str] = UNSET
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
        chatbot_color = self.chatbot_color
        persona_instructions = self.persona_instructions

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
        if chatbot_color is not UNSET:
            field_dict["chatbot_color"] = chatbot_color
        if persona_instructions is not UNSET:
            field_dict["persona_instructions"] = persona_instructions

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        chatbot_avatar = src_dict.get("chatbot_avatar")

        chatbot_background = src_dict.get("chatbot_background")

        default_prompt = src_dict.get("default_prompt")

        example_questions = cast(List[str], src_dict.get("example_questions"))

        _response_source = src_dict.get("response_source")
        response_source: Union[Unset, GetSettingsResponse200DataResponseSource]
        if isinstance(_response_source, Unset):
            response_source = UNSET
        else:
            response_source = GetSettingsResponse200DataResponseSource(_response_source)

        chatbot_msg_lang = src_dict.get("chatbot_msg_lang")

        chatbot_color = src_dict.get("chatbot_color")

        persona_instructions = src_dict.get("persona_instructions")

        get_settings_response_200_data = cls(
            chatbot_avatar=chatbot_avatar,
            chatbot_background=chatbot_background,
            default_prompt=default_prompt,
            example_questions=example_questions,
            response_source=response_source,
            chatbot_msg_lang=chatbot_msg_lang,
            chatbot_color=chatbot_color,
            persona_instructions=persona_instructions,
        )

        get_settings_response_200_data.additional_properties = src_dict
        return get_settings_response_200_data

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
