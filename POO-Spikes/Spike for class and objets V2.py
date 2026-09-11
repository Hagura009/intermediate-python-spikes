class Category: 
    def __init__(self,category_name,content):
        self.category_name = category_name
        self.content = content
    def __str__(self):
        return f"Category: {self.category_name}, \nContent: {self.content}"
    def add_content(self,content):
        self.content.update(content)
    def show_content(self):
        print(f"Category: {self.category_name}")
        for item, price in self.content.items():
            print(f"{item}: ${price}")
    def discard_item(self,content):
        if content in self.content:
            del self.content[content]
            print(f"Item: {content} removed from category")
        else:
            print("Item not found in category")
    def sellItem(self,Item):
        return self.content[Item]
class ClientWallet:
    def __init__(self,client_name,wallet_balance):
        self.client_name = client_name
        self.__wallet_balance = wallet_balance
    @property
    def ClientCategory(self):
        if self.__wallet_balance < 0:
            raise ValueError("Wallet balance cannot be negative")
        elif self.__wallet_balance >= 0 and self.__wallet_balance <= 1000:
            return "Bronze"
        elif self.__wallet_balance > 1000 and self.__wallet_balance <= 5000:
            return "Silver"
        elif self.__wallet_balance > 5000:
            return "Gold"
    def __str__(self):
        return f"Client: {self.client_name}, ClientCategory: {self.ClientCategory}"
    def add_funds(self,amount):
        if amount > 0:
            self.__wallet_balance += amount
        elif amount <=0:
            raise ValueError("No value could be added because the value provided is less than or equal to 0.")
    def buy_item(self,amount):
        if amount <= 0:
            raise ValueError ('invalid item, equal or lower to 0')
        if amount <= self.__wallet_balance:
            self.__wallet_balance -= amount
            print(f"Purchase successful!")
        else:
            print("Insufficient funds")
category_1=Category('Electronics',{'Clock':150,'CellPhone':300,'Tablet':500,'LapTop':1500})
category_1.show_content()
category_1.discard_item('Tablet')
category_1.add_content({'Mouse':50})
category_1.show_content()
client_1 =ClientWallet('Will Fork',4500)
print(client_1)
client_1.buy_item(category_1.sellItem('LapTop'))
client_1.add_funds(2500)
print(client_1)
