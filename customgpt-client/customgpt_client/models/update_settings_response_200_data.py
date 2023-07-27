from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateSettingsResponse200Data")


@attr.s(auto_attribs=True)
class UpdateSettingsResponse200Data:
    """
    Attributes:
        updated (Union[Unset, bool]): Whether the project was updated successfully or not Example: True.
    """

    updated: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        updated = self.updated

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if updated is not UNSET:
            field_dict["updated"] = updated

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        updated = src_dict.get("updated")

        update_settings_response_200_data = cls(
            updated=updated,
        )

        update_settings_response_200_data.additional_properties = src_dict
        return update_settings_response_200_data

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
