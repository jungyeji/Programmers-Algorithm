#include <string>
#include <vector>
#include <iostream>
using namespace std;

vector<int> solution(vector<int> answers) {
    vector<int> answer;
    int n=answers.size();
    int p2[8] = {2,1,2,3,2,4,2,5};
    int p3[10] = {3,3,1,1,2,2,4,4,5,5};
    
    vector<int> pick1;
    vector<int> pick2;
    vector<int> pick3;
    
    for(int i=0; i<n; i++){
        pick1.push_back(i%5+1);
    }
    int j=0;
    for(int i=0; i<n; i++){
        if(j==8) j=0;
        pick2.push_back(p2[j]);
        j++;
    }
    j=0;
    for(int i=0; i<n; i++){
        if(j==10) j=0;
        pick3.push_back(p3[j]);
        j++;
    }
    
    int count1=0, count2=0, count3=0;
    for(int i=0; i<n; i++){
        if(answers[i]==pick1[i]) count1++;
        if(answers[i]==pick2[i]) count2++;
        if(answers[i]==pick3[i]) count3++;
    }
    int maxnum =max(max(count1,count2),count3);
    if(maxnum==count1) answer.push_back(1);
    if(maxnum==count2) answer.push_back(2);
    if(maxnum==count3) answer.push_back(3);
    
    return answer;
}