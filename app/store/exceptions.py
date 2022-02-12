from typing import Any, Dict, Optional

from fastapi import HTTPException, status


class StoreNotFoundException(HTTPException):
    def __init__(
        self,
        status_code: int = status.HTTP_404_NOT_FOUND,
        detail: Any = "Store not found",
        headers: Optional[Dict[str, Any]] = None,
    ) -> None:
        super().__init__(status_code, detail=detail, headers=headers)
