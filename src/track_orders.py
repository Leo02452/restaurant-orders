def get_customer_never(
    subject: str, customer: str, list: list, complete_set: set
):
    customer_set = set()
    for order in list:
        if order['customer'] == customer:
            customer_set.add(order[subject])
    return complete_set.difference(customer_set)


def get_most(subject: str, list: list, customer: str = None):
    counter_dict = dict()
    min_count = 0
    most_subject = ''

    for order in list:
        if (
            order['customer'] == customer
            or customer is None
        ):
            if order[subject] not in counter_dict:
                counter_dict[order[subject]] = 1
            else:
                counter_dict[order[subject]] += 1
            if counter_dict[order[subject]] > min_count:
                min_count = counter_dict[order[subject]]
                most_subject = order[subject]
    return most_subject


class TrackOrders:
    def __init__(self) -> None:
        self._data = []
        self._all_costumers = set()
        self._all_dishes = set()
        self._all_days = set()

    def __len__(self):
        return len(self._data)

    def add_new_order(self, customer, order, day):
        self._data.append({
            'customer': customer,
            'dish': order,
            'day': day
        })
        self._all_costumers.add(customer)
        self._all_dishes.add(order)
        self._all_days.add(day)

    def get_most_ordered_dish_per_customer(self, customer):
        return get_most(
            'dish', self._data, customer
        )

    def get_never_ordered_per_customer(self, customer):
        return get_customer_never(
            'dish', customer, self._data, self._all_dishes
        )

    def get_days_never_visited_per_customer(self, customer):
        return get_customer_never(
            'day', customer, self._data, self._all_days
        )

    def get_busiest_day(self):
        return get_most(
            'day', self._data
        )

    def get_least_busy_day(self):
        open_days_counter = dict()
        day_volume = 1
        least_busy_day = ''

        for order in self._data:
            if order['day'] not in open_days_counter:
                open_days_counter[order['day']] = 1
            else:
                open_days_counter[order['day']] += 1
            if open_days_counter[order['day']] <= day_volume:
                day_volume = open_days_counter[order['day']]
                least_busy_day = order['day']
        return least_busy_day
