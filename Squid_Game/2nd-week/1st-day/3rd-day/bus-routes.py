class Solution(object):
    def numBusesToDestination(self, routes, source, target):
        buses = defaultdict(list)
        stops = defaultdict(list)

        for i in range(len(routes)):
            for j in routes[i]:
                buses[j] += [i]
                stops[i] += [j]

        
        queue = [(source, 0)]
        visited = set()

        while queue:

            stop, num_buses = queue.pop(0)

            if stop == target:
                return num_buses

            for bus in buses[stop]:
                if bus not in visited:
                    visited.add(bus)
                    for nextstop in stops[bus]:
                        queue.append((nextstop, num_buses + 1))
        
        return -1