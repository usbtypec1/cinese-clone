from dataclasses import dataclass


@dataclass(frozen=True, slots=True, kw_only=True)
class CategoryListQueryModel:
    id: int
    name: str
    hashtag: str
