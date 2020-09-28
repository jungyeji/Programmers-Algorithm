#include <string>
#include <vector>
#include <algorithm>
using namespace std;

bool dfs(string from, vector<vector<string>> &tickets, vector<bool> &used, 
         vector<string> &answer, int cnt){
    answer.push_back(from);
    for(int i=0; i<tickets.size(); i++){
        if(tickets[i][0]==from && !used[i]){
            used[i]=true;
            bool flag = dfs(tickets[i][1], tickets, used, answer, cnt+1);
            if(flag) return true;
            else used[i]=false;
        }
    }
    if(cnt==tickets.size()) return true;
    answer.pop_back();
    return false;
}
    
vector<string> solution(vector<vector<string>> tickets) {
    vector<string> answer;
    vector<bool> used(tickets.size());
    sort(tickets.begin(), tickets.end());
    dfs("ICN", tickets, used, answer, 0);
    return answer;
}
