class CustomStack {
    int maxStack;
    vector<int> v;
public:
    CustomStack(int maxSize) : maxStack(maxSize){
        v.reserve(maxSize);
    }
    
    void push(int x) {
        if (v.size() < maxStack){
            v.push_back(x);
        }
    }
    
    int pop() {
        if (v.empty()){
            return -1;
        } else {
            int val = v.back();
            v.pop_back();
            return val;
        }
    }
    
    void increment(int k, int val) {
        for (int i = 0; i < min((int) v.size(), k); i++){
            v[i] += val;
        }
    }
};
