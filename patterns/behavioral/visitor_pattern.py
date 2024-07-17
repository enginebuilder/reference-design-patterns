class ProductOperation:
    def visit_storage(self, storage):
        pass
    def visit_compute(self, compute):
        pass

class Product:
    def __init__(self, type) -> None:
        self.type = type

    def accept(self, product_operation):
        pass

class Storage(Product):
    def __init__(self, type) -> None:
        super().__init__(type)

    def get_capacity(self):
        return "1 TB"
    
    def accept(self, product_operation):
        product_operation.visit_storage(self)

class Compute(Product):
    def __init__(self, type) -> None:
        super().__init__(type)

    def get_speed(self):
        return "4 Ghz"
    
    def accept(self, product_operation):
        product_operation.visit_compute(self)

class GenerateCapacity(ProductOperation):
    def visit_compute(self, compute):
        print(f" Compute speed {compute.get_speed()}")

    def visit_storage(self, storage):
        print(f"Storage capacity: {storage.get_capacity()}")

if __name__ == "__main__":
    compute = Compute("general")
    storage = Storage("mini")
    capacity_generator = GenerateCapacity()
    compute.accept(capacity_generator)
    storage.accept(capacity_generator)
