class Package:
    def __init__(self, priority) -> None:
        self.priority = priority

class ShippingOption:
    def __init__(self) -> None:
        pass

    def ship_package(self, package):
        pass

class FirstClassShippingOption(ShippingOption):
    def __init__(self) -> None:
        super().__init__()

    def ship_package(self, package):
        print("Sent via air mail")

class StandardShippingOption(ShippingOption):
    def __init__(self) -> None:
        super().__init__()

    def ship_package(self, package):
        print("Sent via road transport")

class ShippingStrategy:

    def __init__(self, slow_ship, fast_ship) -> None:
        self.slow_ship = slow_ship
        self.fast_ship = fast_ship

    def accept_package(self, package: Package):
        ship_speed = self.slow_ship if package.priority == 1 else self.fast_ship
        ship_speed.ship_package(package)

if __name__ == "__main__":
    shipping_strategy = ShippingStrategy(StandardShippingOption(), FirstClassShippingOption())
    shipping_strategy.accept_package(Package(1))
    shipping_strategy.accept_package(Package(2))
