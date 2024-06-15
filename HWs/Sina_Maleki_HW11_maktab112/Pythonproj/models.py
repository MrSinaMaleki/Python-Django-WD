from abc import ABC, abstractmethod


class Model(ABC):
    @classmethod
    @property
    @abstractmethod
    def registered_list(cls):
        raise NotImplemented("'users_list' is required! ")
