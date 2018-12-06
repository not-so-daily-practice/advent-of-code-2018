from collections import defaultdict

file = open("../input/day_4.txt").read().split('\n')
file.sort()  # sort into chronological order

# create dict of dicts
# sleep_times[guard][minute] = number of times sleeping at minute
sleep_times = defaultdict(lambda: defaultdict(int))

guard = None
fell_asleep = None
for line in file:
    words = line.split()
    time = int(words[1][:-1].split(':')[1])

    if 'begins shift' in line:
        guard = int(line.split()[3][1:])
        fell_asleep = None
    elif 'falls asleep' in line:
        fell_asleep = time
    elif 'wakes up' in line:
        for t in range(fell_asleep, time):
            sleep_times[guard][t] += 1


def guard_most_sleep(sleep_times):
    most_sleep = None  # most minutes slept by a guard
    best_guard = None  # best guard (most minutes slept)
    best_minute = None  # minute in which best guard slept the most
    for guard, times in sleep_times.items():
        total_sleep = 0
        for time, count in times.items():
            total_sleep += count

        if best_guard is None or total_sleep > most_sleep:
            most_sleep = total_sleep
            best_guard = guard
            best_minute = max(times, key=times.get)

    return (best_guard * best_minute)


def guard_most_times_minute(sleep_times):
    best_guard = None  # guard which slept the most times at a single minute
    guard_minute = None  # minute at which best guard slept the most
    best_count = None  # number of times best guard slept at their best minute
    for guard, times in sleep_times.items():
        best_minute = max(times, key=times.get)
        count = times[best_minute]

        if best_guard is None or count > best_count:
            best_guard = guard
            guard_minute = best_minute
            best_count = count

    return best_guard * guard_minute


print(guard_most_sleep(sleep_times))
print(guard_most_times_minute(sleep_times))
