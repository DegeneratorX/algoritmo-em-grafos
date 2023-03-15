#include <iostream>
#include <vector>
#include <string>

using std::cin;
using std::cout;
using std::endl;
using std::string;
using std::vector;

class Vertex{
private:
    string name;
    vector<Vertex>* adjacency_list;
public:
    Vertex(string name){
        this->name = name;
        this->adjacency_list = new vector<Vertex>();
    }

    void add_neighbor(Vertex vertex){
        adjacency_list->push_back(vertex);
    }

    void show_neighbors(){
        for(int i = 0; i < adjacency_list->size(); i++){
            cout << adjacency_list[i] << " ";
        }
    }

};

int main(){

}