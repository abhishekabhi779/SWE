import sys

def plot_chain_code(filename):
    directions = {
        '0': (0, 1, '-'),  '4': (0, -1, '-'),
        '1': (-1, 1, '/'), '5': (1, -1, '/'),
        '2': (-1, 0, '|'), '6': (1, 0, '|'),
        '3': (-1, -1, '\\'), '7': (1, 1, '\\')
    }
    
    def draw_line(chain_code):
        x, y = 0, 0
        points = {}
        
        for direction in chain_code:
            dx, dy, char = directions[direction]
            points[(x, y)] = char  # Draw at current position
            x += dx
            y += dy
        
        return points

    def normalize_points(points):
        if not points:
            return []

        min_x = min(x for x, y in points)
        min_y = min(y for x, y in points)
        
        max_x = max(x for x, y in points)
        max_y = max(y for x, y in points)
        
        width = max_y - min_y + 1
        height = max_x - min_x + 1
        
        grid = [[' ' for _ in range(width)] for _ in range(height)]
        
        for (x, y), char in points.items():
            grid[x - min_x][y - min_y] = char
        
        return grid

    with open(filename, 'r') as file:
        chain_codes = file.readlines()
    
    for chain_code in chain_codes:
        chain_code = chain_code.strip().split()
        points = draw_line(chain_code)
        grid = normalize_points(points)
        
        for line in grid:
            print(''.join(line).rstrip())
        print()  # Blank line between each drawing

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python plot_chain_code.py <input_filename>")
        sys.exit(1)

    input_filename = sys.argv[1]
    plot_chain_code(input_filename)