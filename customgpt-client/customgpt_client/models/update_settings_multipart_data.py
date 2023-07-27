from io import BytesIO
from typing import Any, Dict, List, Tuple, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, File, FileJsonType, Unset

T = TypeVar("T", bound="UpdateSettingsMultipartData")


@attr.s(auto_attribs=True)
class UpdateSettingsMultipartData:
    """
    Attributes:
        chat_bot_avatar (Union[Unset, File]): Chatbot avatar Example: avatar.png.
        chat_bot_bg (Union[Unset, File]): Chatbot background Example: bg.png.
        default_prompt (Union[Unset, str]): Default prompt Example: How can I help you?.
        example_questions (Union[Unset, List[str]]): Example questions
        response_source (Union[Unset, str]): Response source Example: https://example.com.
        chatbot_msg_lang (Union[Unset, str]): Chatbot message language Example: en.
        chatbot_color (Union[Unset, str]): Chatbot color in hex format Example: #000000.
        persona_instructions (Union[Unset, None, str]): Role instructions for persona or null if persona must be delete
            Example: You are a custom chatbot assistant called CustomGPT, a friendly lawyer who answers questions based on
            the given context..
    """

    chat_bot_avatar: Union[Unset, File] = UNSET
    chat_bot_bg: Union[Unset, File] = UNSET
    default_prompt: Union[Unset, str] = UNSET
    example_questions: Union[Unset, List[str]] = UNSET
    response_source: Union[Unset, str] = UNSET
    chatbot_msg_lang: Union[Unset, str] = UNSET
    chatbot_color: Union[Unset, str] = UNSET
    persona_instructions: Union[Unset, None, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        chat_bot_avatar: Union[Unset, FileJsonType] = UNSET
        if not isinstance(self.chat_bot_avatar, Unset):
            chat_bot_avatar = self.chat_bot_avatar.to_tuple()

        chat_bot_bg: Union[Unset, FileJsonType] = UNSET
        if not isinstance(self.chat_bot_bg, Unset):
            chat_bot_bg = self.chat_bot_bg.to_tuple()

        default_prompt = self.default_prompt
        example_questions: Union[Unset, List[str]] = UNSET
        if not isinstance(self.example_questions, Unset):
            example_questions = self.example_questions

        response_source = self.response_source
        chatbot_msg_lang = self.chatbot_msg_lang
        chatbot_color = self.chatbot_color
        persona_instructions = self.persona_instructions

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if chat_bot_avatar is not UNSET:
            field_dict["chat_bot_avatar"] = chat_bot_avatar
        if chat_bot_bg is not UNSET:
            field_dict["chat_bot_bg"] = chat_bot_bg
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

    def to_multipart(self) -> Dict[str, Any]:
        chat_bot_avatar: Union[Unset, FileJsonType] = UNSET
        if not isinstance(self.chat_bot_avatar, Unset):
            chat_bot_avatar = self.chat_bot_avatar.to_tuple()

        chat_bot_bg: Union[Unset, FileJsonType] = UNSET
        if not isinstance(self.chat_bot_bg, Unset):
            chat_bot_bg = self.chat_bot_bg.to_tuple()

        default_prompt = (
            self.default_prompt
            if isinstance(self.default_prompt, Unset)
            else (None, str(self.default_prompt).encode(), "text/plain")
        )
        example_questions: Union[Unset, Tuple[None, bytes, str]] = UNSET
        if not isinstance(self.example_questions, Unset):
            self.example_questions
            example_questions = []
            for index, value in enumerate(self.example_questions):
                field_value = (None, str(value).encode(), "text/plain")
                example_questions.append(field_value)

        response_source = (
            self.response_source
            if isinstance(self.response_source, Unset)
            else (None, str(self.response_source).encode(), "text/plain")
        )
        chatbot_msg_lang = (
            self.chatbot_msg_lang
            if isinstance(self.chatbot_msg_lang, Unset)
            else (None, str(self.chatbot_msg_lang).encode(), "text/plain")
        )
        chatbot_color = (
            self.chatbot_color
            if isinstance(self.chatbot_color, Unset)
            else (None, str(self.chatbot_color).encode(), "text/plain")
        )
        persona_instructions = (
            self.persona_instructions
            if isinstance(self.persona_instructions, Unset)
            else (None, str(self.persona_instructions).encode(), "text/plain")
        )

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {key: (None, str(value).encode(), "text/plain") for key, value in self.additional_properties.items()}
        )
        field_dict.update({})
        if chat_bot_avatar is not UNSET:
            field_dict["chat_bot_avatar"] = chat_bot_avatar
        if chat_bot_bg is not UNSET:
            field_dict["chat_bot_bg"] = chat_bot_bg
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
        _chat_bot_avatar = src_dict.get("chat_bot_avatar")
        chat_bot_avatar: Union[Unset, File]
        if isinstance(_chat_bot_avatar, Unset):
            chat_bot_avatar = UNSET
        else:
            chat_bot_avatar = File(payload=BytesIO(_chat_bot_avatar))

        _chat_bot_bg = src_dict.get("chat_bot_bg")
        chat_bot_bg: Union[Unset, File]
        if isinstance(_chat_bot_bg, Unset):
            chat_bot_bg = UNSET
        else:
            chat_bot_bg = File(payload=BytesIO(_chat_bot_bg))

        default_prompt = src_dict.get("default_prompt")

        example_questions = cast(List[str], src_dict.get("example_questions"))

        response_source = src_dict.get("response_source")

        chatbot_msg_lang = src_dict.get("chatbot_msg_lang")

        chatbot_color = src_dict.get("chatbot_color")

        persona_instructions = src_dict.get("persona_instructions")

        update_settings_multipart_data = cls(
            chat_bot_avatar=chat_bot_avatar,
            chat_bot_bg=chat_bot_bg,
            default_prompt=default_prompt,
            example_questions=example_questions,
            response_source=response_source,
            chatbot_msg_lang=chatbot_msg_lang,
            chatbot_color=chatbot_color,
            persona_instructions=persona_instructions,
        )

        update_settings_multipart_data.additional_properties = src_dict
        return update_settings_multipart_data

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
