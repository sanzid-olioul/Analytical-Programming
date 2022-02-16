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
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode *head = nullptr,*prev = nullptr;
        int carry =0 ;
        while (l1 || l2)
        {
            if(l1 && l2){
                
                int sum = (l1->val + l2->val+ carry)%10;
                carry = (l1->val + l2->val + carry)/10;
                ListNode *lstnd = new ListNode(sum);
                if(!head){
                    head = lstnd;
                    prev = head;
                }else{
                    prev->next = lstnd;
                    prev = lstnd;
                }
                l1 = l1->next;
                l2 = l2->next;
            }else if(l1 && !l2){
                int sum = (l1->val + carry)%10;
                carry = (l1->val + carry)/10;
                ListNode *lstnd = new ListNode(sum);
                prev->next = lstnd;
                prev = lstnd;
                l1 = l1->next;
            }
            else if(!l1 && l2){
                int sum = (l2->val+ carry)%10;
                carry = (l2->val + carry)/10;
                ListNode *lstnd = new ListNode(sum);
                prev->next = lstnd;
                prev = lstnd;
                l2 = l2->next;
            }
        }
        if(carry > 0){
            ListNode *lstnd = new ListNode(carry);
            prev->next = lstnd;
        }
        return head;
    }
};
