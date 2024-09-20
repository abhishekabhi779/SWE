#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <algorithm>

const int MAX_SIZE = 100;

class ChainCodePlotter {
private:
    std::vector<std::vector<char>> grid;
    int minX, maxX, minY, maxY;
    int curX, curY;

    void initializeGrid() {
        grid = std::vector<std::vector<char>>(MAX_SIZE, std::vector<char>(MAX_SIZE, ' '));
        minX = minY = MAX_SIZE / 2;
        maxX = maxY = MAX_SIZE / 2;
        curX = curY = MAX_SIZE / 2;
    }

    void updateBounds() {
        minX = std::min(minX, curX);
        maxX = std::max(maxX, curX);
        minY = std::min(minY, curY);
        maxY = std::max(maxY, curY);
    }

    void plotCharacter(char ch) {
        grid[curY][curX] = ch;
        updateBounds();
    }

    void move(int direction) {
        switch (direction) {
            case 0: curX++; plotCharacter('-'); break;
            case 1: curX++; curY--; plotCharacter('/'); break;
            case 2: curY--; plotCharacter('|'); break;
            case 3: curX--; curY--; plotCharacter('\\'); break;
            case 4: curX--; plotCharacter('-'); break;
            case 5: curX--; curY++; plotCharacter('/'); break;
            case 6: curY++; plotCharacter('|'); break;
            case 7: curX++; curY++; plotCharacter('\\'); break;
        }
    }

public:
    void plotChainCode(const std::string& code) {
        initializeGrid();
        for (char c : code) {
            if (c >= '0' && c <= '7') {
                move(c - '0');
            }
        }
    }

    void printResult() {
        for (int y = minY; y <= maxY; y++) {
            for (int x = minX; x <= maxX; x++) {
                std::cout << grid[y][x];
            }
            std::cout << std::endl;
        }
    }
};

int main(int argc, char* argv[]) {
    if (argc != 2) {
        std::cerr << "Usage: " << argv[0] << " <input_filename>" << std::endl;
        return 1;
    }

    std::ifstream inputFile(argv[1]);
    if (!inputFile) {
        std::cerr << "Error: Unable to open file " << argv[1] << std::endl;
        return 1;
    }

    ChainCodePlotter plotter;
    std::string line;
    while (std::getline(inputFile, line)) {
        plotter.plotChainCode(line);
        plotter.printResult();
        std::cout << std::endl;  // Add a blank line between plots
    }

    return 0;
}