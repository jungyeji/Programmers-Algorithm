#include <string>
#include <vector>

using namespace std;

int mincount;
string targetword;

bool diffcheck(string a, string b){
    int n=a.size();
    int cnt=0;
    for(int i=0; i<n; i++){
        if(a[i]!=b[i]) cnt++;
    }
    if(cnt==1) return true;
    else return false;
}

void dfs(vector<string> lefts, string cur, int count){
    if(targetword==cur){
        if(mincount>count){
            mincount=count;
            return;
        }
    }
    for(int i=0; i<lefts.size(); i++){
       if(diffcheck(cur, lefts[i])){
            vector<string> Newlefts = lefts;
			Newlefts.erase(Newlefts.begin() + i);
            dfs(Newlefts, lefts[i], count+1);
        } 
    }
   return; 
}

int solution(string begin, string target, vector<string> words) {
    int answer = 0;
    targetword=target;
    mincount=51;
    for(int i=0; i<words.size(); i++){
        if(diffcheck(begin, words[i])){
            vector<string> Newlefts = words;
			Newlefts.erase(Newlefts.begin() + i);
            dfs(Newlefts, words[i], 1);
        }
    }
    if(mincount<51) answer=mincount;
        
    return answer;
}
