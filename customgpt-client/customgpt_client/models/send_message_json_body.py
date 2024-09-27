from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="SendMessageJsonBody")


@attr.s(auto_attribs=True)
class SendMessageJsonBody:
    """
    Attributes:
        prompt (Union[Unset, str]): Prompt to send to OpenAI Example: Write me hello world program in C.
        custom_persona (Union[Unset, None, str]): Custom persona to use for the conversation Example: You are a custom
            chatbot assistant called *bot name*, a friendly *bot role* who works for *organization* and answers questions
            based on the given context. Be as helpful as possible. Always prioritize the customer. Escalate complex issues.
            Stay on topic. Use appropriate language, Acknowledge limitations..
        chatbot_model (Union[Unset, None, SendMessageJsonBodyChatbotModel]): Chatbot model to use for the conversation
            Example: gpt-4.
        response_source (Union[Unset, None, SendMessageJsonBodyResponseSource]): By default, we ask ChatGPT to use only
            your content in its response (recommended). If you wish ChatGPT to improvise and use its own knowledgebase as
            well, you can set this to "openai_content". Default: SendMessageJsonBodyResponseSource.DEFAULT. Example:
            default.
    """

    prompt: Union[Unset, str] = UNSET
    custom_persona: Union[Unset, None, str] = UNSET
    chatbot_model: Union[Unset, str] = UNSET
    response_source: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        prompt = self.prompt
        custom_persona = self.custom_persona
        chatbot_model: Union[Unset, None, str] = UNSET
        if not isinstance(self.chatbot_model, Unset):
            chatbot_model = self.chatbot_model if self.chatbot_model else None

        response_source: Union[Unset, None, str] = UNSET
        if not isinstance(self.response_source, Unset):
            response_source = self.response_source if self.response_source else None

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if prompt is not UNSET:
            field_dict["prompt"] = prompt
        if custom_persona is not UNSET:
            field_dict["custom_persona"] = custom_persona
        if chatbot_model is not UNSET:
            field_dict["chatbot_model"] = chatbot_model
        if response_source is not UNSET:
            field_dict["response_source"] = response_source

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        prompt = src_dict.get("prompt")

        custom_persona = src_dict.get("custom_persona")

        chatbot_model = src_dict.get("chatbot_model")

        response_source = src_dict.get("response_source")

        send_message_json_body = cls(
            prompt=prompt,
            custom_persona=custom_persona,
            chatbot_model=chatbot_model,
            response_source=response_source,
        )

        send_message_json_body.additional_properties = src_dict
        return send_message_json_body

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
