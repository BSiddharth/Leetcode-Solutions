# https://leetcode.com/problems/reconstruct-itinerary/description/
# git add . && git commit -m "completed reconstruct_itinerary" && git push && exit

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adjacency_list = {}

        for ticket in tickets:
            source,destination = ticket[0],ticket[1]
            if source not in adjacency_list:
                adjacency_list[source] = []
            if destination not in adjacency_list:
                adjacency_list[destination] = []
            adjacency_list[source].append(destination)

        for source in adjacency_list:
            adjacency_list[source].sort()
            
        exhuasted_intinerary = {x:[False for _ in range(len(adjacency_list[x]))] for x in adjacency_list}
        visited = []
        def helper(current_airport):
            visited.append(current_airport)
            if len(visited) == len(tickets) + 1:
                return visited

            for index in range(len(adjacency_list[current_airport])):
                next_airport = adjacency_list[current_airport][index]

                if (exhuasted_intinerary[current_airport][index]) or ((index - 1 >= 0) and adjacency_list[current_airport][index] == adjacency_list[current_airport][index-1] and not exhuasted_intinerary[current_airport][index-1]):
                    continue

                exhuasted_intinerary[current_airport][index] = True
                result = helper(next_airport)

                if len(result) == len(tickets) + 1:
                    return result
                
                exhuasted_intinerary[current_airport][index] = False

            visited.pop()
            return []

        return helper("JFK")
