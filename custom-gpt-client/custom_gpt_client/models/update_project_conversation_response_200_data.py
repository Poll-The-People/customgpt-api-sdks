from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.update_project_conversation_response_200_data_conversation_schema import (
        UpdateProjectConversationResponse200DataConversationSchema,
    )


T = TypeVar("T", bound="UpdateProjectConversationResponse200Data")


@attr.s(auto_attribs=True)
class UpdateProjectConversationResponse200Data:
    """
    Attributes:
        conversation_schema (Union[Unset, UpdateProjectConversationResponse200DataConversationSchema]):
    """

    conversation_schema: Union[Unset, "UpdateProjectConversationResponse200DataConversationSchema"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        conversation_schema: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.conversation_schema, Unset):
            conversation_schema = self.conversation_schema.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if conversation_schema is not UNSET:
            field_dict["ConversationSchema"] = conversation_schema

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.update_project_conversation_response_200_data_conversation_schema import (
            UpdateProjectConversationResponse200DataConversationSchema,
        )

        d = src_dict.copy()
        _conversation_schema = d.pop("ConversationSchema", UNSET)
        conversation_schema: Union[Unset, UpdateProjectConversationResponse200DataConversationSchema]
        if isinstance(_conversation_schema, Unset):
            conversation_schema = UNSET
        else:
            conversation_schema = UpdateProjectConversationResponse200DataConversationSchema.from_dict(
                _conversation_schema
            )

        update_project_conversation_response_200_data = cls(
            conversation_schema=conversation_schema,
        )

        update_project_conversation_response_200_data.additional_properties = d
        return update_project_conversation_response_200_data

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
