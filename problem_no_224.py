# 155. Min Stack
# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
# Implement the MinStack class:
# MinStack() initializes the stack object.
# void push(int val) pushes the element val onto the stack.
# void pop() removes the element on the top of the stack.
# int top() gets the top element of the stack.
# int getMin() retrieves the minimum element in the stack.
# You must implement a solution with O(1) time complexity for each function.

# Example 1:
# Input
# ["MinStack","push","push","push","getMin","pop","top","getMin"]
# [[],[-2],[0],[-3],[],[],[],[]]
# Output
# [null,null,null,null,-3,null,0,-2]
# Explanation
# MinStack minStack = new MinStack();
# minStack.push(-2);
# minStack.push(0);
# minStack.push(-3);
# minStack.getMin(); // return -3
# minStack.pop();
# minStack.top();    // return 0
# minStack.getMin(); // return -2



class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self) -> None:
        val = self.stack.pop()
        if val == self.min_stack[-1]:
            self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()



# 🎯 Goal
# You want a normal stack plus the ability to get the current minimum value in constant time (O(1)), no matter how many times you push or pop.

# 🧠 Concept
# You use two stacks:

# self.stack – holds all elements as usual.

# self.min_stack – keeps track of the minimum element at each stage.

# 🔎 Why min_stack.append(val) only if it's smaller or equal?
# Because you want min_stack[-1] to always hold the current minimum, and if a smaller or equal value comes in, it's a new candidate for minimum.

# 💡 Example Walkthrough
# ➤ Start: Empty stack

# stack = []
# min_stack = []
# ➤ Operation: push(5)
# stack = [5]

# min_stack = [5] because it's the first and also min so far.

# ➤ Operation: push(3)
# stack = [5, 3]

# min_stack = [5, 3] because 3 ≤ 5, so it's a new min.

# ➤ Operation: push(7)
# stack = [5, 3, 7]

# min_stack = [5, 3] → 7 > 3, so we don’t push it to min_stack.

# ➤ Operation: getMin()
# Return min_stack[-1] → 3

# ➤ Operation: pop()
# val = 7 → remove from stack

# 7 ≠ min_stack[-1], so don’t pop from min_stack

# New state:

# stack = [5, 3]

# min_stack = [5, 3]

# ➤ Operation: pop() again
# val = 3 → remove from stack

# 3 == min_stack[-1], so pop from min_stack too

# New state:

# stack = [5]

# min_stack = [5]

# ➤ Operation: getMin() now returns 5
# 📌 Summary Table
# Operation	stack	min_stack	Notes
# push(5)	[5]	[5]	5 is min
# push(3)	[5, 3]	[5, 3]	3 ≤ 5 → push to min_stack
# push(7)	[5, 3, 7]	[5, 3]	7 > 3 → do not push
# pop()	[5, 3]	[5, 3]	7 not in min_stack
# pop()	[5]	[5]	3 == current min → pop it
# getMin()		[5]	min is now 5


# if not self.min_stack
# This checks if min_stack is empty.
# not self.min_stack returns True if min_stack is empty ([]).
# So, it means:
# ➤ "If min_stack is currently empty..."
# ✅ Why check this?
# Because when you push the first element, it should always go into min_stack (it’s the minimum so far).