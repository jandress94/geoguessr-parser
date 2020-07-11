from abc import ABC, abstractmethod


class GeoParser(ABC):

    @abstractmethod
    def parse(self, filepath):
        pass
