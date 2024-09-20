import sys
import math

def find_optimal_zones(mine):
    mine_length = len(mine)
    zone_size = 2000  # Defined zone size
    num_zones = 5  # Number of zones to find
    zones = []
    scores = []

    # Initialize character counts within the window
    current_counts = {'g': 0, 'o': 0, 'l': 0, 'd': 0, '-': 0}
    for i in range(zone_size):
        if mine[i] in current_counts:
            current_counts[mine[i]] += 1

    # Use a sliding window to calculate scores for zones
    for start in range(mine_length - zone_size + 1):
        end = start + zone_size - 1
        if start != 0:
            # Update counts for the sliding window
            current_counts[mine[start - 1]] -= 1
            current_counts[mine[end]] += 1

        score = calculate_score(current_counts, zone_size)
        if is_non_overlapping(zones, start, end):
            zones.append((start, end))
            scores.append(score)
            if len(zones) > num_zones:
                # Keep only the top 5 highest scoring zones
                combined = sorted(zip(zones, scores), key=lambda x: x[1], reverse=True)[:num_zones]
                zones, scores = [list(t) for t in zip(*combined)]

    return zones, scores

def calculate_score(counts, width):
    gold_count = min(counts['g'], counts['o'], counts['l'], counts['d'])
    rock_count = counts['-']
    scalar = 1 + (1200.0 * math.exp(-width / 20000.0) / 100.0)
    return math.floor((4 * gold_count + 4 * gold_count - rock_count) * scalar)

def is_non_overlapping(zones, start, end):
    return all(end < zone[0] or start > zone[1] for zone in zones)

def main():
    mine = sys.stdin.read().strip()

    if len(mine) != 100000:
        print(" ".join(["-1"] * 10))
        return

    zones, scores = find_optimal_zones(mine)

    if len(zones) == 5:
        output = " ".join(f"{start} {end}" for start, end in zones)
        print(output)
    else:
        print(" ".join(["-1"] * 10))

if __name__ == "__main__":
    main()