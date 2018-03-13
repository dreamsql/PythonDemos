


queue = [i for i in range(0, 100)]

front = 0
back = 0

def enqueue(a, b, parent, action):
    global front
    global back
    global queue
    for i in range(0, front):
        item = queue[i]
        if item.a == a and item.b == b: return
    queue[back]= State(a, b, parent,action)
    back += 1


def backtrace(state):
    if state:
        backtrace(state.parent)
        print(state)
    


class State:
    def __init__(self, a, b, parent, action):
        self.a = a
        self.b = b
        self.parent = parent
        self.action = action
    
    def __str__(self):
        return '{}, {}, {}'.format(self.a, self.b, self.action)


if __name__ == '__main__':

    enqueue(0, 0, None, 'initialize')

    while front < back:
        s = queue[front]
        front += 1
        if s.a == 2 or s.b == 2:
            backtrace(s)
            print()
            continue
        enqueue(0, s.b,s, 'clear a')
        enqueue(s.a, 0, s, 'clear b')
        enqueue(3, s.b, s, 'fill a')
        enqueue(s.a, 4, s, 'fill b')
        enqueue(s.a - min(s.a, 4 - s.b), s.b + min(s.a, 4 - s.b), s, 'fill b by a')
        enqueue(s.a + min(s.b, 3 - s.a), s.b - min(s.b, 3 - s.a), s, 'fill a by b')
    print('process {} states'.format(back))