#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <deque>
#include <algorithm>
#include <limits>

/**
 * Trabalho 3 do run.codes de Algoritmos em Grafos feito em python.
 * Usando apenas Lista de Adjacências para vizinhos e Matriz de Adjacências 
 * para acesso rápido das capacidades
 */

class Grafo {
public:
    std::vector<std::vector<int>> lista_adj;
    std::vector<std::vector<float>> capacidades;

    Grafo(const std::vector<std::string>& linhas, bool tem_peso = false) {
        tratamento_dos_dados(linhas, tem_peso);
    }

    float fluxo_maximo(int origem, int destino) {
        int n = lista_adj.size();
        std::vector<std::vector<float>> fluxos(n, std::vector<float>(n, 0));

        while (true) {
            std::vector<std::pair<int, int>> caminho = bfs(fluxos, origem, destino);
            if (caminho.empty()) {
                break;
            }

            float fluxo = std::numeric_limits<float>::max();
            for (const auto& [u, v] : caminho) {
                float capacidade = capacidades[u][v] - fluxos[u][v];
                fluxo = std::min(fluxo, capacidade);
            }

            for (const auto& [u, v] : caminho) {
                fluxos[u][v] += fluxo;
                fluxos[v][u] -= fluxo;
            }
        }

        float fluxo_total = 0;
        for (int i = 0; i < n; ++i) {
            fluxo_total += fluxos[origem][i];
        }

        return fluxo_total;
    }

private:
    void tratamento_dos_dados(const std::vector<std::string>& linhas, bool tem_peso) {
        int num_vertices = stoi(linhas[2].substr(linhas[2].find('=') + 1));

        std::vector<std::vector<float>> lista_de_arestas;
        for (size_t i = 4; i < linhas.size(); ++i) {
            std::string linha = linhas[i];
            std::stringstream ss(linha);
            std::vector<float> aresta;
            float col;
            while (ss >> col) {
                aresta.push_back(col);
            }
            if (tem_peso) {
                float peso;
                ss >> peso;
                aresta.push_back(peso);
            }
            lista_de_arestas.push_back(aresta);
        }

        lista_adj.resize(num_vertices + 1);
        capacidades.resize(num_vertices + 1, std::vector<float>(num_vertices + 1, 0));

        for (const auto& aresta : lista_de_arestas) {
            int u = static_cast<int>(aresta[0]);
            int v = static_cast<int>(aresta[1]);
            float w = tem_peso ? aresta[2] : 1.0f;

            lista_adj[u].emplace_back(v);
            lista_adj[v].emplace_back(u);
            capacidades[u][v] = w;
        }
    }

    std::vector<std::pair<int, int>> bfs(const std::vector<std::vector<float>>& fluxos, int origem, int destino) {
        int n = lista_adj.size();
        std::deque<int> fila;
        fila.push_back(origem);
        std::vector<std::vector<std::pair<int, int>>> caminhos(n);
        caminhos[origem] = {};

        while (!fila.empty()) {
            int vertice_atual = fila.front();
            fila.pop_front();

            for (int vizinho : lista_adj[vertice_atual]) {
                float capacidade_residual = capacidades[vertice_atual][vizinho] - fluxos[vertice_atual][vizinho];
                if (capacidade_residual > 0 && caminhos[vizinho].empty()) {
                    caminhos[vizinho] = caminhos[vertice_atual];
                    caminhos[vizinho].emplace_back(vertice_atual, vizinho);
                    if (vizinho == destino) {
                        return caminhos[vizinho];
                    }
                    fila.push_back(vizinho);
                }
            }
        }

        return {};
    }
};

std::vector<std::string> leitura_do_arquivo(const std::string& arquivo) {
    std::ifstream file(arquivo);
    std::vector<std::string> linhas;
    std::string linha;
    while (getline(file, linha)) {
        linhas.push_back(linha);
    }
    return linhas;
}

int main() {
    std::vector<std::string> linhas;
    std::string linha;
    while (getline(std::cin, linha)) {
        if (linha.empty()) {
            break;
        }
        linhas.push_back(linha);
    }

    Grafo grafo(linhas, true);

    for (size_t vertice = 2; vertice < grafo.lista_adj.size(); ++vertice) {
        std::cout << vertice << " " << grafo.fluxo_maximo(1, vertice) << std::endl;
    }
    return 0;
}