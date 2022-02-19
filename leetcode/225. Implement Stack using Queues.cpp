class MyStack {
public:
    queue<int> q1;
    queue<int> q2;
    MyStack() {
        
    }
    
    void push(int x) {
        
        while(q1.size()){
            q2.push(q1.front());
            q1.pop();
        }
        q1.push(x);
        while(q2.size()){
            q1.push(q2.front());
            q2.pop();
        }
    }

    int pop() {
       int top_=q1.front();
        q1.pop();
        return top_;
    }
    
    int top() {
        return q1.front();
    }
    
    bool empty() {
        return q1.empty() && q2.empty();
    }
};
