class Solution {
public:
    Node* copyRandomList(Node* head) {
        if (head == nullptr) return head;

        unordered_map<Node*, Node*> copyMap;
        
        Node* cur = head;

        while (cur){
            copyMap[cur] = new Node(cur->val);
            cur = cur->next;
        }

        cur = head;

        while (cur){
            copyMap[cur]->next = copyMap[cur->next];
            copyMap[cur]->random = copyMap[cur->random];
            cur = cur->next;
        }

        return copyMap[head];
    }
};
