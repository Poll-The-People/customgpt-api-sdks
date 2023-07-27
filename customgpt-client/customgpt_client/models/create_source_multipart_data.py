from io import BytesIO
from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, File, FileJsonType, Unset

T = TypeVar("T", bound="CreateSourceMultipartData")


@attr.s(auto_attribs=True)
class CreateSourceMultipartData:
    """
    Attributes:
        sitemap_path (Union[Unset, str]): The sitemap path Example: https://example.com/sitemap.xml.
        file_data_retension (Union[Unset, bool]): File data retension Example: True.
        file (Union[Unset, File]): The submitted file. Example: file.pdf.
    """

    sitemap_path: Union[Unset, str] = UNSET
    file_data_retension: Union[Unset, bool] = UNSET
    file: Union[Unset, File] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        sitemap_path = self.sitemap_path
        file_data_retension = self.file_data_retension
        file: Union[Unset, FileJsonType] = UNSET
        if not isinstance(self.file, Unset):
            file = self.file.to_tuple()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if sitemap_path is not UNSET:
            field_dict["sitemap_path"] = sitemap_path
        if file_data_retension is not UNSET:
            field_dict["file_data_retension"] = file_data_retension
        if file is not UNSET:
            field_dict["file"] = file

        return field_dict

    def to_multipart(self) -> Dict[str, Any]:
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
        if sitemap_path is not UNSET:
            field_dict["sitemap_path"] = sitemap_path
        if file_data_retension is not UNSET:
            field_dict["file_data_retension"] = file_data_retension
        if file is not UNSET:
            field_dict["file"] = file

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        sitemap_path = src_dict.get("sitemap_path")

        file_data_retension = src_dict.get("file_data_retension")

        _file = src_dict.get("file")
        file: Union[Unset, File]
        if isinstance(_file, Unset):
            file = UNSET
        else:
            file = File(payload=BytesIO(_file))

        create_source_multipart_data = cls(
            sitemap_path=sitemap_path,
            file_data_retension=file_data_retension,
            file=file,
        )

        create_source_multipart_data.additional_properties = src_dict
        return create_source_multipart_data

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
