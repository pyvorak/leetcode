class AllOne {
    set<pair<int, string>> keys;
    unordered_map<string, int> mp;
public:
    AllOne() {
    }
    void inc(string key) {
        int old_cnt = mp[key];
        mp[key]++;
        int new_cnt = mp[key];

        if (old_cnt != 0){
            keys.erase({old_cnt, key});
        }

        keys.insert({new_cnt, key});
    }
    
    void dec(string key) {
        int old_cnt = mp[key];
        mp[key]--;
        int new_cnt = mp[key];

        keys.erase({old_cnt, key});
        
        if (new_cnt != 0){
            keys.insert({new_cnt, key});
        }
    }
    
    string getMaxKey() {
        if (keys.size()){
            return prev(keys.end())->second;
        } else {
            return "";
        }
    }
    
    string getMinKey() {
        if (keys.size()){
            return keys.begin()->second;
        } else {
            return "";
        }
    }
};
