/*
struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};
*/

class Solution {
public:
    ListNode* swapPairs(ListNode* head) {
        ListNode *odd = nullptr,*even = nullptr,*temp = head;
        int count = 0;
        while (temp)
        {   
            odd = temp;
            even = temp->next;
            if(even){
                int tmp = odd->val;
                odd->val = even->val;
                even->val = tmp;
                temp = even->next;
            }else{
                return head;
            }
        }
        return head;
    }
};