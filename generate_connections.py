
from time import sleep

def generate_connections(file_name: str = 'connections.txt') -> dict[int, dict[str, set[int]]]:

    result: dict[int, dict[str, set[int]]] = {}

    f = open(file_name, 'r')
    while(True):
        line = f.readline()
        if not line:
            break

        data = line.split(' ')
        first_node = int(data[0])
        second_node = int(data[1])
        transport_type = data[2][:-1]

        if result.get(first_node) is None:
            result[first_node] = {}
        if result.get(second_node) is None:
            result[second_node] = {}
        if result[first_node].get(transport_type) is None:
            result[first_node][transport_type] = set()
        if result[second_node].get(transport_type) is None:
            result[second_node][transport_type] = set()
        
        result[first_node][transport_type].add(second_node)
        result[second_node][transport_type].add(first_node)
    
    return result
