from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_project_response_200_data_project import GetProjectResponse200DataProject


T = TypeVar("T", bound="GetProjectResponse200Data")


@attr.s(auto_attribs=True)
class GetProjectResponse200Data:
    """
    Attributes:
        project (Union[Unset, GetProjectResponse200DataProject]):
    """

    project: Union[Unset, "GetProjectResponse200DataProject"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        project: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.project, Unset):
            project = self.project.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if project is not UNSET:
            field_dict["project"] = project

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.get_project_response_200_data_project import GetProjectResponse200DataProject

        d = src_dict.copy()
        _project = d.pop("project", UNSET)
        project: Union[Unset, GetProjectResponse200DataProject]
        if isinstance(_project, Unset):
            project = UNSET
        else:
            project = GetProjectResponse200DataProject.from_dict(_project)

        get_project_response_200_data = cls(
            project=project,
        )

        get_project_response_200_data.additional_properties = d
        return get_project_response_200_data

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
