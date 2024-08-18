from abc import ABC, abstractmethod

# Abstract Factory


class AbstractFactory(ABC):
    @abstractmethod
    def create_product_a(self):
        pass

    @abstractmethod
    def create_product_b(self):
        pass

# Concrete Factories


class ConcreteFactoryA(AbstractFactory):
    def create_product_a(self):
        return ProductA1()

    def create_product_b(self):
        return ProductB1()


class ConcreteFactoryB(AbstractFactory):
    def create_product_a(self):
        return ProductA2()

    def create_product_b(self):
        return ProductB2()

# Abstract Products


class AbstractProductA(ABC):
    @abstractmethod
    def operation(self):
        pass


class AbstractProductB(ABC):
    @abstractmethod
    def operation(self):
        pass

# Concrete Products


class ProductA1(AbstractProductA):
    def operation(self) -> str:
        print("ProductA1 operation")


class ProductB1(AbstractProductB):
    def operation(self) -> str:
        print("ProductB1 operation")


class ProductA2(AbstractProductA):
    def operation(self) -> str:
        print("ProductA2 operation")


class ProductB2(AbstractProductB):
    def operation(self) -> str:
        print("ProductB2 operation")

# Client code


def client_code(factory: AbstractFactory):
    # Can add new products and factories without changing
    # client code
    # Abstracts Creation from Operations and Usage
    # Creation is internally handled by the Factory
    product_a = factory.create_product_a()
    product_b = factory.create_product_b()
    # Usage
    product_a.operation()
    product_b.operation()


def client_get_factory(factory_selection: str) -> AbstractFactory:
    factories = {
        'Factory A': ConcreteFactoryA(),
        'Factory B': ConcreteFactoryB()
    }
    if factory_selection in factories:
        return factories[factory_selection]
    print(f"Unknown factory choice {factory_selection}.")


if __name__ == "__main__":
    factory1 = ConcreteFactoryA()
    client_code(factory1)

    factory2 = ConcreteFactoryB()
    client_code(factory2)
    print("----------")
    # Another possibility is to
    factory = client_get_factory('Factory A')
    client_code(factory)
