class Solution:
    def simplifyPath(self, path: str) -> str:
        order = []
        check = path.split("/") 
        for i in check:
            if i == "..":
                if order:
                    order.pop()
            elif i == "" or i == ".":
                continue
            else:
                order.append(i)
        return "/" + "/".join(order)

        