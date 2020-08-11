#include <string>
#include <vector>
#include <algorithm>
#include <iostream>
using namespace std;

bool cmp(const string &u, const string &v){
    if(u+v > v+u) return true;
    else return false;
}

string solution(vector<int> numbers) {
    string answer = "";
    vector<string> ntos;
    for(int i=0; i<numbers.size(); i++){
        ntos.push_back(to_string(numbers[i]));
    }
    sort(ntos.begin(),ntos.end(),cmp);
    for(int i=0; i<ntos.size(); i++)
        answer=answer+ntos[i];
    if(atoi(answer.c_str())==0) answer="0";
    return answer;
}