from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreatePluginJsonBody")


@attr.s(auto_attribs=True)
class CreatePluginJsonBody:
    """
    Attributes:
        model_name (Union[Unset, str]): Model Name Example: IndoorPlants.
        human_name (Union[Unset, str]): Name For Human Example: The Indoor Plants Channel.
        keywords (Union[Unset, str]): Keywords For Model Example: Indoor plants, Gardening, Trusted information..
        description (Union[Unset, str]): Description For Human Example: Trusted information about indoor plants and
            gardening..
        is_active (Union[Unset, bool]): Whether the project plugin is active or not Example: True.
    """

    model_name: Union[Unset, str] = UNSET
    human_name: Union[Unset, str] = UNSET
    keywords: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    is_active: Union[Unset, bool] = False
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        model_name = self.model_name
        human_name = self.human_name
        keywords = self.keywords
        description = self.description
        is_active = self.is_active

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if model_name is not UNSET:
            field_dict["model_name"] = model_name
        if human_name is not UNSET:
            field_dict["human_name"] = human_name
        if keywords is not UNSET:
            field_dict["keywords"] = keywords
        if description is not UNSET:
            field_dict["description"] = description
        if is_active is not UNSET:
            field_dict["is_active"] = is_active

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        model_name = src_dict.get("model_name")

        human_name = src_dict.get("human_name")

        keywords = src_dict.get("keywords")

        description = src_dict.get("description")

        is_active = src_dict.get("is_active")

        create_plugin_json_body = cls(
            model_name=model_name,
            human_name=human_name,
            keywords=keywords,
            description=description,
            is_active=is_active,
        )

        create_plugin_json_body.additional_properties = src_dict
        return create_plugin_json_body

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
