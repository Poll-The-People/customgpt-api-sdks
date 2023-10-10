from io import BytesIO
from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, File, FileJsonType, Unset

T = TypeVar("T", bound="GetSettingsResponse200Data")


@attr.s(auto_attribs=True)
class GetSettingsResponse200Data:
    """
    Attributes:
        chat_bot_avatar (Union[Unset, File]): This is the avatar that is shown in the bot response. You can make it a
            profile picture or your company logo. Example: avatar.png.
        chat_bot_bg (Union[Unset, File]): This is the background image shown in the bot conversations widget. You can
            change it to a company logo or background image. Example: bg.png.
        default_prompt (Union[Unset, str]): This is the default prompt shown to the user. You can customize this for
            your company or client. Example: How can I help you?.
        example_questions (Union[Unset, List[str]]): These are example questions shown to guide the bot users. You can
            create customized questions to suit your company or client needs.
        response_source (Union[Unset, str]): By default, we ask ChatGPT to use only your content in its response
            (recommended). If you wish ChatGPT to improvise and use its own knowledgebase as well, you can select "My
            Content + ChatGPT" Example: own_content.
        chatbot_msg_lang (Union[Unset, str]): By default, the chatbot messages like 'Ask Me Anything' are in English.
            You can customize this to your preferred language. Please note: This setting does not control what language
            ChatGPT responds in. That is controlled by the user's question. So a user asking in Portuguese, will most likely
            get a response from ChatGPT in Portuguese. Example: en.
        chatbot_color (Union[Unset, str]): Color of the chatbot in hex format Example: #000000.
        persona_instructions (Union[Unset, None, str]): [Advanced Users] Customize your chatbot behavior by adjusting
            the system parameter to control its personality traits  and role. Example: You are a custom chatbot assistant
            called CustomGPT, a friendly lawyer who answers questions based on the given context..
        citations_answer_source_label_msg (Union[Unset, None, str]): This is the message shown to indicate where the
            response came from. You can customize this message based on your business or language. Example: Where did this
            answer come from?.
        citations_sources_label_msg (Union[Unset, None, str]): This is the message shown for the Sources label.  You can
            customize this message based on your business or language. Example: Sources.
        hang_in_there_msg (Union[Unset, None, str]): This is the message shown when the bot is thinking and waiting to
            answer. You can customize this message based on your tone, personality or language. Example: Hang in there! I'm
            thinking...
        chatbot_siesta_msg (Union[Unset, None, str]): This is the message shown when the bot has encountered a problem
            or error. You can customize this message based on your tone, personality or language. Example: Oops! The chat
            bot is taking a siesta. This usually happens when OpenAI is down! Please try again later..
        is_loading_indicator_enabled (Union[Unset, None, bool]): Show animated loading indicator while waiting for a
            response from the chatbot Default: True. Example: True.
        enable_citations (Union[Unset, None, bool]): Each chatbot response shows an option for the user to see the
            sources/citations from your content from which the response was generated. Default: True. Example: True.
        citations_view_type (Union[Unset, None, GetSettingsResponse200DataCitationsViewType]): Control how citations are
            shown. By default, the user can initiate to see the citations. You can choose to have it "Auto Shown" or "Auto
            Hide" Default: GetSettingsResponse200DataCitationsViewType.USER. Example: user.
        no_answer_message (Union[Unset, None, str]): This is the message shown when the bot cannot answer. You can
            customize it to a message asking the user to contact customer support or leave their email / phone. Example:
            Sorry, I don't have an answer for that..
        ending_message (Union[Unset, None, str]): You can instruct ChatGPT to end every response with some text like
            asking "Please email us for further support" (Not recommended for most use cases) Example: Please email us for
            further support.
        remove_branding (Union[Unset, None, bool]): Controls what branding is shown at the bottom of the chatbot.
    """

    chat_bot_avatar: Union[Unset, File] = UNSET
    chat_bot_bg: Union[Unset, File] = UNSET
    default_prompt: Union[Unset, str] = UNSET
    example_questions: Union[Unset, List[str]] = UNSET
    response_source: Union[Unset, str] = UNSET
    chatbot_msg_lang: Union[Unset, str] = UNSET
    chatbot_color: Union[Unset, str] = UNSET
    persona_instructions: Union[Unset, None, str] = UNSET
    citations_answer_source_label_msg: Union[Unset, None, str] = UNSET
    citations_sources_label_msg: Union[Unset, None, str] = UNSET
    hang_in_there_msg: Union[Unset, None, str] = UNSET
    chatbot_siesta_msg: Union[Unset, None, str] = UNSET
    is_loading_indicator_enabled: Union[Unset, None, bool] = True
    enable_citations: Union[Unset, None, bool] = True
    citations_view_type: Union[Unset, str] = Unset
    no_answer_message: Union[Unset, None, str] = UNSET
    ending_message: Union[Unset, None, str] = UNSET
    remove_branding: Union[Unset, None, bool] = False
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
        citations_answer_source_label_msg = self.citations_answer_source_label_msg
        citations_sources_label_msg = self.citations_sources_label_msg
        hang_in_there_msg = self.hang_in_there_msg
        chatbot_siesta_msg = self.chatbot_siesta_msg
        is_loading_indicator_enabled = self.is_loading_indicator_enabled
        enable_citations = self.enable_citations
        citations_view_type: Union[Unset, None, str] = UNSET
        if not isinstance(self.citations_view_type, Unset):
            citations_view_type = self.citations_view_type.value if self.citations_view_type else None

        no_answer_message = self.no_answer_message
        ending_message = self.ending_message
        remove_branding = self.remove_branding

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
                field_dict[f"example_questions[]"] = field_value
        if response_source is not UNSET:
            field_dict["response_source"] = response_source
        if chatbot_msg_lang is not UNSET:
            field_dict["chatbot_msg_lang"] = chatbot_msg_lang
        if chatbot_color is not UNSET:
            field_dict["chatbot_color"] = chatbot_color
        if persona_instructions is not UNSET:
            field_dict["persona_instructions"] = persona_instructions
        if citations_answer_source_label_msg is not UNSET:
            field_dict["citations_answer_source_label_msg"] = citations_answer_source_label_msg
        if citations_sources_label_msg is not UNSET:
            field_dict["citations_sources_label_msg"] = citations_sources_label_msg
        if hang_in_there_msg is not UNSET:
            field_dict["hang_in_there_msg"] = hang_in_there_msg
        if chatbot_siesta_msg is not UNSET:
            field_dict["chatbot_siesta_msg"] = chatbot_siesta_msg
        if is_loading_indicator_enabled is not UNSET:
            field_dict["is_loading_indicator_enabled"] = is_loading_indicator_enabled
        if enable_citations is not UNSET:
            field_dict["enable_citations"] = enable_citations
        if citations_view_type is not UNSET:
            field_dict["citations_view_type"] = citations_view_type
        if no_answer_message is not UNSET:
            field_dict["no_answer_message"] = no_answer_message
        if ending_message is not UNSET:
            field_dict["ending_message"] = ending_message
        if remove_branding is not UNSET:
            field_dict["remove_branding"] = remove_branding

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

        citations_answer_source_label_msg = src_dict.get("citations_answer_source_label_msg")

        citations_sources_label_msg = src_dict.get("citations_sources_label_msg")

        hang_in_there_msg = src_dict.get("hang_in_there_msg")

        chatbot_siesta_msg = src_dict.get("chatbot_siesta_msg")

        is_loading_indicator_enabled = src_dict.get("is_loading_indicator_enabled")

        enable_citations = src_dict.get("enable_citations")

        citations_view_type = src_dict.get("citations_view_type")

        no_answer_message = src_dict.get("no_answer_message")

        ending_message = src_dict.get("ending_message")

        remove_branding = src_dict.get("remove_branding")

        get_settings_response_200_data = cls(
            chat_bot_avatar=chat_bot_avatar,
            chat_bot_bg=chat_bot_bg,
            default_prompt=default_prompt,
            example_questions=example_questions,
            response_source=response_source,
            chatbot_msg_lang=chatbot_msg_lang,
            chatbot_color=chatbot_color,
            persona_instructions=persona_instructions,
            citations_answer_source_label_msg=citations_answer_source_label_msg,
            citations_sources_label_msg=citations_sources_label_msg,
            hang_in_there_msg=hang_in_there_msg,
            chatbot_siesta_msg=chatbot_siesta_msg,
            is_loading_indicator_enabled=is_loading_indicator_enabled,
            enable_citations=enable_citations,
            citations_view_type=citations_view_type,
            no_answer_message=no_answer_message,
            ending_message=ending_message,
            remove_branding=remove_branding,
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
