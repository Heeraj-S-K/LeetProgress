from collections import deque, defaultdict

class Solution:
    def numBusesToDestination(self, routes: list[list[int]], source: int, target: int) -> int:
        # If already at the destination, 0 buses are needed
        if source == target:
            return 0
            
        # Map each bus stop to the routes (bus indices) that pass through it
        stop_to_routes = defaultdict(list)
        for route_id, stops in enumerate(routes):
            for stop in stops:
                stop_to_routes[stop].append(route_id)
                
        # Queue stores elements as tuples: (current_stop, bus_count)
        queue = deque([(source, 0)])
        
        # Track visited entities to prevent infinite loops
        visited_stops = {source}
        visited_routes = set()
        
        while queue:
            curr_stop, bus_count = queue.popleft()
            
            # Loop through all buses that stop at the current station
            for route_id in stop_to_routes[curr_stop]:
                if route_id in visited_routes:
                    continue
                visited_routes.add(route_id)
                
                # Check all stops available on this specific bus line
                for next_stop in routes[route_id]:
                    if next_stop == target:
                        return bus_count + 1
                        
                    if next_stop not in visited_stops:
                        visited_stops.add(next_stop)
                        queue.append((next_stop, bus_count + 1))
                        
        return -1
