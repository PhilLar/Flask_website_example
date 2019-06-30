class Product:
    def __init__(self, name, price, kal ):
        self.name = name
        self.price = price
        self.kal = kal


bread = Product('bread', 100, 60)
oil = Product('oil', 100, 50)

l = list()
l.append(bread)
l.append(oil)
l.sort(key=lambda x: int(x.price)/int(x.kal))
for i in l:
    print(i.name)