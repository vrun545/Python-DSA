tsk = list(map(list, input().split(',')))
tsk.sort(key = lambda x:x[1])

tsk_cnt = 1
i = 1
prev_tsk = tsk[0]

while i<len(tsk):
    curr_tsk = tsk[i]
    if prev_tsk[1]<=curr_tsk[0]:
        tsk_cnt += 1
        prev_tsk = curr_tsk
    i += 1

print(tsk_cnt)
