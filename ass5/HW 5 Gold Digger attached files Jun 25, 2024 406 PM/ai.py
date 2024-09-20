import sys

def find_optimal_zones(mine):
    mine_length = len(mine)
    zone_size = 2000  # Adjust size as needed
    num_zones = 5
    zones = []
    scores = []

    # Define interval to avoid overlaps and maximize the potential of each zone
    interval = mine_length // num_zones
    
    for i in range(num_zones):
        best_score = -float('inf')
        best_zone = None
        start_index = i * interval

        for start in range(start_index, start_index + interval - zone_size + 1):
            end = start + zone_size - 1
            if end >= mine_length:
                break
            score = evaluate_zone(mine, start, end)
            if score > best_score:
                best_score = score
                best_zone = (start, end)

        if best_zone:
            zones.append(best_zone)
            scores.append(best_score)

    return zones

def evaluate_zone(mine, start, end):
    counts = {'g': 0, 'o': 0, 'l': 0, 'd': 0, '-': 0}
    for i in range(start, end + 1):
        if mine[i] in counts:
            counts[mine[i]] += 1

    gold_count = min(counts['g'], counts['o'], counts['l'], counts['d'])
    rock_count = counts['-']
    return (4 * gold_count) - rock_count

def main():
    if len(sys.argv) < 2:
        print("Usage: python script.py <input_file>")
        sys.exit(1)

    with open(sys.argv[1], 'r') as file:
        mine = file.read().strip()

    if not mine:
        print("No data found in file.")
        return

    zones = find_optimal_zones(mine)

    if zones:
        output = " ".join(f"{start} {end}" for start, end in zones)
        print(output)  # Output only the indices

if __name__ == "__main__":
    main()
