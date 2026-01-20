class BrowserHistory:

    def __init__(self, homepage: str):
        self.curr = Node(homepage)
        

    def visit(self, url: str) -> None:
        self.curr.next_node = Node(url, None, self.curr)
        self.curr = self.curr.next_node

        

    def back(self, steps: int) -> str:
        temp = self.curr
        x = 0
        while temp:
            if x == steps or not temp.prev_node:
                self.curr = temp
                return temp.page
            temp = temp.prev_node
            x += 1
        return self.curr.page

    def forward(self, steps: int) -> str:
        temp = self.curr
        x = 0
        while temp:
            if x == steps or not temp.next_node:
                self.curr = temp
                return temp.page
            temp = temp.next_node
            x += 1
        return self.curr.page


class Node:
    def __init__(self, page="", next_node=None, prev_node=None):
        self.page = page
        self.next_node = next_node
        self.prev_node = prev_node 
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)