from ua.univer.lesson07.client import ClientAccount
from ua.univer.lesson07.currency import Currency
from ua.univer.lesson07.order import Order
from ua.univer.lesson07.product import Product

if __name__ == '__main__':
    apple = Product("Apple1", 2, 25)
    print(apple)
    pinapple = Product("PinApple1", 1, 55)
    banana = Product("Banana1", 3, 35)
    client = ClientAccount("Tom",111, 10000)

    order = Order(client)
    order.add(apple)
    order.add(pinapple)
    order.add(banana)
    order.complete()
    order2 = Order(client)
    order2.add(Product("Tomato", 1, 40))
    order2.complete()
    Currency.usd = 30.00
    order.print()
    print("Max price: ", order.get_max_price())
    print("Max weight: ", order.get_max_weight())
    print("Total price with discount=", order.get_total_price_with_discount())
    print(client.order_list)
    print(order)

