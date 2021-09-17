if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    a,b,c = student_marks[query_name]
    print('%.2f'%((a+b+c)/3))
    print(scores)
