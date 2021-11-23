class Stack:
    def __init__(self):
        self.list_elements = []

    def isEmpty(self):
        if len(self.list_elements) == 0:
            return True
        else:
            return False

    def push(self, element):
        self.list_elements.append(element)

    def pop(self):
        return self.list_elements.pop()

    def peek(self):
        return self.list_elements[-1]

    def size(self):
        return len(self.list_elements)

dict_brace = {']': '[', ')': '(', '}': '{'}

def brace_balance2(start_str):
    st = Stack()
    for element in start_str:
        if element not in dict_brace:
            st.push(element)
        else:
            if st.peek() != dict_brace[element]:
                return "Несбалансированно"
            else:
                st.pop()
    if st.isEmpty():
        return "Сбалансированно"

print(brace_balance2('{{[()]}}'))