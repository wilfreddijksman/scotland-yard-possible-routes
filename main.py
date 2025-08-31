
from generate_connections import generate_connections


def find_nodes(transports: list[str], current_nodes: set[int]) -> set[int]:
    new_nodes: set[int] = set()
    for current_node in current_nodes:
        current_transport = transports[0]
        next_nodes: set[int] = set()
        if current_transport == 'hide':
            next_nodes.update(board[current_node].get('taxi', set()))
            next_nodes.update(board[current_node].get('bus', set()))
            next_nodes.update(board[current_node].get('metro', set()))
            next_nodes.update(board[current_node].get('water', set()))
        else:
            next_nodes = board[current_node].get(current_transport, set())

        if len(transports) > 1:
            new_nodes.update(find_nodes(transports[1:], next_nodes))
        else:
            new_nodes.update(next_nodes)

    return new_nodes


board: dict[int, dict[str, set[int]]] = generate_connections()

def main():
    nodes: set[int] = {int(input("Start position: "))}
    while(True):
        transports = []
        transport_type = input("Transport type: ")
        if transport_type == "":
            break
        if transport_type not in ['taxi', 'bus', 'metro', 'hide']:
            print("Invalid transport type. Please enter 'taxi', 'bus', 'metro' or 'hide'.")
            continue
        transports.append(transport_type)

        nodes = find_nodes(transports, nodes)
        list_nodes = list(nodes)
        if len(list_nodes) <= 0:
            print("Transport not possible!")
            transports.pop()
            continue

        list_nodes.sort()
        print("Possible locations:")
        for node in list_nodes:
            print(node)


if __name__ == "__main__":
    main()
