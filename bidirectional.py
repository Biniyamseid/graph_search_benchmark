import collections
from graph import Graph

Oradea="Oradea"
Zerind="Zerind" 
Arad="Arad" 
Timisoara="Timisoara"
Lugoj="Lugoj"
Mehadia="Mehadia" 
Drobeta="Drobeta"  
Craiova="Craiova"   
Sibiu="Sibiu"
Rimnicu_Vilcea="Rimnicu Vilcea"   
Fagaras="Fagaras"
Pitesti="Pitesti"
Giurgiu="Giurgiu"
Bucharest="Bucharest"    
Urziceni="Urziceni"   
Eforie="Eforie"  
Hirsova="Hirsova"   
Vaslui="Vaslui"  
Iasi="Iasi"  
Neamt="Neamt"   

cities = {}
with open("cities.txt", "r") as file:
    # Skip the header line
    next(file)
    
    for line in file:
        information = (line.strip().split("   "))
        if len(information) == 4:
            information[1] = information[0]+information[1]
            information = information[1:]
        city, longitude, latitude = information
        cities[city] = (float(longitude), float(latitude))
# print(cities)



def bidirectional_search(graph, start, end):
    # Set up the starting and ending nodes

    start_frontier = [(start, [])]
    end_frontier = [(end, [])]
    start_explored = set()
    end_explored = set()
    
    # Search for a path using bidirectional search
    while start_frontier and end_frontier:
        # Explore from the starting node
        current, path = start_frontier.pop(0)
        start_explored.add(current)
        for neighbors in graph.adjacencyList[current]:
            neighbor = neighbors[0]
            if neighbor not in start_explored:
                new_path =[]
                new_path += path
                if current not in path:
                     new_path.append(current)
                if neighbor not in path:
                     new_path.append(neighbor)
                
                if neighbor == end:
                    return new_path
                start_frontier.append((neighbor, new_path))
        
        # Explore from the ending node
        current, path = end_frontier.pop(0)
        end_explored.add(current)
        for neighbors in graph.adjacencyList[current]:
            neighbor = neighbors[0]
            if neighbor not in end_explored:
                new_path =[]
                if neighbor not in path:
                     new_path.append(neighbor)
                if current not in path:
                     new_path.append(current)
                new_path += path
                if neighbor == start:
                    return new_path
                end_frontier.append((neighbor, new_path))
    
    # No path was found
    return []




graph = Graph()
#edge list of the graph on our text book
edgeList = [(Oradea,Sibiu),(Oradea,Zerind),(Zerind,Arad),(Arad,Sibiu),(Arad,Timisoara),(Timisoara,Lugoj),(Lugoj,Mehadia),(Mehadia,Drobeta),(Craiova,Drobeta),(Craiova,Rimnicu_Vilcea),(Giurgiu,Bucharest),(Bucharest,Pitesti),(Urziceni,Bucharest),(Hirsova,Eforie),(Hirsova,Urziceni),(Vaslui,Iasi),(Vaslui,Urziceni),(Neamt,Iasi),(Rimnicu_Vilcea,Sibiu),(Rimnicu_Vilcea,Pitesti),(Fagaras,Sibiu),(Fagaras,Bucharest),(Pitesti,Craiova)]
for source,destination in edgeList:
    if not graph.nodeExists(source):
            graph.addNode(source)
    if not  graph.nodeExists(destination):
            graph.addNode(destination)
    distance = ((cities[source][0] - cities[destination][0])**2+(cities[source][1] - cities[destination][1])**2)**0.5
    graph.addUndirectedEdge(source,destination,distance,distance)
# graph.show()
# print(bidirectional_search2(graph,Oradea,Neamt))
print(bidirectional_search(graph,Craiova,Neamt))
print(bidirectional_search(graph,Bucharest,Timisoara))
print(bidirectional_search(graph,Mehadia,Neamt))
print(bidirectional_search(graph,Craiova,Vaslui))
print(bidirectional_search(graph,Timisoara,Craiova))
print(bidirectional_search(graph,Lugoj,Mehadia))
print(bidirectional_search(graph,Timisoara,Vaslui))
print(bidirectional_search(graph,Arad,Zerind))
print(bidirectional_search(graph,Craiova,Zerind))
print(bidirectional_search(graph,Arad,Oradea))


#average time taken
import timeit

# Measure the time taken by the function using timeit
start_node = Bucharest
end_node = Neamt
num_runs = 10
time_taken = timeit.timeit(lambda: bidirectional_search(graph, start_node, end_node), number=num_runs)

# Calculate the average time taken
avg_time_taken = time_taken / num_runs

print("Average time taken:", avg_time_taken)
answer = bidirectional_search(graph,start_node,end_node)
print("the length of the solution is:", len(answer))



