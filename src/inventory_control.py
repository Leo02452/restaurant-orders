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
            self._inventory[ingredient] -= 1

    def get_quantities_to_buy(self):
        quantities_to_buy = dict()

        for ingredient in self.MINIMUM_INVENTORY:
            amount_difference = self.MINIMUM_INVENTORY[ingredient] - self._inventory[ingredient]
            quantities_to_buy[ingredient] = amount_difference
            
        return quantities_to_buy
