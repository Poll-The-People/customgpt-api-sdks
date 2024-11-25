from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ProjectSourceSettings")


@attr.s(auto_attribs=True)
class ProjectSourceSettings:
    """The project source settings

    Attributes:
        executive_js (Union[Unset, bool]): Whether the project source should execute JavaScript Default: True. Example:
            True.
        data_refresh_frequency (Union[Unset, ProjectSourceSettingsDataRefreshFrequency]): The project source data
            refresh frequency Default: ProjectSourceSettingsDataRefreshFrequency.NEVER. Example: never.
        create_new_pages (Union[Unset, bool]): Add new pages to project automatically during refresh project source
            Default: True. Example: True.
        remove_unexist_pages (Union[Unset, bool]): Remove pages from project automatically during refresh project source
            Default: True.
        refresh_existing_pages (Union[Unset, ProjectSourceSettingsRefreshExistingPages]): Refresh existing page during
            refresh project source Default: ProjectSourceSettingsRefreshExistingPages.NEVER. Example: never.
        sitemap_path (Union[Unset, str]): The project source sitemap path Example: https://example.com/sitemap.xml.
    """

    executive_js: Union[Unset, bool] = True
    data_refresh_frequency: Union[Unset, str] = UNSET
    create_new_pages: Union[Unset, bool] = True
    remove_unexist_pages: Union[Unset, bool] = True
    refresh_existing_pages: Union[Unset, str] = UNSET
    sitemap_path: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        executive_js = True if self.executive_js else False

        data_refresh_frequency: Union[Unset, str] = UNSET
        if not isinstance(self.data_refresh_frequency, Unset):
            data_refresh_frequency = self.data_refresh_frequency

        create_new_pages = True if self.create_new_pages else False

        remove_unexist_pages = True if self.remove_unexist_pages else False

        refresh_existing_pages: Union[Unset, str] = UNSET
        if not isinstance(self.refresh_existing_pages, Unset):
            refresh_existing_pages = self.refresh_existing_pages

        sitemap_path = self.sitemap_path

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if executive_js is not UNSET:
            field_dict["executive_js"] = executive_js
        if data_refresh_frequency is not UNSET:
            field_dict["data_refresh_frequency"] = data_refresh_frequency
        if create_new_pages is not UNSET:
            field_dict["create_new_pages"] = create_new_pages
        if remove_unexist_pages is not UNSET:
            field_dict["remove_unexist_pages"] = remove_unexist_pages
        if refresh_existing_pages is not UNSET:
            field_dict["refresh_existing_pages"] = refresh_existing_pages
        if sitemap_path is not UNSET:
            field_dict["sitemap_path"] = sitemap_path

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        executive_js = src_dict.get("executive_js")

        data_refresh_frequency = src_dict.get("data_refresh_frequency")

        create_new_pages = src_dict.get("create_new_pages")

        remove_unexist_pages = src_dict.get("remove_unexist_pages")

        refresh_existing_pages = src_dict.get("refresh_existing_pages")

        sitemap_path = src_dict.get("sitemap_path")

        project_source_settings = cls(
            executive_js=executive_js,
            data_refresh_frequency=data_refresh_frequency,
            create_new_pages=create_new_pages,
            remove_unexist_pages=remove_unexist_pages,
            refresh_existing_pages=refresh_existing_pages,
            sitemap_path=sitemap_path,
        )

        project_source_settings.additional_properties = src_dict
        return project_source_settings

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
