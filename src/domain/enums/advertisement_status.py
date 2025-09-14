from enum import StrEnum


class AdvertisementStatus(StrEnum):
    NOT_PUBLISHED = 'not_published'
    AWAITING_MODERATION = 'awaiting_moderation'
    PUBLISHED = 'published'
    REJECTED = 'rejected'
    ARCHIVED = 'archived'
