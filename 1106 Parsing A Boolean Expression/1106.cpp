class Solution {
public:
    void reduce(stack<char>& stk){
        bool a = true;
        bool b = false;

        while (stk.top() != '('){
            bool cur = stk.top() == 't' ? true : false;
            stk.pop();
            a &= cur;
            b |= cur;
        }
        stk.pop();

        char op = stk.top();
        stk.pop();

        if (op == '|'){
            a = b;
        } else if (op == '!') {
            a = !a;
        }

        stk.push(a ? 't' : 'f');
    }

    bool parseBoolExpr(string expression) {
        stack<char> stk;

        for (char c: expression){
            if (c == ','){
                continue;
            } else if (c != ')'){
                stk.push(c);
            } else {
                reduce(stk);
            }
        }

        return stk.top() == 't';
    }
};
