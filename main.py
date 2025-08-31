
from generate_connections import generate_connections

board: dict[int, dict[str, set[int]]] = generate_connections()

start_pos = int(input("Start position: "))
transports = []
while(True):
    transport_type = input("Transport type: ")
    if transport_type == "":
        break
    if transport_type not in ['taxi', 'bus', 'metro', 'hide']:
        print("Invalid transport type. Please enter 'taxi', 'bus', 'metro' or 'hide'.")
        continue
    transports.append(transport_type)


def recurse_route(transports: list[str], routes: list[list[int]], first_recursive_call = True) -> list[list[int]]:
    for i in range(len(routes)):
        current_pos = routes[i][-1]
        current_transport = transports[0]
        next_nodes: set[int] = set()
        if current_transport == 'hide':
            next_nodes.update(board[current_pos].get('taxi', set()))
            next_nodes.update(board[current_pos].get('bus', set()))
            next_nodes.update(board[current_pos].get('metro', set()))
            next_nodes.update(board[current_pos].get('water', set()))
        else:
            next_nodes = board[current_pos].get(current_transport, set())

        for next_node in next_nodes:
            routes.append(routes[i].copy())
            routes[-1].append(next_node)
            if len(transports) > 1:
                for new_route in recurse_route(transports[1:], [routes[-1]], False):
                    routes.append(new_route)

    if first_recursive_call:
        result = []
        for route in routes:
            if len(route) == len(transports) + 1:
                result.append(route)
        return result

    return routes
    

for route in recurse_route(transports, [[start_pos]]):
    print(route)
