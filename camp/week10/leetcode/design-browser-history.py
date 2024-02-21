class BrowserHistory:

    def __init__(self, homepage: str):
        self.cur = -1
        self.history = [homepage]
        
    def visit(self, url: str) -> None:
        if self.cur == -1:
            self.history.append(url)
            return
        # when we visit a site our for ward history will be deleted
        del self.history[self.cur + 1:]
        self.cur = -1
        self.history.append(url)

    def back(self, steps: int) -> str:
        self.cur -= steps
        if self.cur < -len(self.history):
            # stop at the fist posible site
            self.cur = -len(self.history)
        return self.history[self.cur]

    def forward(self, steps: int) -> str:
        self.cur += steps
        if self.cur > -1: 
            # stop at the fist posible site
            self.cur = -1
        return self.history[self.cur]
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)