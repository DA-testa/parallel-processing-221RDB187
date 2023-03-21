# python3
#221RDB187

def parallel_processing(n, m, data):
    output = []
    # TODO: write the function for simulating parallel tasks, 
    # create the output pairs
    threads = [(i, 0) for i in range(n)]

    for j in range(m):
        thread = 0
        for i in range(0, n):
            if threads[i][1]< threads[thread][1]:
                thread = 1
        index, times = threads[thread]
        output.append(threads[thread])
        threads[thread] = (index, times + data[j])
    return output

def main():
    # TODO: create input from keyboard
    # input consists of two lines
    # first line - n and m
    # n - thread count 
    # m - job count
   

    first = input().split()
    n = int(first[0])
    m = int(first[1])
    data = list(map(int, input().split()))

    # second line - data 
    # data - contains m integers t(i) - the times in seconds it takes any thread to process i-th job

    # TODO: create the function
    result = parallel_processing(n,m,data)
    
    # TODO: print out the results, each pair in it's own line

    for r in result:
        print(r[0], r[1])

if __name__ == "__main__":
    main()
