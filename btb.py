import networkx as nx
import argparse
from pathlib import Path

def parse_arguments():
    """
    Process command line arguments.
    @return arguments
    """
    parser = argparse.ArgumentParser(
        description="BowTieBuilder pathway reconstruction"
    )
    parser.add_argument("--network_file", type=Path, required=True,
                        help="Path to the edges file")
    parser.add_argument("--source_file", type=Path, required=True,
                        help="Path to the sources file")
    parser.add_argument("--target_file", type=Path, required=True,
                        help="Path to the targets file")
    parser.add_argument("--output_file", type=Path, required=True,
                        help="Path to the output file that will be written")

    return parser.parse_args()


# functions for reading input files
def read_edges(network_file : Path) -> list:
    network = []
    print(network_file)
    with open(network_file, 'r') as f:
        for line in (f):
            line = line.strip()
            line = line.split('\t')
            network.append((line[0], line[1], float(line[2])))
    return network

def read_source_target(source_file : Path, target_file : Path) -> tuple:
    source = []
    target = []
    with open(source_file, 'r') as f:
        for line in (f):
            line = line.strip()
            source.append(line)
    with open(target_file, 'r') as f:
        for line in (f):
            line = line.strip()
            target.append(line)
    return source, target

# functions for constructing the network
def construct_network(network : list, source : list, target : list) -> nx.DiGraph:
    print(network)
    Network = nx.DiGraph()
    Network.add_weighted_edges_from(network)
    Network.add_nodes_from(source)
    Network.add_nodes_from(target)
    return Network


def update_D(network : nx.DiGraph, i : str, j : str, D : dict) -> None:
        # check if there is a path between i and j
        if nx.has_path(network, i, j):
            D[(i, j)] = [nx.dijkstra_path_length(network, i, j), nx.dijkstra_path(network, i, j)]
        else:
            D[(i, j)] = [float('inf'), []]
            # print(f"There is no path between {i} and {j}")
            
def add_path_to_P(path : list, P : nx.DiGraph) -> None:
        for i in range(len(path) - 1):
            P.add_edge(path[i], path[i + 1])
            
def check_path(network : nx.DiGraph, nodes : list, not_visited : list) -> bool:
    # print(f"Nodes: {nodes}")
    # print(f"Not visited: {not_visited}")
    for n in not_visited:
        for i in set(nodes) - set(not_visited):
            if nx.has_path(network, i, n):
                return True
    return False

def check_visited_not_visited(visited : list, not_visited : list, D : dict) -> tuple:
    # Set initial values
    min_value = float('inf')
    current_path = []
    current_s = ""
    current_t = ""
    for v in visited:
        for n in not_visited:
                    # Since we don't know if the path is from v to n or from n to v, we need to check both cases
                    if (v, n) in D:
                        if D[(v, n)][0] < min_value:
                            min_value = D[(v, n)][0]
                            current_path = D[(v, n)][1]
                            current_s = v
                            current_t = n
                    if (n, v) in D:
                        if D[(n, v)][0] < min_value:
                            min_value = D[(n, v)][0]
                            current_path = D[(n, v)][1]
                            current_s = n
                            current_t = v
                            
    return current_path, current_s, current_t, min_value

def check_not_visited_not_visited(not_visited : list, D : dict) -> tuple:
    # Set initial values
    min_value = float('inf')
    current_path = []
    current_s = ""
    current_t = ""
    for i in range(len(not_visited)):
        for j in range(i + 1, len(not_visited)):
            if (not_visited[i], not_visited[j]) in D:
                if D[(not_visited[i], not_visited[j])][0] < min_value:
                    min_value = D[(not_visited[i], not_visited[j])][0]
                    current_path = D[(not_visited[i], not_visited[j])][1]
                    current_s = not_visited[i]
                    current_t = not_visited[j]
                if (not_visited[j], not_visited[i]) in D:
                    if D[(not_visited[j], not_visited[i])][0] < min_value:
                        min_value = D[(not_visited[j], not_visited[i])][0]
                        current_path = D[(not_visited[j], not_visited[i])][1]
                        current_s = not_visited[j]
                        current_t = not_visited[i]
    return current_path, current_s, current_t, min_value

def BTB_main(Network : nx.DiGraph, source : list, target : list) -> nx.DiGraph:
    # P is the returned pathway
    P = nx.DiGraph()
    P.add_nodes_from(source)
    P.add_nodes_from(target)

    # Step 1
    # Initialize the pathway P with all nodes S union T, and flag all nodes in S union T as 'not visited'.
    not_visited = []
    visited = []

    for i in source:
        not_visited.append(i)
    for j in target:
        not_visited.append(j)
        
    # D is the distance matrix
    # Format
    D = {}
    for i in source:
        # run a single_souce_dijsktra to find the shortest path from source to every other nodes
        # val is the shortest distance from source to every other nodes
        # path is the shortest path from source to every other nodes
        val, path = nx.single_source_dijkstra(Network, i)
        for j in target:
            # if there is a path between i and j, then add the distance and the path to D
            if j in val:
                D[i, j] = [val[j], path[j]]
            else:
                D[i, j] = [float('inf'), []]
                       
    print(f'Original D: {D}')

    # source_target is the union of source and target
    source_target = source + target

    # Index is for debugging (will be removed later)
    index = 1
    
    # need to check if there is a path between source and target 
    while not_visited != []:
        print("\n\nIteration: ", index)
        print(f"Current not visited nodes: {not_visited}")
        
        # Set initial values
        min_value = float('inf')
        current_path = []
        current_s = ""
        current_t = ""
        
        # First checking whether there exists a path from visited nodes to not visited nodes or vise versa
        current_path, current_s, current_t, min_value = check_visited_not_visited(visited, not_visited, D)
            
        # if such a path exists, then we need to update D and P
        if min_value != float('inf'):
            # Set the distance to infinity
            D[(current_s, current_t)] = [float('inf'), []]
                
            # Add the nodes in the current path to visited
            for i in current_path:
                    visited.append(i)
            
            # Remove the nodes in the current path from not_visited
            for i in [current_s, current_t]:
                if i in not_visited:
                    not_visited.remove(i)
                    visited.append(i)
    
        # If such path doesn't exist, then we find a path from a not-visited node to a not-visited node
        else:
            current_path, current_s, current_t, min_value = check_not_visited_not_visited(not_visited, D)
            # If such a path exists, then we need to update D and P
            if min_value != float('inf'):
                D[(current_s, current_t)] = [float('inf'), []]
                # Remove the nodes in the current path from not_visited
                not_visited.remove(current_path[0])
                not_visited.remove(current_path[-1])
                # Add the nodes in the current path to visited
                for i in current_path:
                    visited.append(i)
        
        # Note that if there is no valid path between visited nodes and not visited nodes, then min_value will be infinity
        # In this case, we exit the loop
        if min_value == float('inf'):
            print("There is no path between source and target")
            break
                    
        # If we successfully extract the path, then update the distance matrix (step 5)
        for i in current_path:
            if i not in source_target: 
                # Since D is a matrix from Source to Target, we need to update the distance from source to i and from i to target
                for s in source:
                    update_D(Network, s, i, D)
                for t in target:
                    update_D(Network, i, t, D)
                # Update the distance from i to i
                D[(i, i)] = [float('inf'), []]
                
        # Add the current path to P
        add_path_to_P(current_path, P)
        
        # # some debugging info
        # print(f"Min Value: {min_value}")
        # print(f"Current selected path: {current_path}")
        # print(f"Update D as: {D}")
        # print(f"Update visited nodes as: {visited}")
        # print(f"Update not visited nodes as: {not_visited}")
        # print(f"Add edges to P as: {P.edges}")
        
        index += 1
    
    print(f"\nThe final pathway is: {P.edges}")
    return P

def write_output(output_file, P):
    with open(output_file, 'w') as f:
        f.write('Node1' + '\t' + 'Node2' + '\n')
        for edge in P.edges:
            f.write(edge[0] + '\t' + edge[1] + '\n')

def btb_wrapper(network_file : Path, source_file : Path, target_file : Path, output_file : Path):
    """
    Run BowTieBuilder pathway reconstruction.
    @param network_file: Path to the edge file
    @param source_file: Path to the source file
    @param target_file: Path to the source file
    @param output_file: Path to the output file that will be written
    """
    if not network_file.exists():
        raise OSError(f"Edges file {str(network_file)} does not exist")
    if not source_file.exists():
        raise OSError(f"Sources file {str(source_file)} does not exist")
    if not target_file.exists():
        raise OSError(f"Targets file {str(target_file)} does not exist")
    

    if output_file.exists():
        print(f"Output files {str(output_file)} (nodes) will be overwritten")

    # Create the parent directories for the output file if needed
    output_file.parent.mkdir(parents=True, exist_ok=True)
    
    
    edge_list = read_edges(network_file)
    source, target = read_source_target(source_file, target_file)
    network = construct_network(edge_list, source, target)

    write_output(output_file, BTB_main(network, source, target))

def main():
    """
    Parse arguments and run pathway reconstruction
    """
    args = parse_arguments()
    
    # path length - l
    # test_mode - default to be false
    btb_wrapper(
        args.network_file,
        args.source_file,
        args.target_file,
        args.output_file
    )

if __name__ == "__main__":
    main()
    
# test: python btb.py --edges ./input/edges1.txt --sources ./input/source1.txt --targets ./input/target1.txt --output ./output/output1.txt