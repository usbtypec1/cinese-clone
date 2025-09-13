from enum import StrEnum


class DeliveryOption(StrEnum):
    NO_DELIVERY = 'no_delivery'
    COUNTRY = 'across_country'
    CIS = 'cis'
    WORLD = 'world'
