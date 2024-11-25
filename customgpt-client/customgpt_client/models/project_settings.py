from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ProjectSettings")


@attr.s(auto_attribs=True)
class ProjectSettings:
    """
    Attributes:
        chatbot_avatar (Union[Unset, str]): This is the avatar that is shown in the bot response. You can make it a
            profile picture or your company logo. Example: https://example.com/chatbot_avatar.png.
        chatbot_background (Union[Unset, str]): This is the background image shown in the bot conversations widget. You
            can change it to a company logo or background image. Example: https://example.com/chatbot_background.png.
        default_prompt (Union[Unset, str]): This is the default prompt shown to the user. You can customize this for
            your company or client. Example: How can I help you?.
        example_questions (Union[Unset, List[str]]): These are example questions shown to guide the bot users. You can
            create customized questions to suit your company or client needs. Example: ['How do I get started?'].
        response_source (Union[Unset, ProjectSettingsResponseSource]): By default, we ask ChatGPT to use only your
            content in its response (recommended). If you wish ChatGPT to improvise and use its own knowledgebase as well,
            you can select "My Content + ChatGPT" Example: own_content.
        chatbot_msg_lang (Union[Unset, str]): By default, the chatbot messages like 'Ask Me Anything' are in English.
            You can customize this to your preferred language. Please note: This setting does not control what language
            ChatGPT responds in. That is controlled by the user's question. So a user asking in Portuguese, will most likely
            get a response from ChatGPT in Portuguese. Example: en.
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
        enable_citations (Union[Unset, None, ProjectSettingsEnableCitations]): Each chatbot response shows an option for
            the user to see the sources/citations from your content from which the response was generated. Default:
            ProjectSettingsEnableCitations.VALUE_3. Example: 3.
        enable_feedbacks (Union[Unset, None, bool]): Each chatbot response shows an thumbs up/down for the user to left
            own feedback. Default: True. Example: True.
        citations_view_type (Union[Unset, None, ProjectSettingsCitationsViewType]): Control how citations are shown. By
            default, the user can initiate to see the citations. You can choose to have it "Auto Shown" or "Auto Hide"
            Default: ProjectSettingsCitationsViewType.USER. Example: user.
        no_answer_message (Union[Unset, None, str]): This is the message shown when the bot cannot answer. You can
            customize it to a message asking the user to contact customer support or leave their email / phone. Default:
            "I'm sorry, I don't know the answer". Example: Sorry, I don't have an answer for that..
        ending_message (Union[Unset, None, str]): You can instruct ChatGPT to end every response with some text like
            asking "Please email us for further support" (Not recommended for most use cases) Example: Please email us for
            further support.
        remove_branding (Union[Unset, None, bool]): Controls what branding is shown at the bottom of the chatbot.
        enable_recaptcha_for_public_chatbots (Union[Unset, None, bool]): Should we check messages from guests with
            Recaptcha when your chatbot is publicly available (i.e. shared or embedded).
        chatbot_model (Union[Unset, None, ProjectSettingsChatbotModel]): This is the model used by the chatbot. You can
            choose a different model to suit your needs. Default: ProjectSettingsChatbotModel.GPT_4. Example: gpt-4.
        is_selling_enabled (Union[Unset, None, bool]): Enable selling of chatbot for monetization
        license_slug (Union[Unset, None, bool]): License slug used for monetization
        selling_url (Union[Unset, None, str]): Selling URL used for monetization
    """

    chatbot_avatar: Union[Unset, str] = UNSET
    chatbot_background: Union[Unset, str] = UNSET
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
    license_slug: Union[Unset, None, bool] = UNSET
    selling_url: Union[Unset, None, str] = UNSET
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
            response_source = self.response_source

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

        license_slug = True if self.license_slug else False

        selling_url = self.selling_url

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
        if license_slug is not UNSET:
            field_dict["license_slug"] = license_slug
        if selling_url is not UNSET:
            field_dict["selling_url"] = selling_url

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        chatbot_avatar = src_dict.get("chatbot_avatar")

        chatbot_background = src_dict.get("chatbot_background")

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

        license_slug = src_dict.get("license_slug")

        selling_url = src_dict.get("selling_url")

        project_settings = cls(
            chatbot_avatar=chatbot_avatar,
            chatbot_background=chatbot_background,
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
            license_slug=license_slug,
            selling_url=selling_url,
        )

        project_settings.additional_properties = src_dict
        return project_settings

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
