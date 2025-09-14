from dataclasses import dataclass


@dataclass(frozen=True, slots=True, kw_only=True)
class CityListQueryModel:
    id: int
    name: str
