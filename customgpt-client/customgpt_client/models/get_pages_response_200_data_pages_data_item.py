import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.get_pages_response_200_data_pages_data_item_crawl_status import (
    GetPagesResponse200DataPagesDataItemCrawlStatus,
)
from ..models.get_pages_response_200_data_pages_data_item_index_status import (
    GetPagesResponse200DataPagesDataItemIndexStatus,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="GetPagesResponse200DataPagesDataItem")


@attr.s(auto_attribs=True)
class GetPagesResponse200DataPagesDataItem:
    r"""
    Attributes:
        id (Union[Unset, int]): Page ID Example: 1.
        page_url (Union[Unset, str]): URL of the page or file Example: https://example.com.
        page_url_hash (Union[Unset, str]): Hash of the URL of the page or file Example:
            d41d8cd98f00b204e9800998ecf8427e.
        project_id (Union[Unset, int]): Project ID Example: 1.
        s3_path (Union[Unset, None, str]): This is the path where the page is stored in S3.\nNote: This is omitted in
            the response if the page is not a file Example: project-1/page-1/file.pdf.
        crawl_status (Union[Unset, GetPagesResponse200DataPagesDataItemCrawlStatus]): Crawl status of the page Default:
            GetPagesResponse200DataPagesDataItemCrawlStatus.QUEUED. Example: queued.
        index_status (Union[Unset, GetPagesResponse200DataPagesDataItemIndexStatus]): Index status of the page Default:
            GetPagesResponse200DataPagesDataItemIndexStatus.QUEUED. Example: queued.
        is_file (Union[Unset, bool]): Whether the page is a file or not Example: True.
        is_file_kept (Union[Unset, bool]): Whether the file is kept after processing or not.\nNote: This is omitted in
            the response if the page is not a file Default: True. Example: True.
        filename (Union[Unset, None, str]): Filename of the page.\nNote: This is omitted in the response if the page is
            not a file Example: file.pdf.
        filesize (Union[Unset, None, int]): Filesize of the page.\nNote: This is omitted in the response if the page is
            not a file Example: 100.
        created_at (Union[Unset, datetime.datetime]): Date and time when the page was created Example: 2021-01-01
            00:00:00.
        updated_at (Union[Unset, datetime.datetime]): Date and time when the page was updated Example: 2021-01-01
            00:00:00.
        deleted_at (Union[Unset, None, datetime.datetime]): Date and time when the page was deleted Example: 2021-01-01
            00:00:00.
    """

    id: Union[Unset, int] = UNSET
    page_url: Union[Unset, str] = UNSET
    page_url_hash: Union[Unset, str] = UNSET
    project_id: Union[Unset, int] = UNSET
    s3_path: Union[Unset, None, str] = UNSET
    crawl_status: Union[
        Unset, GetPagesResponse200DataPagesDataItemCrawlStatus
    ] = GetPagesResponse200DataPagesDataItemCrawlStatus.QUEUED
    index_status: Union[
        Unset, GetPagesResponse200DataPagesDataItemIndexStatus
    ] = GetPagesResponse200DataPagesDataItemIndexStatus.QUEUED
    is_file: Union[Unset, bool] = False
    is_file_kept: Union[Unset, bool] = True
    filename: Union[Unset, None, str] = UNSET
    filesize: Union[Unset, None, int] = UNSET
    created_at: Union[Unset, datetime.datetime] = UNSET
    updated_at: Union[Unset, datetime.datetime] = UNSET
    deleted_at: Union[Unset, None, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        page_url = self.page_url
        page_url_hash = self.page_url_hash
        project_id = self.project_id
        s3_path = self.s3_path
        crawl_status: Union[Unset, str] = UNSET
        if not isinstance(self.crawl_status, Unset):
            crawl_status = self.crawl_status.value

        index_status: Union[Unset, str] = UNSET
        if not isinstance(self.index_status, Unset):
            index_status = self.index_status.value

        is_file = self.is_file
        is_file_kept = self.is_file_kept
        filename = self.filename
        filesize = self.filesize
        created_at: Union[Unset, str] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        updated_at: Union[Unset, str] = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        deleted_at: Union[Unset, None, str] = UNSET
        if not isinstance(self.deleted_at, Unset):
            deleted_at = self.deleted_at.isoformat() if self.deleted_at else None

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if page_url is not UNSET:
            field_dict["page_url"] = page_url
        if page_url_hash is not UNSET:
            field_dict["page_url_hash"] = page_url_hash
        if project_id is not UNSET:
            field_dict["project_id"] = project_id
        if s3_path is not UNSET:
            field_dict["s3_path"] = s3_path
        if crawl_status is not UNSET:
            field_dict["crawl_status"] = crawl_status
        if index_status is not UNSET:
            field_dict["index_status"] = index_status
        if is_file is not UNSET:
            field_dict["is_file"] = is_file
        if is_file_kept is not UNSET:
            field_dict["is_file_kept"] = is_file_kept
        if filename is not UNSET:
            field_dict["filename"] = filename
        if filesize is not UNSET:
            field_dict["filesize"] = filesize
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if deleted_at is not UNSET:
            field_dict["deleted_at"] = deleted_at

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        id = src_dict.get("id")

        page_url = src_dict.get("page_url")

        page_url_hash = src_dict.get("page_url_hash")

        project_id = src_dict.get("project_id")

        s3_path = src_dict.get("s3_path")

        _crawl_status = src_dict.get("crawl_status")
        crawl_status: Union[Unset, GetPagesResponse200DataPagesDataItemCrawlStatus]
        if isinstance(_crawl_status, Unset):
            crawl_status = UNSET
        else:
            crawl_status = GetPagesResponse200DataPagesDataItemCrawlStatus(_crawl_status)

        _index_status = src_dict.get("index_status")
        index_status: Union[Unset, GetPagesResponse200DataPagesDataItemIndexStatus]
        if isinstance(_index_status, Unset):
            index_status = UNSET
        else:
            index_status = GetPagesResponse200DataPagesDataItemIndexStatus(_index_status)

        is_file = src_dict.get("is_file")

        is_file_kept = src_dict.get("is_file_kept")

        filename = src_dict.get("filename")

        filesize = src_dict.get("filesize")

        _created_at = src_dict.get("created_at")
        created_at: Union[Unset, datetime.datetime]
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = isoparse(_created_at)

        _updated_at = src_dict.get("updated_at")
        updated_at: Union[Unset, datetime.datetime]
        if isinstance(_updated_at, Unset):
            updated_at = UNSET
        else:
            updated_at = isoparse(_updated_at)

        _deleted_at = src_dict.get("deleted_at")
        deleted_at: Union[Unset, None, datetime.datetime]
        if _deleted_at is None:
            deleted_at = None
        elif isinstance(_deleted_at, Unset):
            deleted_at = UNSET
        else:
            deleted_at = isoparse(_deleted_at)

        get_pages_response_200_data_pages_data_item = cls(
            id=id,
            page_url=page_url,
            page_url_hash=page_url_hash,
            project_id=project_id,
            s3_path=s3_path,
            crawl_status=crawl_status,
            index_status=index_status,
            is_file=is_file,
            is_file_kept=is_file_kept,
            filename=filename,
            filesize=filesize,
            created_at=created_at,
            updated_at=updated_at,
            deleted_at=deleted_at,
        )

        get_pages_response_200_data_pages_data_item.additional_properties = src_dict
        return get_pages_response_200_data_pages_data_item

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
