/*
You  have  a  business  with  several  offices;  
you  want  to lease  phone  lines  to  connect  them  up  with  each  other;  
and  the  phone  company  charges different  amounts  of  money  to  connect  different  pairs  of  cities.  
You  want  a  set  of  lines  that connects  all  your  offices  with  a  minimum  total  cost.  
Solve  the  problem  by  suggesting appropriate data structures
*/

#include<bits/stdc++.h>

#define MAX 10

using namespace std;

class Edge
{
private:
    int u, v, w;
public:
    Edge(){}
    Edge(int a, int b, int weight);

    friend class edgeList;
    friend class phoneGraph;
};

Edge::Edge(int a, int b, int weight){
    u =a;
    v = b;
    w = weight;
}

int main(){

    return 0;
}