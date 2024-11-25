from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetApiV1LimitsUsageResponse200Data")


@attr.s(auto_attribs=True)
class GetApiV1LimitsUsageResponse200Data:
    """
    Attributes:
        max_projects_num (Union[Unset, int]): The maximum number of projects allowed for this team. Example: 10.
        current_projects_num (Union[Unset, int]): The total number of projects currently belonging to this team.
            Example: 10.
        max_total_storage_credits (Union[Unset, int]): The maximum number of storage credits allowed for this team.
            Example: 10.
        current_total_storage_credits (Union[Unset, int]): The amount of storage credits currently in use. Example: 10.
        max_queries (Union[Unset, int]): The maximum number of queries allowed per billing cycle for this team. Example:
            10.
        current_queries (Union[Unset, int]): The number of queries used in the current billing cycle. Example: 10.
    """

    max_projects_num: Union[Unset, int] = UNSET
    current_projects_num: Union[Unset, int] = UNSET
    max_total_storage_credits: Union[Unset, int] = UNSET
    current_total_storage_credits: Union[Unset, int] = UNSET
    max_queries: Union[Unset, int] = UNSET
    current_queries: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        max_projects_num = self.max_projects_num
        current_projects_num = self.current_projects_num
        max_total_storage_credits = self.max_total_storage_credits
        current_total_storage_credits = self.current_total_storage_credits
        max_queries = self.max_queries
        current_queries = self.current_queries

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if max_projects_num is not UNSET:
            field_dict["max_projects_num"] = max_projects_num
        if current_projects_num is not UNSET:
            field_dict["current_projects_num"] = current_projects_num
        if max_total_storage_credits is not UNSET:
            field_dict["max_total_storage_credits"] = max_total_storage_credits
        if current_total_storage_credits is not UNSET:
            field_dict["current_total_storage_credits"] = current_total_storage_credits
        if max_queries is not UNSET:
            field_dict["max_queries"] = max_queries
        if current_queries is not UNSET:
            field_dict["current_queries"] = current_queries

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        max_projects_num = src_dict.get("max_projects_num")

        current_projects_num = src_dict.get("current_projects_num")

        max_total_storage_credits = src_dict.get("max_total_storage_credits")

        current_total_storage_credits = src_dict.get("current_total_storage_credits")

        max_queries = src_dict.get("max_queries")

        current_queries = src_dict.get("current_queries")

        get_api_v1_limits_usage_response_200_data = cls(
            max_projects_num=max_projects_num,
            current_projects_num=current_projects_num,
            max_total_storage_credits=max_total_storage_credits,
            current_total_storage_credits=current_total_storage_credits,
            max_queries=max_queries,
            current_queries=current_queries,
        )

        get_api_v1_limits_usage_response_200_data.additional_properties = src_dict
        return get_api_v1_limits_usage_response_200_data

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
