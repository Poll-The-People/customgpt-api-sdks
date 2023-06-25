from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ProjectPlugin")


@attr.s(auto_attribs=True)
class ProjectPlugin:
    """
    Attributes:
        id (Union[Unset, int]): Plugin ID Example: 1.
        model_name (Union[Unset, str]): Model Name Example: IndoorPlants.
        human_name (Union[Unset, str]): Name For Human Example: The Indoor Plants Channel.
        keywords (Union[Unset, str]): Keywords For Model Example: Indoor plants, Gardening, Trusted information..
        description (Union[Unset, str]): Description For Human Example: Trusted information about indoor plants and
            gardening..
        logo (Union[Unset, str]): Project plugin logo Example: https://app.customgpt.ai/logo.svg.
        is_active (Union[Unset, bool]): Whether the project plugin is active or not Example: True.
    """

    id: Union[Unset, int] = UNSET
    model_name: Union[Unset, str] = UNSET
    human_name: Union[Unset, str] = UNSET
    keywords: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    logo: Union[Unset, str] = UNSET
    is_active: Union[Unset, bool] = False
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        model_name = self.model_name
        human_name = self.human_name
        keywords = self.keywords
        description = self.description
        logo = self.logo
        is_active = self.is_active

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if model_name is not UNSET:
            field_dict["model_name"] = model_name
        if human_name is not UNSET:
            field_dict["human_name"] = human_name
        if keywords is not UNSET:
            field_dict["keywords"] = keywords
        if description is not UNSET:
            field_dict["description"] = description
        if logo is not UNSET:
            field_dict["logo"] = logo
        if is_active is not UNSET:
            field_dict["is_active"] = is_active

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        model_name = d.pop("model_name", UNSET)

        human_name = d.pop("human_name", UNSET)

        keywords = d.pop("keywords", UNSET)

        description = d.pop("description", UNSET)

        logo = d.pop("logo", UNSET)

        is_active = d.pop("is_active", UNSET)

        project_plugin = cls(
            id=id,
            model_name=model_name,
            human_name=human_name,
            keywords=keywords,
            description=description,
            logo=logo,
            is_active=is_active,
        )

        project_plugin.additional_properties = d
        return project_plugin

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
