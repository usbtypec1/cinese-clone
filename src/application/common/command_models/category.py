from dataclasses import dataclass


@dataclass
class CategoryCreateCommandModel:
    name: str
    hashtag: str
