from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_project_pages_response_200_data_pages import GetProjectPagesResponse200DataPages
    from ..models.get_project_pages_response_200_data_project import GetProjectPagesResponse200DataProject


T = TypeVar("T", bound="GetProjectPagesResponse200Data")


@attr.s(auto_attribs=True)
class GetProjectPagesResponse200Data:
    """
    Attributes:
        project (Union[Unset, GetProjectPagesResponse200DataProject]):
        pages (Union[Unset, GetProjectPagesResponse200DataPages]):
    """

    project: Union[Unset, "GetProjectPagesResponse200DataProject"] = UNSET
    pages: Union[Unset, "GetProjectPagesResponse200DataPages"] = UNSET
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
        from ..models.get_project_pages_response_200_data_pages import GetProjectPagesResponse200DataPages
        from ..models.get_project_pages_response_200_data_project import GetProjectPagesResponse200DataProject

        d = src_dict.copy()
        _project = d.pop("project", UNSET)
        project: Union[Unset, GetProjectPagesResponse200DataProject]
        if isinstance(_project, Unset):
            project = UNSET
        else:
            project = GetProjectPagesResponse200DataProject.from_dict(_project)

        _pages = d.pop("pages", UNSET)
        pages: Union[Unset, GetProjectPagesResponse200DataPages]
        if isinstance(_pages, Unset):
            pages = UNSET
        else:
            pages = GetProjectPagesResponse200DataPages.from_dict(_pages)

        get_project_pages_response_200_data = cls(
            project=project,
            pages=pages,
        )

        get_project_pages_response_200_data.additional_properties = d
        return get_project_pages_response_200_data

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
