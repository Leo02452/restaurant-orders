import csv
from src.track_orders import TrackOrders


def analyze_log(path_to_file: str):
    if not path_to_file.endswith('.csv'):
        raise FileNotFoundError(f'Extensão inválida {path_to_file}')

    track_orders = TrackOrders()
    try:
        with open(path_to_file) as file:
            csv_reader = csv.reader(file, delimiter=",")
            for customer, order, day in csv_reader:
                track_orders.add_new_order(customer, order, day)
    except FileNotFoundError:
        raise FileNotFoundError(f'Arquivo inexistente: {path_to_file}')

    most_ordered = track_orders.get_most_ordered_dish_per_customer('maria')
    ordered_times = track_orders.get_quantity_ordered_per_customer('arnaldo', 'hamburguer')
    never_ordered = track_orders.get_never_ordered_per_customer('joao')
    visited_days = track_orders.get_days_never_visited_per_customer('joao')   

    file_to_write = 'data/mkt_campaign.txt'
    with open(file_to_write, 'a') as log_file:
        log_file.write(
            f'{most_ordered}\n{ordered_times}\n{never_ordered}\n{visited_days}'
        )
