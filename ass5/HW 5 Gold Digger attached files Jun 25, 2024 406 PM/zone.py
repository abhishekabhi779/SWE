import sys
if __name__ == "__main__":
    mine = sys.stdin.read().strip()
    print(f"Read {len(mine)} characters from input.")
    # ... rest of the code
    import sys

    def score_zone(mine, left, right):
        gold_cnt = 0
        element_cnt = {'g': 0, 'o': 0, 'l': 0, 'd': 0}
        rock_cnt = 0
        
        for i in range(left, right + 1):
            if mine[i] in element_cnt:
                element_cnt[mine[i]] += 1
            elif mine[i] == '-':
                rock_cnt += 1
        
        for i in range(left, right - 2):
            if mine[i:i+4] in ["gold", "dlog"]:
                gold_cnt += 1
        
        size = right - left + 1
        zone_scalar = 1 + (1200 * 2.718281828 ** (-size / 20000)) / 100
        
        return zone_scalar * ((4 * gold_cnt) + (4 * min(element_cnt.values())) - rock_cnt)

    def find_best_zones(mine):
        n = len(mine)
        best_zones = []
        
        for start in range(0, n, n // 10):
            end = min(start + n // 5, n - 1)
            while start < end:
                score = score_zone(mine, start, end)
                if not any(start <= z[1] and end >= z[0] for z in best_zones):
                    best_zones.append((start, end, score))
                    break
                end -= 1
            
            if len(best_zones) == 5:
                break
        
        return sorted(best_zones)[:5]

    if __name__ == "__main__":
        mine = sys.stdin.read().strip()
        zones = find_best_zones(mine)
        
        if len(zones) != 5:
            print(-1)
        else:
            print(" ".join(f"{left} {right}" for left, right, _ in zones))