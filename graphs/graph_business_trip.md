# # Code Challenge Class-37: graph_business_trip
In this lab i'm asked to write a functiion that will take the route and the destination, then determen if its possibell or not , if yes return the cost else return Nune. 

# White Bord Class-Class-37: graph_business_trip
![MarineGEO circle logo](/graphs/png/price%20graph.png)









## Approach & Efficiency
| Function | Time Complexity | Space Complexity |
| -------- | -------------- | ---------------- |
| `price`  | O(n*e)    | O (n)           |




## Solution

   def price(graph, cities):
      total = 0
    path_exists = False
    for i in range(len(cities)-1):
        neighbors = graph.show_neighbors(cities[i])
        for neighbor in neighbors:
            if neighbor.vertex.value == cities[i+1].value:
                total += neighbor.weight
                path_exists = True
                break

        if not path_exists:
            return None
    return total