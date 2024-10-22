class Solution {
public:
    int next(int num){
        int nextNum = 0;

        while (num > 0){
            int cur = num % 10;
            nextNum += cur * cur;
            num /= 10;
        }

        return nextNum; 
    }

    bool isHappy(int n) {
        int fast = next(n);
        int slow = n;

        while (fast != 1 && fast != slow){
            slow = next(slow);
            fast = next(next(fast));
        }

        return fast == 1;
    }
};
