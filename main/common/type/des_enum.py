from enum import Enum


class DescEnum(Enum):

    def __new__(cls, value, desc=None):
        self = str.__new__(cls)
        self._value_ = value
        if desc is not None:
            self.desc = desc
        return self
