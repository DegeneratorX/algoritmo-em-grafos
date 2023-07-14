#include <iostream>
#include <vector>
#include <deque>
#include <fstream>
#include <sstream>

using namespace std;

struct Edge {
    int source;
    int destination;
    double weight;

    Edge(int src, int dest, double w) : source(src), destination(dest), weight(w) {}
};

class Graph {
private:
    vector<Edge> edgeList;
    int numVertices;
    vector<vector<pair<int, double>>> adjacencyList;

public:
    Graph(const vector<string>& lines, bool hasWeight = false) {
        tie(edgeList, numVertices) = processInput(lines, hasWeight);
        adjacencyList = createAdjacencyList();
    }

    tuple<vector<Edge>, int> processInput(const vector<string>& lines, bool hasWeight) {
        int numVertices = stoi(lines[2].substr(lines[2].find("=") + 1));

        vector<Edge> edgeList;
        for (size_t i = 4; i < lines.size(); i++) {
            istringstream iss(lines[i]);
            int src, dest;
            double weight = 0.0;
            iss >> src >> dest;
            if (hasWeight) {
                iss >> weight;
            }
            edgeList.emplace_back(src, dest, weight);
        }

        return make_tuple(edgeList, numVertices + 1);
    }

    vector<vector<pair<int, double>>> createAdjacencyList() {
        vector<vector<pair<int, double>>> adjList(numVertices);
        for (const auto& edge : edgeList) {
            adjList[edge.source].emplace_back(edge.destination, edge.weight);
        }
        return adjList;
    }

    double maximumFlow(int source, int destination) {
        int n = adjacencyList.size();
        vector<vector<double>> flows(n, vector<double>(n, 0.0));

        while (true) {
            vector<pair<int, int>> path = bfs(flows, source, destination);
            if (path.empty()) {
                break;
            }

            double flow = numeric_limits<double>::max();
            for (const auto& [u, v] : path) {
                flow = min(flow, getCapacity(u, v) - flows[u][v]);
            }

            for (const auto& [u, v] : path) {
                flows[u][v] += flow;
                flows[v][u] -= flow;
            }
        }

        double maxFlow = 0.0;
        for (int i = 0; i < n; i++) {
            maxFlow += flows[source][i];
        }

        return maxFlow;
    }

    double getCapacity(int u, int v) {
        for (const auto& [vertex, weight] : adjacencyList[u]) {
            if (vertex == v) {
                return weight;
            }
        }
        return 0.0;
    }

    vector<pair<int, int>> bfs(const vector<vector<double>>& flows, int source, int destination) {
        deque<int> queue;
        queue.push_back(source);

        vector<vector<pair<int, int>>> paths(numVertices);
        paths[source] = {{-1, -1}};

        while (!queue.empty()) {
            int currentVertex = queue.front();
            queue.pop_front();

            for (const auto& [neighbor, _] : adjacencyList[currentVertex]) {
                if (getCapacity(currentVertex, neighbor) - flows[currentVertex][neighbor] > 0 &&
                    paths[neighbor].empty()) {
                    paths[neighbor] = paths[currentVertex];
                    paths[neighbor].emplace_back(currentVertex, neighbor);

                    if (neighbor == destination) {
                        return paths[neighbor];
                    }

                    queue.push_back(neighbor);
                }
            }
        }

        return {};
    }
};

vector<string> readLinesFromFile(const string& fileName) {
    ifstream file(fileName);
    vector<string> lines;
    string line;
    while (getline(file, line)) {
        lines.push_back(line);
    }
    return lines;
}

void removeTrailingZeroes(double number, stringstream& ss) {
    if (number == static_cast<int>(number)) {
        ss << static_cast<int>(number);
    } else {
        ss << number;
    }
}

void mainFunction() {
    vector<string> lines = readLinesFromFile("Trab3/solucoes/file.in");
    Graph graph(lines, true);

    for (int vertex = 2; vertex < graph.getNumVertices(); vertex++) {
        double maxFlow = graph.maximumFlow(1, vertex);

        stringstream ss;
        ss << vertex << " ";
        removeTrailingZeroes(maxFlow, ss);
        cout << ss.str() << endl;
    }
}

int main() {
    mainFunction();
    return 0;
}