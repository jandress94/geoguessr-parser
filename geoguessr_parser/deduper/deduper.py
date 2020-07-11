from abc import ABC, abstractmethod


class DeDuper(ABC):

    @abstractmethod
    def add_locs(self, locs):
        pass

    @abstractmethod
    def get_locs(self):
        pass
