# trying to use vanilla python
# would be much easier with numpy!

# part 1
from collections import Counter
from itertools import product


def largest_area(filename):
    file = open(filename).read().split('\n')

    all_points = {}  # set of all points in input
    id = 0
    for line in file:
        y, x = line.split(',')
        all_points[id] = (int(y), int(x))
        id += 1

    # dimensions of area to check
    max_x = max(all_points.items(), key=lambda kv: kv[1][0])[1][0]
    max_y = max(all_points.items(), key=lambda kv: kv[1][1])[1][0]

    area_map = [[-1] * max_x for i in range(max_y)]  # map of which locations are closest to each point

    for x, y in product(range(len(area_map[0])), range(len(area_map))):
        nearest_id = None
        nearest_dist = None
        for id, point in all_points.items():
            dist = (abs(point[0] - y)) + (abs(point[1] - x))
            if nearest_id is None or dist < nearest_dist:
                # closer than existing point, update
                nearest_id = id
                nearest_dist = dist
            elif dist == nearest_dist:
                # equally close points don't count
                nearest_id = -1

        area_map[y][x] = nearest_id

    edge_areas = {-1}
    # find id's of areas which extend to infinity
    for x in range(len(area_map[0])):
        edge_areas.add(area_map[0][x])
        edge_areas.add(area_map[-1][x])

    for y in range(len(area_map)):
        edge_areas.add(area_map[y][0])
        edge_areas.add(area_map[y][-1])

    flattened_area = [id for sublist in area_map for id in sublist]
    # clean up id's which have an area of infinity
    flattened_area = [x for x in flattened_area if x not in edge_areas]

    max_area_id = Counter(flattened_area).most_common()

    return max_area_id[0][1]


print(largest_area("../input/day_6.txt"))
