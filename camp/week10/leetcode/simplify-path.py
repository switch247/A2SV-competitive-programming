class Solution:
    def simplifyPath(self, path: str) -> str:
        path_list = path.split('/')
        # print(path_list)
        stack = []
        for ele in path_list:
            if ele not in ["",".",".."]:
                stack.append(ele)
            elif ele == ".." and stack:
                stack.pop()
        # print("/".join(['']))
        return "/" + "/".join(stack)