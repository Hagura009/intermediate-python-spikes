class Category: 
    def __init__(self, category_name, content):
        self.category_name = category_name
        self.content = content

    def __str__(self):
        return f"Category: {self.category_name}, \nContent: {self.content}"

    def add_content(self, content):
        self.content.update(content)

    def show_content(self):
        print(f"Category: {self.category_name}")
        for item, price in self.content.items():
            print(f"{item}: ${price}")

    def discard_item(self, content):
        if content in self.content:
            del self.content[content]
            print(f"Item: {content} removed from category")
        else:
            print("Item not found in category")
    def sellItem(self, item):
        return self.content[item]

class DiscountCategory(Category):
    def __init__(self, category_name, content, discount_percentage):
        super().__init__(category_name, content)  # Uso de super()
        self.discount_percentage = discount_percentage

    def sellItem(self, item):
        original_price = super().sellItem(item)
        discounted_price = original_price * (1 - self.discount_percentage / 100)
        return discounted_price


class ClientWallet:
    def __init__(self, client_name, wallet_balance):
        self.client_name = client_name
        self.__wallet_balance = wallet_balance

    @property
    def wallet_balance(self):
        return self.__wallet_balance

    @property
    def ClientCategory(self):
        if self.__wallet_balance < 0:
            raise ValueError("Wallet balance cannot be negative")
        elif self.__wallet_balance <= 1000:
            return "Bronze"
        elif self.__wallet_balance <= 5000:
            return "Silver"
        else:
            return "Gold"

    def __str__(self):
        return f"Client: {self.client_name}, ClientCategory: {self.ClientCategory}, Balance: ${self.__wallet_balance}"

    def add_funds(self, amount):
        if amount > 0:
            self.__wallet_balance += amount
        else:
            raise ValueError("No value could be added because the value provided is less than or equal to 0.")
    def buy_item(self, amount):
        if amount <= 0:
            raise ValueError('invalid item, equal or lower to 0')
        if amount <= self.__wallet_balance:
            self.__wallet_balance -= amount
            print(f"Purchase successful! Remaining balance: ${self.__wallet_balance}")
        else:
            print("Insufficient funds")
class VIPClientWallet(ClientWallet):
    def __init__(self, client_name, wallet_balance, cashback_rate=0.05):
        super().__init__(client_name, wallet_balance)
        self.cashback_rate = cashback_rate  # 5% de cashback por defecto
    def buy_item(self, amount):
        if amount <= self.wallet_balance:
            super().buy_item(amount)
            cashback = amount * self.cashback_rate
            self.add_funds(cashback)
            print(f"VIP Perk: ${cashback:.2f} added to wallet as cashback!")
        else:
            print("Insufficient funds")
