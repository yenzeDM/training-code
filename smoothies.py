prices = {"Strawberries": 1.50, "Banana": 0.50, "Mango": 2.50,
          "Blueberries": 1, "Raspberries": 1, "Apple": 1.75,
          "Pineapple": 3.50}


class Beverage:

    def __init__(self, ingredients):
        self.ingredients = ingredients
        self.cost = sum([prices[fruit] for fruit in self.ingredients])
        self.price = self.cost * 2.5

    def get_cost(self):
        return f'${self.cost:.2f}'

    def get_price(self):
        return f'${self.price:.2f}'

    def get_name(self):
        list = sorted([i.replace('ies', 'y') for i in self.ingredients])
        return f'{" ".join(list)} {"Fusion" if len(list) > 1 else "Smoothie"}'
