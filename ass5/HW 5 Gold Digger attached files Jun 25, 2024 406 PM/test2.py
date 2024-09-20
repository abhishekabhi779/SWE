import sys
import math
import logging

# Configure logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

def find_optimal_zones(mine):
    logging.info("Starting to find optimal zones")
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
            logging.debug(f"Zone added: start={start}, end={end}, score={score}")
            if len(zones) > num_zones:
                # Keep only the top 5 highest scoring zones
                combined = sorted(zip(zones, scores), key=lambda x: x[1], reverse=True)[:num_zones]
                zones, scores = [list(t) for t in zip(*combined)]

    logging.info("Finished finding optimal zones")
    return zones, scores

def calculate_score(counts, width):
    gold_count = min(counts['g'], counts['o'], counts['l'], counts['d'])
    rock_count = counts['-']
    scalar = 1 + (1200.0 * math.exp(-width / 20000.0) / 100.0)
    score = math.floor((4 * gold_count + 4 * gold_count - rock_count) * scalar)
    logging.debug(f"Calculated score: {score} for counts: {counts}")
    return score

def is_non_overlapping(zones, start, end):
    non_overlapping = all(end < zone[0] or start > zone[1] for zone in zones)
    if not non_overlapping:
        logging.debug(f"Overlapping detected for zone: start={start}, end={end}")
    return non_overlapping

def main():
    logging.info("Script started")
    mine = sys.stdin.read().strip()

    if len(mine) != 100000:
        logging.error("Incorrect mine length")
        print(" ".join(["-1"] * 10))
        return

    zones, scores = find_optimal_zones(mine)

    if len(zones) == 5:
        output = " ".join(f"{start} {end}" for start, end in zones)
        logging.info(f"Outputting zones: {output}")
        print(output)
    else:
        logging.error("Incorrect number of zones calculated")
        print(" ".join(["-1"] * 10))

    logging.info("Script finished")

if __name__ == "__main__":
    main()
