from abc import ABC,abstractmethod
class ItemFalse(Exception):
    def __init__(self,mensaje,code_error):
        super().__init__(mensaje)
        self.error=code_error
class ItemTrue(ABC):
    @abstractmethod
    def ItemFree(self,item,storage):
        pass
class Category(ItemTrue): 
    def __init__(self, category_name, content):
        self.category_name = category_name
        self.content = content
    def ItemFree(self, item, storage):
        if item in storage:
            return True
        else:
            raise ItemFalse("item is false/not exist",101)
    def __str__(self):
        return f"Category: {self.category_name}, \nContent: {self.content}"
    def add_content(self, new_items: dict):
        if isinstance(new_items, dict):
            for item, price in new_items.items():
                self.content[item] = price
            print("Content added")
        else:
            raise TypeError("El contenido a añadir debe ser un diccionario.")
    def show_content(self):
        print(f"Category: {self.category_name}")
        for item, price in self.content.items():
            print(f"{item}: ${price}")
    def discard_item(self, Item):
        if self.ItemFree(Item,self.content):
            del self.content[Item]
            print(f"Item: {Item} removed from category")
    def sellItem(self, Item):
        if self.ItemFree(Item,self.content):
            return self.content[Item]
class DiscountCategory(Category):
    def __init__(self, category_name, content, discount_percentage):
        super().__init__(category_name, content)  
        self.discount_percentage = discount_percentage
    def sellItem(self, item):
        if self.ItemFree(item,self.content):
            original_price = super().sellItem(item)
            discounted_price = original_price * (1 - self.discount_percentage / 100)
            return discounted_price
class ClientWallet():
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
        self.cashback_rate = cashback_rate  
    def buy_item(self, amount):
        if amount <= self.wallet_balance:
            super().buy_item(amount)
            cashback = amount * self.cashback_rate
            self.add_funds(cashback)
            print(f"VIP Perk: ${cashback:.2f} added to wallet as cashback!")
        else:
            print("Insufficient funds")
normal_client=ClientWallet('Vladimir',2300)
VIP_client=VIPClientWallet('Elon Bill XD',7900000)
print(normal_client)
print(VIP_client)
fruit=Category('Fruit',{'Apple':5,'Raspberry':13,'Banana':2})