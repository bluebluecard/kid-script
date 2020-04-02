a = [[1,5],[3,10],[6,15],[19,29],[23,26],[25,30],[34,40],[45,50]]


def run_pick(last_cor,now_cor):

    if last_cor[1] >= now_cor[1]:
        merge_cor = last_cor
    else:
        merge_cor = [last_cor[0],now_cor[1]]

    return merge_cor


def merge(a):

    data = []
    last_cor = a[0]

    for i in range(len(a)):

        if last_cor[0]<= a[i][0] <= last_cor[1]:
            merge_cor = run_pick(last_cor,a[i])
            last_cor = merge_cor

        else:

            data.append(last_cor)
            last_cor = a[i]

        if i == len(a) - 1:
            data.append(last_cor)


    print(data)


merge(a)
