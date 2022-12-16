class InventoryControl:
    INGREDIENTS = {
        'hamburguer': ['pao', 'carne', 'queijo'],
        'pizza': ['massa', 'queijo', 'molho'],
        'misto-quente': ['pao', 'queijo', 'presunto'],
        'coxinha': ['massa', 'frango'],
    }
    MINIMUM_INVENTORY = {
        'pao': 50,
        'carne': 50,
        'queijo': 100,
        'molho': 50,
        'presunto': 50,
        'massa': 50,
        'frango': 50,
    }

    def __init__(self):
        self._inventory = dict(self.MINIMUM_INVENTORY)

    def add_new_order(self, customer, order, day):
        for ingredient in self.INGREDIENTS[order]:
            if self._inventory[ingredient] <= 0:
                return False
            self._inventory[ingredient] -= 1

    def get_quantities_to_buy(self):
        quantities_to_buy = dict()

        for ingredient in self.MINIMUM_INVENTORY:
            minimun_ingredient_amount = self.MINIMUM_INVENTORY[ingredient]
            actual_ingredient_amount = self._inventory[ingredient]
            amount_difference = (
                minimun_ingredient_amount - actual_ingredient_amount
            )
            quantities_to_buy[ingredient] = amount_difference

        return quantities_to_buy

    def get_available_dishes(self):
        available_ingredients = set()
        available_dishes = set()

        for ingredient in self._inventory:
            if self._inventory[ingredient] > 0:
                available_ingredients.add(ingredient)

        for dish, ingredients in self.INGREDIENTS.items():
            if set(ingredients).issubset(available_ingredients):
                available_dishes.add(dish)

        return available_dishes
