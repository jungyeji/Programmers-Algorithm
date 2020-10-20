#include<string>
#include <iostream>
#include <stack>

using namespace std;

bool solution(string str)
{
    stack<char> s;
    bool answer = true;

    for(int i=0; i<str.size(); i++){
        if(str[i]=='('){
            s.push(str[i]);
        }else{ // str[i]==')'
            if(s.empty()){
                answer=false;
                break;
            }
            if(!s.empty() && s.top()=='('){
                s.pop();
            }
        }
    }
    if(!s.empty()){
        answer=false;
    }
    return answer;
}
