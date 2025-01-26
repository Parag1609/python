from abc import ABC, abstractmethod
from collections import namedtuple

Customer = namedtuple('Customer', 'name fidelity')
class LineItem:
    def __init__(self, product,quantity, price):
        self.quantity= quantity
        self.product= product
        self.price= price
    def total(self):
        return self.price * self.quantity
    
class Order:
    def __init__(self,customer,cart,promotion=None):
        self.customer = customer
        self.cart = list(cart)
        self.promotion = promotion

    def total(self):
        if not hasattr(self,'__total'):
            self.__total=sum(item.total() for item in self.cart)
        return self.__total
    
    def due(self):
        if self.promotion is None:
            discount = 0
        else:
            discount = self.promotion.discount(self)
        return self.total() - discount
    
    def __repr__(self):
        fmt = '<Order total: {:.2f} due: {:.2f}>'
        return fmt.format(self.total(), self.due())
    
class Promotion(ABC):
    @abstractmethod
    def discount(self,order):
        """Return discount as a positive dollar amount"""

class fidelityPromo(Promotion):
    """5% discount for customers with 1000 or more fidelity points"""
    def discount(self, order):
        return order.total() * .05 if order.customer.fidelity >= 1000 else 0
    
class BulkItemPromo(Promotion): 
    """10% discount for each LineItem with 20 or more units"""
    def discount(self, order):
        discount = 0
        for item in order.cart:
            if item.quantity >= 20:
                discount += item.total() * .1
        return discount
    
class LargeOrderPromo(Promotion): # third Concrete Strategy
    """7% discount for orders with 10 or more distinct items"""
    def discount(self, order):
        distinct_items = {item.product for item in order.cart}
        if len(distinct_items) >= 10:
            return order.total() * .07
        return 0
    
if __name__ == "__main__":
    # Customers
    joe = Customer('Joe', 0)
    ann = Customer('Ann', 1100)

    # Cart items
    cart = [
        LineItem('banana', 4, 0.5),
        LineItem('apple', 10, 1.5),
        LineItem('watermelon', 5, 5.0)
    ]

    # Orders with different promotions
    order1 = Order(joe, cart, fidelityPromo())  # Joe doesn't qualify for fidelity promo
    order2 = Order(ann, cart, fidelityPromo())  # Ann qualifies for fidelity promo

    bulk_cart = [LineItem('strawberry', 25, 1.0)]  # Bulk item promotion
    order3 = Order(joe, bulk_cart, BulkItemPromo())

    large_cart = [LineItem(str(item_code), 1, 1.0) for item_code in range(10)]  # 10 distinct items
    order4 = Order(joe, large_cart, LargeOrderPromo())

    # Print order summaries
    print(order1)  # <Order total: 42.00 due: 42.00>
    print(order2)  # <Order total: 42.00 due: 39.90>
    print(order3)  # <Order total: 25.00 due: 22.50>
    print(order4)  # <Order total: 10.00 due: 9.30>