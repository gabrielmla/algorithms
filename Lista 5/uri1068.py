while True:
    try:
        n = raw_input()
        stack = []
        f = True
        for c in n:
            if c == '(':
                stack.append(c)
            elif c == ')':
                if len(stack) > 0 and stack[-1] == '(':
                    stack.pop()
                else:
                    f = False
                    break
        if len(stack) == 0 and f:
            print "correct"
        else:
            print "incorrect"
    except:
        break
