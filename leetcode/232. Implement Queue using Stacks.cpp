
class MyQueue {
private:
    stack<int> in;
    stack<int> out; 
public:
    MyQueue() {
        
    }
    
    void push(int x) {        
        while(!in.empty()){
            out.push(in.top());
            in.pop();
        }
        in.push(x);
        while(!out.empty()){
            in.push(out.top());
            out.pop();
        }
        
    }
    
    int pop() {
        int e = in.top();
        in.pop();
        return e;
    }
    
    int peek() {
        return in.top();
    }
    
    bool empty() {
        return in.empty();
    }    
};