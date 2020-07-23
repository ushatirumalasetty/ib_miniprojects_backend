import enum

from ib_common.constants import BaseEnumClass


class UserRole(BaseEnumClass, enum.Enum):
    USER="USER"
    ADMIN="ADMIN"
    RP="RP"