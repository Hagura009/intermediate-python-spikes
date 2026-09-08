class category:
    def __init__(self,category_name,content):
        self.category_name = category_name
        self.content = content
    def __str__(self):
        return f"Category: {self.category_name}, Content: {self.content}"
    def add_content(self,content):
        self.content.update(content)
    def show_content(self):
        print(f"Category: {self.category_name}")
        for item, price in self.content.items():
            print(f"{item}: ${price}")
    def discard_item(self,content):
        self.content.pop(content)
category1 = category("Electronics", {"Laptop": 1000, "Smartphone": 500})
new_content = {"Tablet": 300, "Headphones": 100}
category1.add_content(new_content)
category1.discard_item("Smartphone")
category1.show_content()
