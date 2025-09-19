from pydantic import BaseModel


class Ticket(BaseModel):
    price: float | int | None = None
    symbol: str | None = None