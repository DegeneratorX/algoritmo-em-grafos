#include <iostream>
#include <fstream>
#include <vector>
#include <queue>
#include <set>
#include <algorithm>

using namespace std;

void read_data(const string& filename, int& n, vector<pair<int, int>>& data) {
    ifstream file(filename);
    vector<string> lines;
    string line;
    while (getline(file, line)) {
        lines.push_back(line);
    }
    file.close();

    n = stoi(lines[2].substr(2));
    for (int i = 4; i < lines.size(); i++) {
        int x, y;
        sscanf(lines[i].c_str(), "%d %d", &x, &y);
        data.push_back(make_pair(x - 1, y - 1));
    }
}

void write_data(const vector<vector<int>>& components) {
    for (const auto& component : components) {
        for (int node : component) {
            cout << node + 1 << " ";
        }
        cout << endl;
    }
}

void find_connected_components(int n, const vector<pair<int, int>>& data, vector<vector<int>>& components) {
    vector<set<int>> graph(n);
    for (const auto& edge : data) {
        graph[edge.first].insert(edge.second);
        graph[edge.second].insert(edge.first);
    }

    set<int> visited;
    for (int i = 0; i < n; i++) {
        if (visited.count(i) == 0) {
            set<int> component;
            queue<int> q;
            q.push(i);
            visited.insert(i);

            while (!q.empty()) {
                int node = q.front();
                q.pop();
                component.insert(node);
                for (int neighbor : graph[node]) {
                    if (visited.count(neighbor) == 0) {
                        visited.insert(neighbor);
                        q.push(neighbor);
                    }
                }
            }

            vector<int> component_vec(component.begin(), component.end());
            sort(component_vec.begin(), component_vec.end());
            components.push_back(component_vec);
        }
    }
}

int main() {
    for (int arqs = 0; arqs < 120; arqs++) {
        cout << endl;
        cout << "Arquivo " << arqs << endl;
        int n;
        vector<pair<int, int>> data;
        read_data("exemplos/instancias/" + to_string(arqs) + ".in", n, data);
        vector<vector<int>> components;
        find_connected_components(n, data, components);
        write_data(components);
        cout << endl;
    }
    return 0;
}