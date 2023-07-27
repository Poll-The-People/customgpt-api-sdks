from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ListSourcesResponse200DataUploadsSettings")


@attr.s(auto_attribs=True)
class ListSourcesResponse200DataUploadsSettings:
    """The project source settings

    Attributes:
        data_refresh (Union[Unset, bool]): Whether the project source data should be refreshed Example: True.
        executive_js (Union[Unset, bool]): Whether the project source should execute JavaScript Default: True. Example:
            True.
        data_refresh_frequency (Union[Unset, str]): The project source data refresh frequency Default: 'never'. Example:
            never.
        sitemap_path (Union[Unset, str]): The project source sitemap path Example: https://example.com/sitemap.xml.
    """

    data_refresh: Union[Unset, bool] = False
    executive_js: Union[Unset, bool] = True
    data_refresh_frequency: Union[Unset, str] = "never"
    sitemap_path: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        data_refresh = self.data_refresh
        executive_js = self.executive_js
        data_refresh_frequency = self.data_refresh_frequency
        sitemap_path = self.sitemap_path

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if data_refresh is not UNSET:
            field_dict["data_refresh"] = data_refresh
        if executive_js is not UNSET:
            field_dict["executive_js"] = executive_js
        if data_refresh_frequency is not UNSET:
            field_dict["data_refresh_frequency"] = data_refresh_frequency
        if sitemap_path is not UNSET:
            field_dict["sitemap_path"] = sitemap_path

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        data_refresh = src_dict.get("data_refresh")

        executive_js = src_dict.get("executive_js")

        data_refresh_frequency = src_dict.get("data_refresh_frequency")

        sitemap_path = src_dict.get("sitemap_path")

        list_sources_response_200_data_uploads_settings = cls(
            data_refresh=data_refresh,
            executive_js=executive_js,
            data_refresh_frequency=data_refresh_frequency,
            sitemap_path=sitemap_path,
        )

        list_sources_response_200_data_uploads_settings.additional_properties = src_dict
        return list_sources_response_200_data_uploads_settings

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
