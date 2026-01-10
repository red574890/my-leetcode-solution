class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.split('/')

        newpath = []

        for p in range(len(path)):
            if("." == path[p] or "" == path[p]):
                continue
            elif(".." == path[p]):
                if(len(newpath)==0):
                    continue
                newpath.pop()
            else:
                newpath.append(path[p])

        return '/' + '/'.join(newpath)
