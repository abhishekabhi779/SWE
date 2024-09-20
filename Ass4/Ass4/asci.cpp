#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <map>
#include <vector>
#include <algorithm>

struct Point {
    int x, y;
    bool operator<(const Point& other) const {
        return y < other.y || (y == other.y && x < other.x);
    }
};

std::map<char, std::pair<int, int>> moves = {
    {'0', {1, 0}}, {'4', {-1, 0}},
    {'1', {1, -1}}, {'5', {-1, 1}},
    {'2', {0, -1}}, {'6', {0, 1}},
    {'3', {-1, -1}}, {'7', {1, 1}}
};

std::map<char, char> symbols = {
    {'0', '-'}, {'4', '-'},
    {'1', '/'}, {'5', '/'},
    {'2', '|'}, {'6', '|'},
    {'3', '\\'}, {'7', '\\'}
};

void plot_chain_code(const std::string& chain_code, std::map<Point, char>& grid, 
                     int& min_x, int& max_x, int& min_y, int& max_y) {
    int x = 0, y = 0;
    min_x = max_x = min_y = max_y = 0;
    
    std::istringstream iss(chain_code);
    char code;
    while (iss >> code) {
        // Draw at current position first
        grid[{x, y}] = symbols[code];
        
        // Then move
        auto [dx, dy] = moves[code];
        x += dx;
        y += dy;
        
        min_x = std::min(min_x, x);
        max_x = std::max(max_x, x);
        min_y = std::min(min_y, y);
        max_y = std::max(max_y, y);
    }
}

void draw_grid(const std::map<Point, char>& grid, int min_x, int max_x, int min_y, int max_y) {
    for (int y = min_y; y <= max_y; ++y) {
        std::string line;
        for (int x = min_x; x <= max_x; ++x) {
            auto it = grid.find({x, y});
            line += (it != grid.end()) ? it->second : ' ';
        }
        while (!line.empty() && line.back() == ' ') {
            line.pop_back();
        }
        if (!line.empty()) {
            std::cout << line << std::endl;
        }
    }
}

int main(int argc, char* argv[]) {
    if (argc != 2) {
        std::cerr << "Usage: " << argv[0] << " <input_file>" << std::endl;
        return 1;
    }

    std::ifstream file(argv[1]);
    if (!file) {
        std::cerr << "Error: Unable to open file '" << argv[1] << "'" << std::endl;
        return 1;
    }

    std::string line;
    bool first = true;
    while (std::getline(file, line)) {
        if (!first) {
            std::cout << std::endl;
        }
        first = false;

        std::map<Point, char> grid;
        int min_x, max_x, min_y, max_y;
        plot_chain_code(line, grid, min_x, max_x, min_y, max_y);
        draw_grid(grid, min_x, max_x, min_y, max_y);
    }

    return 0;
}