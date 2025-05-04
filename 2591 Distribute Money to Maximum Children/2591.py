class Solution:
    def distMoney(self, money: int, children: int) -> int:
        if money < children:
            return -1

        money -= children
        ans = min(children, money // 7)
        children -= ans
        money -= 7 * ans
        
        if money == 3 and children == 1:
            ans -= 1
        
        if children == 0 and money > 0:
            ans -= 1

        return ans
