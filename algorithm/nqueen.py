import numpy

N = 8

# a = numpy.full((N,N), '-')


def isSafe(a, r, c):
    # print('is safe r = %s, c = %s' % (r,c))
    for i in range(r):
        if a[i,c] == 'Q': 
            # print('is safe r = %s, c = %s already exists' % (i,c))
            return False

    i = r
    j = c
    while i >= 0 and j >=0 :
        if a[i,j] == 'Q': 
            # print('is safe r = %s, c = %s left adj already exists' % (i,j))
            return False
        else:
            i -= 1
            j -= 1


    i = r
    j = c
    while i >= 0 and j < N :
        if  a[i,j] == 'Q': 
            # print('is safe r = %s, c = %s right adj already exists' % (i,j))
            return False
        else:
            i -= 1
            j += 1

    return True

def nQueen(a , r, c):
    if c == 0 and r == N:
        for i in range(N):
            for j in range(N):
                print(a[i,j], end = ' ')
            print("")
        print('')
        return

    for i in range(N):
        if isSafe(a, r, i):
            a[r,i] = 'Q'
            nQueen(a, r + 1, 0)
            a[r,i] = '-'


if __name__ == '__main__':
    a = numpy.full((N,N), '-')
    nQueen(a, 0,0)

        

        


