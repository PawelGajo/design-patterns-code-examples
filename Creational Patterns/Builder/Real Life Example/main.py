from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any



class Builder(ABC):
    @property
    @abstractmethod
    def product(self) -> None:
        pass

    @abstractmethod
    def produce_garage(self) -> None:
        pass

    @abstractmethod
    def produce_garden(self) -> None:
        pass

    @abstractmethod
    def produce_swimming_pool(self) -> None:
        pass

    @abstractmethod
    def produce_bedrooms(self, value: int) -> None:
        pass


class ApartmentBuilder(Builder):
    def __init__(self) -> None:
        self.reset()

    def reset(self) -> None:
        self._product = Apartment()

    @property
    def product(self) -> Apartment:
        product = self._product
        self.reset()
        return product

    def produce_garage(self) -> None:
        self._product.add("Garage") # eg.Garage() class

    def produce_bedrooms(self, value: int) -> None:
        self._product.add(f'{str(value)} bedrooms')

    def produce_garden(self) -> None:
        self._product.add("Garden")
        
    def produce_swimming_pool(self) -> None:
        self._product.add("Swimming Pool")


class Apartment():
    def __init__(self) -> None:
        self.parts = []

    def add(self, part: Any) -> None:
        self.parts.append(part)

    def list_parts(self) -> None:
        print(f"Apartment parts: {', '.join(self.parts)}", end="")


class HouseDirector:
    def __init__(self) -> None:
        self._builder = None

    @property
    def builder(self) -> Builder:
        return self._builder

    @builder.setter
    def builder(self, builder: Builder) -> None:
        self._builder = builder

    def build_studio(self) -> None:
        self.builder.produce_bedrooms(1)

    def build_residence(self) -> None:
        self.builder.produce_bedrooms(2)
        self.builder.produce_garage()
        self.builder.produce_swimming_pool()

if __name__ == "__main__":
    director = HouseDirector()
    builder = ApartmentBuilder()
    director.builder = builder

    print("Basic studio: ")
    director.build_studio()
    builder.product.list_parts()

    print("\n")

    print("Premium Apartment: ")
    director.build_residence()
    builder.product.list_parts()
