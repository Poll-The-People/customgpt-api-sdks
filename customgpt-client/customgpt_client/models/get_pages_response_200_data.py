from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_pages_response_200_data_pages import GetPagesResponse200DataPages
    from ..models.get_pages_response_200_data_project import GetPagesResponse200DataProject


T = TypeVar("T", bound="GetPagesResponse200Data")


@attr.s(auto_attribs=True)
class GetPagesResponse200Data:
    """
    Attributes:
        project (Union[Unset, GetPagesResponse200DataProject]):
        pages (Union[Unset, GetPagesResponse200DataPages]):
    """

    project: Union[Unset, "GetPagesResponse200DataProject"] = UNSET
    pages: Union[Unset, "GetPagesResponse200DataPages"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        project: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.project, Unset):
            project = self.project.to_dict()

        pages: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.pages, Unset):
            pages = self.pages.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if project is not UNSET:
            field_dict["project"] = project
        if pages is not UNSET:
            field_dict["pages"] = pages

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.get_pages_response_200_data_pages import GetPagesResponse200DataPages
        from ..models.get_pages_response_200_data_project import GetPagesResponse200DataProject

        _project = src_dict.get("project")
        project: Union[Unset, GetPagesResponse200DataProject]
        if isinstance(_project, Unset):
            project = UNSET
        else:
            project = GetPagesResponse200DataProject.from_dict(_project)

        _pages = src_dict.get("pages")
        pages: Union[Unset, GetPagesResponse200DataPages]
        if isinstance(_pages, Unset):
            pages = UNSET
        else:
            pages = GetPagesResponse200DataPages.from_dict(_pages)

        get_pages_response_200_data = cls(
            project=project,
            pages=pages,
        )

        get_pages_response_200_data.additional_properties = src_dict
        return get_pages_response_200_data

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
