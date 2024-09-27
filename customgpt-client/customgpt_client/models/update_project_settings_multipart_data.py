from io import BytesIO
from typing import Any, Dict, List, Tuple, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, File, FileJsonType, Unset

T = TypeVar("T", bound="UpdateProjectSettingsMultipartData")


@attr.s(auto_attribs=True)
class UpdateProjectSettingsMultipartData:
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
        response_source (Union[Unset, UpdateProjectSettingsMultipartDataResponseSource]): By default, we ask ChatGPT to
            use only your content in its response (recommended). If you wish ChatGPT to improvise and use its own
            knowledgebase as well, you can select "My Content + ChatGPT" Example: own_content.
        chatbot_msg_lang (Union[Unset, UpdateProjectSettingsMultipartDataChatbotMsgLang]): By default, the chatbot
            messages like 'Ask Me Anything' are in English. You can customize this to your preferred language. Please note:
            This setting does not control what language ChatGPT responds in. That is controlled by the user's question. So a
            user asking in Portuguese, will most likely get a response from ChatGPT in Portuguese. Example: en.
        chatbot_color (Union[Unset, str]): Color of the chatbot in hex format Example: #000000.
        chatbot_toolbar_color (Union[Unset, str]): Color of the chatbot toolbar in hex format Example: #000000.
        persona_instructions (Union[Unset, None, str]): Customize your chatbot behavior by adjusting the system
            parameter to control its personality traits  and role. Example: You are a custom chatbot assistant called
            CustomGPT.ai, a friendly lawyer who answers questions based on the given context..
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
        enable_citations (Union[Unset, None, UpdateProjectSettingsMultipartDataEnableCitations]): Each chatbot response
            shows an option for the user to see the sources/citations from your content from which the response was
            generated. Default: UpdateProjectSettingsMultipartDataEnableCitations.VALUE_3. Example: 3.
        enable_feedbacks (Union[Unset, None, bool]): Each chatbot response shows an thumbs up/down for the user to left
            own feedback. Default: True. Example: True.
        citations_view_type (Union[Unset, None, UpdateProjectSettingsMultipartDataCitationsViewType]): Control how
            citations are shown. By default, the user can initiate to see the citations. You can choose to have it "Auto
            Shown" or "Auto Hide" Default: UpdateProjectSettingsMultipartDataCitationsViewType.USER. Example: user.
        no_answer_message (Union[Unset, None, str]): This is the message shown when the bot cannot answer. You can
            customize it to a message asking the user to contact customer support or leave their email / phone. Default:
            "I'm sorry, I don't know the answer". Example: Sorry, I don't have an answer for that..
        ending_message (Union[Unset, None, str]): You can instruct ChatGPT to end every response with some text like
            asking "Please email us for further support" (Not recommended for most use cases) Example: Please email us for
            further support.
        remove_branding (Union[Unset, None, bool]): Controls what branding is shown at the bottom of the chatbot.
        enable_recaptcha_for_public_chatbots (Union[Unset, None, bool]): Should we check messages from guests with
            Recaptcha when your chatbot is publicly available (i.e. shared or embedded).
        chatbot_model (Union[Unset, None, UpdateProjectSettingsMultipartDataChatbotModel]): This is the model used by
            the chatbot. You can choose a different model to suit your needs. Example: gpt-4.
        is_selling_enabled (Union[Unset, None, bool]): Enable selling of chatbot for monetization
    """

    chat_bot_avatar: Union[Unset, File] = UNSET
    chat_bot_bg: Union[Unset, File] = UNSET
    default_prompt: Union[Unset, str] = UNSET
    example_questions: Union[Unset, List[str]] = UNSET
    response_source: Union[Unset, str] = UNSET
    chatbot_msg_lang: Union[Unset, str] = UNSET
    chatbot_color: Union[Unset, str] = UNSET
    chatbot_toolbar_color: Union[Unset, str] = UNSET
    persona_instructions: Union[Unset, None, str] = UNSET
    citations_answer_source_label_msg: Union[Unset, None, str] = UNSET
    citations_sources_label_msg: Union[Unset, None, str] = UNSET
    hang_in_there_msg: Union[Unset, None, str] = UNSET
    chatbot_siesta_msg: Union[Unset, None, str] = UNSET
    is_loading_indicator_enabled: Union[Unset, None, bool] = True
    enable_citations: Union[Unset, str] = UNSET
    enable_feedbacks: Union[Unset, None, bool] = True
    citations_view_type: Union[Unset, str] = UNSET
    no_answer_message: Union[Unset, None, str] = "I'm sorry, I don't know the answer"
    ending_message: Union[Unset, None, str] = UNSET
    remove_branding: Union[Unset, None, bool] = False
    enable_recaptcha_for_public_chatbots: Union[Unset, None, bool] = False
    chatbot_model: Union[Unset, str] = UNSET
    is_selling_enabled: Union[Unset, None, bool] = False
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

        response_source: Union[Unset, str] = UNSET
        if not isinstance(self.response_source, Unset):
            response_source = self.response_source

        chatbot_msg_lang: Union[Unset, str] = UNSET
        if not isinstance(self.chatbot_msg_lang, Unset):
            chatbot_msg_lang = self.chatbot_msg_lang

        chatbot_color = self.chatbot_color
        chatbot_toolbar_color = self.chatbot_toolbar_color
        persona_instructions = self.persona_instructions
        citations_answer_source_label_msg = self.citations_answer_source_label_msg
        citations_sources_label_msg = self.citations_sources_label_msg
        hang_in_there_msg = self.hang_in_there_msg
        chatbot_siesta_msg = self.chatbot_siesta_msg
        is_loading_indicator_enabled = True if self.is_loading_indicator_enabled else False

        enable_citations: Union[Unset, None, int] = UNSET
        if not isinstance(self.enable_citations, Unset):
            enable_citations = self.enable_citations if self.enable_citations else None

        enable_feedbacks = True if self.enable_feedbacks else False

        citations_view_type: Union[Unset, None, str] = UNSET
        if not isinstance(self.citations_view_type, Unset):
            citations_view_type = self.citations_view_type if self.citations_view_type else None

        no_answer_message = self.no_answer_message
        ending_message = self.ending_message
        remove_branding = True if self.remove_branding else False

        enable_recaptcha_for_public_chatbots = True if self.enable_recaptcha_for_public_chatbots else False

        chatbot_model: Union[Unset, None, str] = UNSET
        if not isinstance(self.chatbot_model, Unset):
            chatbot_model = self.chatbot_model if self.chatbot_model else None

        is_selling_enabled = True if self.is_selling_enabled else False

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
                field_dict[f"example_questions[{index}]"] = field_value
        if response_source is not UNSET:
            field_dict["response_source"] = response_source
        if chatbot_msg_lang is not UNSET:
            field_dict["chatbot_msg_lang"] = chatbot_msg_lang
        if chatbot_color is not UNSET:
            field_dict["chatbot_color"] = chatbot_color
        if chatbot_toolbar_color is not UNSET:
            field_dict["chatbot_toolbar_color"] = chatbot_toolbar_color
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
        if enable_feedbacks is not UNSET:
            field_dict["enable_feedbacks"] = enable_feedbacks
        if citations_view_type is not UNSET:
            field_dict["citations_view_type"] = citations_view_type
        if no_answer_message is not UNSET:
            field_dict["no_answer_message"] = no_answer_message
        if ending_message is not UNSET:
            field_dict["ending_message"] = ending_message
        if remove_branding is not UNSET:
            field_dict["remove_branding"] = remove_branding
        if enable_recaptcha_for_public_chatbots is not UNSET:
            field_dict["enable_recaptcha_for_public_chatbots"] = enable_recaptcha_for_public_chatbots
        if chatbot_model is not UNSET:
            field_dict["chatbot_model"] = chatbot_model
        if is_selling_enabled is not UNSET:
            field_dict["is_selling_enabled"] = is_selling_enabled

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

        response_source: Union[Unset, Tuple[None, bytes, str]] = UNSET
        if not isinstance(self.response_source, Unset):
            response_source = (None, str(self.response_source).encode(), "text/plain")

        chatbot_msg_lang: Union[Unset, Tuple[None, bytes, str]] = UNSET
        if not isinstance(self.chatbot_msg_lang, Unset):
            chatbot_msg_lang = (None, str(self.chatbot_msg_lang).encode(), "text/plain")

        chatbot_color = (
            self.chatbot_color
            if isinstance(self.chatbot_color, Unset)
            else (None, str(self.chatbot_color).encode(), "text/plain")
        )
        chatbot_toolbar_color = (
            self.chatbot_toolbar_color
            if isinstance(self.chatbot_toolbar_color, Unset)
            else (None, str(self.chatbot_toolbar_color).encode(), "text/plain")
        )
        persona_instructions = (
            self.persona_instructions
            if isinstance(self.persona_instructions, Unset)
            else (None, str(self.persona_instructions).encode(), "text/plain")
        )
        citations_answer_source_label_msg = (
            self.citations_answer_source_label_msg
            if isinstance(self.citations_answer_source_label_msg, Unset)
            else (None, str(self.citations_answer_source_label_msg).encode(), "text/plain")
        )
        citations_sources_label_msg = (
            self.citations_sources_label_msg
            if isinstance(self.citations_sources_label_msg, Unset)
            else (None, str(self.citations_sources_label_msg).encode(), "text/plain")
        )
        hang_in_there_msg = (
            self.hang_in_there_msg
            if isinstance(self.hang_in_there_msg, Unset)
            else (None, str(self.hang_in_there_msg).encode(), "text/plain")
        )
        chatbot_siesta_msg = (
            self.chatbot_siesta_msg
            if isinstance(self.chatbot_siesta_msg, Unset)
            else (None, str(self.chatbot_siesta_msg).encode(), "text/plain")
        )
        is_loading_indicator_enabled = (
            self.is_loading_indicator_enabled
            if isinstance(self.is_loading_indicator_enabled, Unset)
            else (None, str(self.is_loading_indicator_enabled).lower().encode(), "text/plain")
        )

        enable_citations: Union[Unset, Tuple[None, bytes, str]] = UNSET
        if not isinstance(self.enable_citations, Unset):
            enable_citations = (
                (None, str(self.enable_citations).encode(), "text/plain") if self.enable_citations else None
            )

        enable_feedbacks = (
            self.enable_feedbacks
            if isinstance(self.enable_feedbacks, Unset)
            else (None, str(self.enable_feedbacks).lower().encode(), "text/plain")
        )

        citations_view_type: Union[Unset, Tuple[None, bytes, str]] = UNSET
        if not isinstance(self.citations_view_type, Unset):
            citations_view_type = (
                (None, str(self.citations_view_type).encode(), "text/plain") if self.citations_view_type else None
            )

        no_answer_message = (
            self.no_answer_message
            if isinstance(self.no_answer_message, Unset)
            else (None, str(self.no_answer_message).encode(), "text/plain")
        )
        ending_message = (
            self.ending_message
            if isinstance(self.ending_message, Unset)
            else (None, str(self.ending_message).encode(), "text/plain")
        )
        remove_branding = (
            self.remove_branding
            if isinstance(self.remove_branding, Unset)
            else (None, str(self.remove_branding).lower().encode(), "text/plain")
        )

        enable_recaptcha_for_public_chatbots = (
            self.enable_recaptcha_for_public_chatbots
            if isinstance(self.enable_recaptcha_for_public_chatbots, Unset)
            else (None, str(self.enable_recaptcha_for_public_chatbots).lower().encode(), "text/plain")
        )

        chatbot_model: Union[Unset, Tuple[None, bytes, str]] = UNSET
        if not isinstance(self.chatbot_model, Unset):
            chatbot_model = (None, str(self.chatbot_model).encode(), "text/plain") if self.chatbot_model else None

        is_selling_enabled = (
            self.is_selling_enabled
            if isinstance(self.is_selling_enabled, Unset)
            else (None, str(self.is_selling_enabled).lower().encode(), "text/plain")
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
                field_dict[f"example_questions[{index}]"] = field_value
        if response_source is not UNSET:
            field_dict["response_source"] = response_source
        if chatbot_msg_lang is not UNSET:
            field_dict["chatbot_msg_lang"] = chatbot_msg_lang
        if chatbot_color is not UNSET:
            field_dict["chatbot_color"] = chatbot_color
        if chatbot_toolbar_color is not UNSET:
            field_dict["chatbot_toolbar_color"] = chatbot_toolbar_color
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
        if enable_feedbacks is not UNSET:
            field_dict["enable_feedbacks"] = enable_feedbacks
        if citations_view_type is not UNSET:
            field_dict["citations_view_type"] = citations_view_type
        if no_answer_message is not UNSET:
            field_dict["no_answer_message"] = no_answer_message
        if ending_message is not UNSET:
            field_dict["ending_message"] = ending_message
        if remove_branding is not UNSET:
            field_dict["remove_branding"] = remove_branding
        if enable_recaptcha_for_public_chatbots is not UNSET:
            field_dict["enable_recaptcha_for_public_chatbots"] = enable_recaptcha_for_public_chatbots
        if chatbot_model is not UNSET:
            field_dict["chatbot_model"] = chatbot_model
        if is_selling_enabled is not UNSET:
            field_dict["is_selling_enabled"] = is_selling_enabled

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

        chatbot_toolbar_color = src_dict.get("chatbot_toolbar_color")

        persona_instructions = src_dict.get("persona_instructions")

        citations_answer_source_label_msg = src_dict.get("citations_answer_source_label_msg")

        citations_sources_label_msg = src_dict.get("citations_sources_label_msg")

        hang_in_there_msg = src_dict.get("hang_in_there_msg")

        chatbot_siesta_msg = src_dict.get("chatbot_siesta_msg")

        is_loading_indicator_enabled = src_dict.get("is_loading_indicator_enabled")

        enable_citations = src_dict.get("enable_citations")

        enable_feedbacks = src_dict.get("enable_feedbacks")

        citations_view_type = src_dict.get("citations_view_type")

        no_answer_message = src_dict.get("no_answer_message")

        ending_message = src_dict.get("ending_message")

        remove_branding = src_dict.get("remove_branding")

        enable_recaptcha_for_public_chatbots = src_dict.get("enable_recaptcha_for_public_chatbots")

        chatbot_model = src_dict.get("chatbot_model")

        is_selling_enabled = src_dict.get("is_selling_enabled")

        update_project_settings_multipart_data = cls(
            chat_bot_avatar=chat_bot_avatar,
            chat_bot_bg=chat_bot_bg,
            default_prompt=default_prompt,
            example_questions=example_questions,
            response_source=response_source,
            chatbot_msg_lang=chatbot_msg_lang,
            chatbot_color=chatbot_color,
            chatbot_toolbar_color=chatbot_toolbar_color,
            persona_instructions=persona_instructions,
            citations_answer_source_label_msg=citations_answer_source_label_msg,
            citations_sources_label_msg=citations_sources_label_msg,
            hang_in_there_msg=hang_in_there_msg,
            chatbot_siesta_msg=chatbot_siesta_msg,
            is_loading_indicator_enabled=is_loading_indicator_enabled,
            enable_citations=enable_citations,
            enable_feedbacks=enable_feedbacks,
            citations_view_type=citations_view_type,
            no_answer_message=no_answer_message,
            ending_message=ending_message,
            remove_branding=remove_branding,
            enable_recaptcha_for_public_chatbots=enable_recaptcha_for_public_chatbots,
            chatbot_model=chatbot_model,
            is_selling_enabled=is_selling_enabled,
        )

        update_project_settings_multipart_data.additional_properties = src_dict
        return update_project_settings_multipart_data

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
