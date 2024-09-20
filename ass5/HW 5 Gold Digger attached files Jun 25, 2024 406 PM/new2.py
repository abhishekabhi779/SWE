import sys
import random

def score_zone(mine, left, right):
    gold_cnt = 0
    element_cnt = {'g': 0, 'o': 0, 'l': 0, 'd': 0}
    rock_cnt = 0
    
    i = left
    while i <= right:
        if mine[i:i+4] == "gold" or mine[i:i+4] == "dlog":
            gold_cnt += 1
            i += 4
        else:
            if mine[i] in element_cnt:
                element_cnt[mine[i]] += 1
            elif mine[i] == '-':
                rock_cnt += 1
            i += 1
    
    size = right - left + 1
    zone_scalar = 1 + (1200 * 2.718281828 ** (-size / 20000)) / 100
    
    return zone_scalar * ((4 * gold_cnt) + (4 * min(element_cnt.values())) - rock_cnt)

def find_best_zones(mine):
    n = len(mine)
    best_zones = []

    def search_zone(existing_zones):
        best_score = float('-inf')
        best_left = best_right = -1
        
        for _ in range(10000):  # Increased number of iterations for better search
            left = random.randint(0, n-1)
            right = random.randint(left, min(left + 20000, n - 1))
            
            if any(left <= z[1] and right >= z[0] for z in existing_zones):
                continue
            
            score = score_zone(mine, left, right)
            if score > best_score:
                best_score = score
                best_left, best_right = left, right
        
        return best_left, best_right, best_score

    for _ in range(5):
        best_result = search_zone(best_zones)
        best_left, best_right, best_score = best_result
        
        if best_left != -1:
            best_zones.append((best_left, best_right))
    
    return sorted(best_zones)

if __name__ == "__main__":
    mine = sys.stdin.read().strip()
    zones = find_best_zones(mine)
    
    if len(zones) != 5:
        print(-1)
    else:
        # Ensure output is exactly 10 integers as required
        output = []
        for left, right in zones:
            output.append(f"{left} {right}")
        print(" ".join(output))
