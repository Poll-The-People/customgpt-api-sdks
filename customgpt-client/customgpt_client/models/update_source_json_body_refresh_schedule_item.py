from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateSourceJsonBodyRefreshScheduleItem")


@attr.s(auto_attribs=True)
class UpdateSourceJsonBodyRefreshScheduleItem:
    """
    Attributes:
        days (Union[Unset, List[int]]): Index of days in which sitemap should be refreshed. Starts from 0 (Sunday) to 6
            (Saturday). Example: [0, 1, 4, 6].
        hours (Union[Unset, List[str]]): List of times in which sitemap should be refreshed. Must be in HH:MM format.
            Example: ['00:00', '08:00', '23:45'].
    """

    days: Union[Unset, List[int]] = UNSET
    hours: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        days: Union[Unset, List[int]] = UNSET
        if not isinstance(self.days, Unset):
            days = self.days

        hours: Union[Unset, List[str]] = UNSET
        if not isinstance(self.hours, Unset):
            hours = self.hours

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if days is not UNSET:
            for index, field_value in enumerate(days):
                field_dict[f"days[{index}]"] = field_value
        if hours is not UNSET:
            for index, field_value in enumerate(hours):
                field_dict[f"hours[{index}]"] = field_value

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        days = cast(List[int], src_dict.get("days"))

        hours = cast(List[str], src_dict.get("hours"))

        update_source_json_body_refresh_schedule_item = cls(
            days=days,
            hours=hours,
        )

        update_source_json_body_refresh_schedule_item.additional_properties = src_dict
        return update_source_json_body_refresh_schedule_item

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
