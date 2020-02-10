

def get_index(result, control, vehicles, idx, num_people=0):
    """
    Identify the index in vehicles' list with the min cost

    The vehicles' list must be ordered. This function makes a combination of elements until all passengers have a seat
    in a  car. Then, it chooses the combination with the minimum cost.

    :param result: Dictionary with the best solution, at the end this dictionary have the minimum cost
    :param control: Dictionary where the function build all the combinations recursively
    :param vehicles: vehicles' list
    :param idx: Index of vehicles where the function must start
    :param num_people: Number of people to carry
    """
    for i in range(len(vehicles[idx:])):

        #  Assign the first value of array, and then make the evaluation
        control['idx'].append(idx+i)
        control['carry_passengers'] += vehicles[idx+i]['capacity']
        control['total_cost'] += vehicles[idx+i]['cost']

        # Base case:
        # Remove element and return when the capacity is overloaded
        if control['carry_passengers'] > num_people:
            car_remove = control['idx'].pop()
            control['carry_passengers'] -= vehicles[car_remove]['capacity']
            control['total_cost'] -= vehicles[car_remove]['cost']
            return
        # Save the data when the capacity was achieve
        if control['carry_passengers'] == num_people:
            if not result['total_cost'] or result['total_cost'] > control['total_cost']:
                result['total_cost'] = control['total_cost']
                result['carry_passengers'] = control['carry_passengers']
                result['idx'] = control['idx'][:]
            return

        # For each first element, make a recursive call with a sub-list
        for j, value_2 in enumerate(vehicles[idx+1+i:]):
            get_index(result, control, vehicles, idx+1+j+i, num_people)
            if control['carry_passengers'] == num_people:
                # Reduce data to evaluate
                car_remove = control['idx'].pop()
                control['carry_passengers'] -= vehicles[car_remove]['capacity']
                control['total_cost'] -= vehicles[car_remove]['cost']
                break

        car_remove = control['idx'].pop()
        control['carry_passengers'] -= vehicles[car_remove]['capacity']
        control['total_cost'] -= vehicles[car_remove]['cost']


def puzzle(num_people, vehicles):
    """
    Return least expensive way to send everyone from Bogota to Medellin

    This function order the list for optimizing the combination in "get_index", this order add O(n log(n)) in the worst
    case but reduce the number of comparisons in the search of the best combination
    :param num_people: number of people
    :param vehicles: tuple of vehicles
    :return: minimum cost
    """
    control = {
        'idx': [],
        'carry_passengers': 0,
        'total_cost': 0
    }
    result = {
        'idx': [],
        'carry_passengers': 0,
        'total_cost': None
    }

    vehicles_list = list(vehicles)
    vehicles_list.sort(key=lambda car: car['capacity'])
    get_index(result=result, control=control, vehicles=vehicles_list, idx=0, num_people=num_people)
    # values = tuple(vehicles_list[i] for i in result['idx'])
    return result['total_cost']


if __name__ == "__main__":

    test_vehicles = (
        {'capacity': 10, 'cost': 250},
        {'capacity': 5, 'cost': 50},
        {'capacity': 15, 'cost': 275},
        {'capacity': 6, 'cost': 20},
    )

    assert puzzle(7, test_vehicles) is None
    assert puzzle(15, test_vehicles) == 275
    assert puzzle(16, test_vehicles) == 270
    assert puzzle(17, test_vehicles) is None
