from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.update_project_response_200_data_project import UpdateProjectResponse200DataProject


T = TypeVar("T", bound="UpdateProjectResponse200Data")


@attr.s(auto_attribs=True)
class UpdateProjectResponse200Data:
    """
    Attributes:
        project (Union[Unset, UpdateProjectResponse200DataProject]):
    """

    project: Union[Unset, "UpdateProjectResponse200DataProject"] = UNSET
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
        from ..models.update_project_response_200_data_project import UpdateProjectResponse200DataProject

        d = src_dict.copy()
        _project = d.pop("project", UNSET)
        project: Union[Unset, UpdateProjectResponse200DataProject]
        if isinstance(_project, Unset):
            project = UNSET
        else:
            project = UpdateProjectResponse200DataProject.from_dict(_project)

        update_project_response_200_data = cls(
            project=project,
        )

        update_project_response_200_data.additional_properties = d
        return update_project_response_200_data

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
