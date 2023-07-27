from io import BytesIO
from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, File, FileJsonType, Unset

T = TypeVar("T", bound="UpdateProjectMultipartData")


@attr.s(auto_attribs=True)
class UpdateProjectMultipartData:
    """
    Attributes:
        project_name (Union[Unset, str]): Project name Example: My project.
        is_shared (Union[Unset, bool]): Whether the project is shared or not Example: True.
        sitemap_path (Union[Unset, str]): Sitemap path Example: https://example.com/sitemap.xml.
        file_data_retension (Union[Unset, bool]): File data retension Example: True.
        file (Union[Unset, File]): File Example: file.pdf.
    """

    project_name: Union[Unset, str] = UNSET
    is_shared: Union[Unset, bool] = UNSET
    sitemap_path: Union[Unset, str] = UNSET
    file_data_retension: Union[Unset, bool] = UNSET
    file: Union[Unset, File] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        project_name = self.project_name
        is_shared = self.is_shared
        sitemap_path = self.sitemap_path
        file_data_retension = self.file_data_retension
        file: Union[Unset, FileJsonType] = UNSET
        if not isinstance(self.file, Unset):
            file = self.file.to_tuple()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if project_name is not UNSET:
            field_dict["project_name"] = project_name
        if is_shared is not UNSET:
            field_dict["is_shared"] = is_shared
        if sitemap_path is not UNSET:
            field_dict["sitemap_path"] = sitemap_path
        if file_data_retension is not UNSET:
            field_dict["file_data_retension"] = file_data_retension
        if file is not UNSET:
            field_dict["file"] = file

        return field_dict

    def to_multipart(self) -> Dict[str, Any]:
        project_name = (
            self.project_name
            if isinstance(self.project_name, Unset)
            else (None, str(self.project_name).encode(), "text/plain")
        )
        is_shared = (
            self.is_shared if isinstance(self.is_shared, Unset) else (None, str(self.is_shared).encode(), "text/plain")
        )
        sitemap_path = (
            self.sitemap_path
            if isinstance(self.sitemap_path, Unset)
            else (None, str(self.sitemap_path).encode(), "text/plain")
        )
        file_data_retension = (
            self.file_data_retension
            if isinstance(self.file_data_retension, Unset)
            else (None, str(self.file_data_retension).encode(), "text/plain")
        )
        file: Union[Unset, FileJsonType] = UNSET
        if not isinstance(self.file, Unset):
            file = self.file.to_tuple()

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {key: (None, str(value).encode(), "text/plain") for key, value in self.additional_properties.items()}
        )
        field_dict.update({})
        if project_name is not UNSET:
            field_dict["project_name"] = project_name
        if is_shared is not UNSET:
            field_dict["is_shared"] = is_shared
        if sitemap_path is not UNSET:
            field_dict["sitemap_path"] = sitemap_path
        if file_data_retension is not UNSET:
            field_dict["file_data_retension"] = file_data_retension
        if file is not UNSET:
            field_dict["file"] = file

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        project_name = src_dict.get("project_name")

        is_shared = src_dict.get("is_shared")

        sitemap_path = src_dict.get("sitemap_path")

        file_data_retension = src_dict.get("file_data_retension")

        _file = src_dict.get("file")
        file: Union[Unset, File]
        if isinstance(_file, Unset):
            file = UNSET
        else:
            file = File(payload=BytesIO(_file))

        update_project_multipart_data = cls(
            project_name=project_name,
            is_shared=is_shared,
            sitemap_path=sitemap_path,
            file_data_retension=file_data_retension,
            file=file,
        )

        update_project_multipart_data.additional_properties = src_dict
        return update_project_multipart_data

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
