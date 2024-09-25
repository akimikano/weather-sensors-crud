from typing import TypeAlias, Annotated

from fastapi import Path


IntPath: TypeAlias = Annotated[int, Path]
