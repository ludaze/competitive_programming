class Solution(object):
    def simplifyPath(self, path):
        dirs = path.split("/")
        stack = []
        for p in dirs:
            if p in ['', '.']:
                continue
            elif p == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(p)
        return '/' + '/'.join(stack)