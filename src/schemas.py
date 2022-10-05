from fastapi import HTTPException, Query, status
from pydantic import BaseModel, validator


class TrackingNumber(BaseModel):
    num: str = Query(..., title="DHL Tracking number.")

    @validator("num")
    def validate_num(cls, v):
        # Overcomplicated due to bug:
        # https://lightrun.com/answers/tiangolo-fastapi-fastapi---pydantic---valueerror-raises-internal-server-error-
        if not v.isalnum():
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Tracking number must contain only letters or numbers",
            )
        if len(v) > 20:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Max length is 20 symbols",
            )
        if len(v) < 16:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Min length is 16 symbols",
            )
        return v
