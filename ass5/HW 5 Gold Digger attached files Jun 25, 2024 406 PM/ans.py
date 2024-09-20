import sys

def read_mine():
    return sys.stdin.read().strip()

def calculate_zone_score(mine, left, right):
    gold = "gold"
    element_cnt = [0] * len(gold)
    gold_cnt = 0
    rock_cnt = 0

    i = left
    while i <= right:
        if mine[i] in gold:
            element_cnt[gold.index(mine[i])] += 1
            if (right - i) >= 3:
                if (mine[i:i+4] == "gold") or (mine[i:i+4] == "dlog"):
                    gold_cnt += 1
                    i += 3
        else:
            rock_cnt += 1
        i += 1

    return (4 * gold_cnt) + (4 * min(element_cnt)) - rock_cnt

def find_zones(mine, num_zones=5):
    mine_length = len(mine)
    zones = []
    window_size = 2000
    step_size = 500

    for _ in range(num_zones):
        best_score = float('-inf')
        best_zone = None

        for left in range(0, mine_length - window_size + 1, step_size):
            right = left + window_size - 1
            if any(left <= z[1] and right >= z[0] for z in zones):
                continue  # Skip if overlapping with existing zones
            
            score = calculate_zone_score(mine, left, right)
            if score > best_score:
                best_score = score
                best_zone = (left, right)

        if best_zone:
            zones.append(best_zone)
        else:
            zones.append((0, 0))  # Add a dummy zone if none found

    return zones

def main():
    mine = read_mine()
    zones = find_zones(mine)
    
    # Sort zones by left index
    zones.sort(key=lambda x: x[0])
    
    # Output the zones
    for zone in zones:
        print(f"{zone[0]} {zone[1]}", end=" ")
    print()  # Newline at the end

if __name__ == "__main__":
    main()