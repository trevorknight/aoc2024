#include <functional>
#include <iostream>
#include <string>
#include <vector>

using std::cout;
using std::endl;
using std::string;
using std::vector;

struct Grid {
  Grid(vector<string> lines)
      : lines(lines), width(lines[0].size()), height(lines.size()) {}

  const vector<string> lines;
  const int width;
  const int height;
};

Grid createGrid() {
  vector<string> lines;
  std::string line;
  while (std::getline(std::cin, line)) {
    cout << line << endl;
    lines.push_back(line);
  };
  return lines;
}

struct Coord {
  int x;
  int y;
};

using Modifier = std::function<Coord(Coord)>;

void checkDirection(const Grid& grid, const Coord start, Modifier modifier,
                    const string& debug_direction, int& count) {
  Coord coord = start;
  for (char letter : {'X', 'M', 'A', 'S'}) {
    if (coord.x < 0 || coord.x >= grid.width || coord.y < 0 ||
        coord.y >= grid.height) {
      return;
    }
    if (grid.lines[coord.y][coord.x] != letter) {
      return;
    }
    coord = modifier(coord);
  }
  cout << "Found " << debug_direction << " at " << start.x << ", " << start.y
       << endl;
  ++count;
}

int main() {
  Grid grid = createGrid();

  int count = 0;
  for (int y = 0; y < grid.height; ++y) {
    for (int x = 0; x < grid.width; ++x) {
      checkDirection(
          grid, {x, y}, [](Coord in) { return Coord{in.x + 1, in.y}; }, "W->E", count);
      checkDirection(
          grid, {x, y}, [](Coord in) { return Coord{in.x - 1, in.y}; }, "E->W", count);
      checkDirection(
          grid, {x, y}, [](Coord in) { return Coord{in.x, in.y + 1}; }, "N->S", count);
      checkDirection(
          grid, {x, y}, [](Coord in) { return Coord{in.x, in.y - 1}; }, "S->N", count);
      checkDirection(
          grid, {x, y}, [](Coord in) { return Coord{in.x - 1, in.y + 1}; }, "NE->SW", count);
      checkDirection(
          grid, {x, y}, [](Coord in) { return Coord{in.x + 1, in.y - 1}; }, "SW->NE", count);
      checkDirection(
          grid, {x, y}, [](Coord in) { return Coord{in.x + 1, in.y + 1}; }, "NW->SE", count);
      checkDirection(
          grid, {x, y}, [](Coord in) { return Coord{in.x - 1, in.y - 1}; }, "SE->NW", count);
    }
  }
  cout << "Final count: " << count << endl;
  return 0;
}