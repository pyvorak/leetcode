# define LL long long
class Solution {
public:
    int count(LL n, LL a, LL b){
        int cnt = 0;

        while (a <= n){
            cnt += min(n + 1, b) - a;
            a *= 10;
            b *= 10;
        }

        return cnt; 
    }

    int findKthNumber(int n, int k) {
        int num = 1;
        k--;

        while (k > 0){
            int cnt = count(n, num, num + 1);

            if (k >= cnt){
                num++;
                k -= cnt;
            } else {
                num *= 10;
                k--;
            }
        }

        return num;
    }
};
