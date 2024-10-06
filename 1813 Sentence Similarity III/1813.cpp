class Solution {
public:
    deque<string> split(string s){
        deque<string> words;
        istringstream ss(s);
        string word;

        while (ss >> word){
            words.push_back(word);
        }

        return words;
    }

    bool areSentencesSimilar(string s1, string s2) {
        deque<string> w1 = split(s1);
        deque<string> w2 = split(s2);
        
        while (!w1.empty() && !w2.empty() && w1.front() == w2.front()){
            w1.pop_front();
            w2.pop_front();
        }

        while (!w1.empty() && !w2.empty() && w1.back() == w2.back()){
            w1.pop_back();
            w2.pop_back();
        }

        return w1.empty() || w2.empty();
    }
};
