from enum import Enum
from typing import Dict, Optional, Union
from hashlib import _Hash as MD5Hash

class VersionAlphanumericType(str, Enum): ...

class VersionAuthor:
    _hash: MD5Hash
    _co_author: bool
    active: bool
    email: str
    name: str
    def __init__(
        self,
        name,
        *,
        shared: Optional[bool] = False,
        active: Optional[bool] = True,
        email: Optional[str] = None,
    ) -> None: ...
    def __hash__(self) -> MD5Hash: ...
    def __str__(self) -> str: ...
    @property
    def signature(self) -> str: ...

class Version:
    _major: int
    _minor: int
    _patch: int
    __version: str
    __alphanum: Dict[str, Union[int, VersionAlphanumericType]]
    def __init__(self, **kwargs) -> None: ...
    def __repr__(self) -> str: ...
    @property
    def major(self) -> int: ...
    @property
    def minor(self) -> int: ...
    @property
    def patch(self) -> int: ...
    @property
    def is_alphanumeric(self) -> bool: ...
    @classmethod
    def extend_version(cls, **kwargs) -> str: ...