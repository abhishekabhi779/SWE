import sys
import random
import math
import logging

logging.basicConfig(filename='debug.log', level=logging.DEBUG)

def score_zone(mine, left, right):
    gold = "gold"
    element_cnt = [0] * len(gold)
    gold_cnt = 0
    rock_cnt = 0
    i = left
    while i <= right:
        if mine[i] in gold:
            element_cnt[gold.index(mine[i])] += 1
            if (right - i) >= 3:
                if (mine[i:i + 4] == "gold") or (mine[i:i + 4] == "dlog"):
                    gold_cnt += 1
                    for c in mine[i + 1:i + 4]:
                        element_cnt[gold.index(c)] += 1
                    i += 3
        else:
            rock_cnt += 1
        i += 1
    width = right - left + 1
    scalar = 1 + (1200.0) * math.exp(-width / 20000.0) / 100.0
    score = ((4 * gold_cnt) + (4 * min(element_cnt) - rock_cnt)) * scalar
    logging.debug(f"Scored zone {left}-{right} with score {score}")
    return score

def find_best_zones(mine):
    best_zones = []
    best_score = -float('inf')
    attempts = 10000

    while attempts > 0:
        zones = []
        valid = True
        for _ in range(5):
            left = random.randint(0, 99995)
            right = random.randint(left, min(left + 20000, 99999))
            zones.append((left, right))
        logging.debug(f"Generated zones: {zones}")
        # Check for overlap
        for i in range(len(zones)):
            for j in range(i + 1, len(zones)):
                if not (zones[i][1] < zones[j][0] or zones[j][1] < zones[i][0]):
                    valid = False
                    break
            if not valid:
                break
        if valid:
            score = sum(score_zone(mine, left, right) for left, right in zones)
            if score > best_score:
                best_score = score
                best_zones = zones
        attempts -= 1
    logging.debug(f"Best zones found: {best_zones} with score {best_score}")
    return best_zones, best_score

if __name__ == "__main__":
    mine = sys.stdin.read().strip()
    zones, best_score = find_best_zones(mine)
    if len(zones) != 5:
        print(-1)
    else:
        for left, right in zones:
            print(left, right)
        print(f"Best score: {best_score}")
