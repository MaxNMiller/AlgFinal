import csv
import random

max_connections = 5  # max connections for a single person
max_names = 100  # max number of names


def generate_names(firstnames_filename, lastnames_filename, names_filename):
    with open(firstnames_filename, 'r') as f:
        reader = csv.reader(f)
        firstnames = next(reader)[:max_names]

    with open(lastnames_filename, 'r') as f:
        reader = csv.reader(f)
        lastnames = next(reader)[:max_names]

    random.shuffle(firstnames)
    random.shuffle(lastnames)

    names = [f'{firstname} {lastname}' for firstname,
             lastname in zip(firstnames, lastnames)]

    with open(names_filename, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(names)

def generate_random_graph(names_filename):
    with open(names_filename, 'r') as f:
        reader = csv.reader(f)
        names = next(reader)

    connections = {}

    for name in names:

        # the list of names excluding the current one
        other_names = [
            other_name for other_name in names if other_name != name]

        # a random number of connections
        num_connections = random.randint(
            1, min(len(other_names), max_connections))

        connected_names = random.sample(other_names, num_connections)

        connections[name] = connected_names

    return connections


def write_connections_to_csv(filename, connections):
    with open(filename, 'w', newline='') as f:
        writer = csv.writer(f)

        # header
        writer.writerow(['Name', 'Connections'])

        # data
        for name, connected_names in connections.items():

            # this is to removev quotes from the name and connected names, if we use this in the project we should clean the data instead
            name = name.replace('"', '')
            connected_names = [connected_name.replace('"', '') for connected_name in connected_names]

            writer.writerow([name, ', '.join(connected_names)])

    print(f"CSV file '{filename}' created successfully.")


generate_names('FirstNames.csv', 'LastNames.csv', 'names.csv')
social_graph = generate_random_graph('names.csv')
write_connections_to_csv('social_graph.csv', social_graph)


# for name, connected_names in social_graph.items():
#     print(f'{name} is connected with {connected_names}')
