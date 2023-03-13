import json
import time
import argparse
import heapq

# --- TODO START --- #
# You can define any class or function
# You can import any python standard library : https://docs.python.org/3/library/
# However, you are not allowed to import any libraries other than python standard library, (such as numpy)
# --- TODO END --- #

def solution(json_input):
    # --- TODO START --- #
    global arr
    arr = json_input["array"]
    arr = [-i for i in arr] # heapq is min heap, but we want max heap
    k = json_input["topk"]
    n = len(arr)
    sum_list = []
    for i in range(n):
        sum_list.append(sum(i, n))

    sum_heap = []
    heapq.heapify(sum_heap)
    for i in sum_list:
        for j in i:
            heapq.heappush(sum_heap, j)
    a=0
    l4 = []
    while a < k:
        l4.append(-heapq.heappop(sum_heap))
        a+=1
    return l4


def sum(start, end):
    l1 = []
    l1.append(arr[start])
    if start < end-1:
        for i in range(end-1-start):
            l1.append(l1[i]+ arr[start+i+1])
    else:
        pass
    return l1
    # --- TODO END --- #

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', default='input_6.json')
    parser.add_argument('--output', default='output_6.json')
    args = parser.parse_args()
    json_input = json.load(open(args.input, "r"))
    t1 = time.time()
    json_output = solution(json_input)
    t2 = time.time()
    json.dump(json_output, open(args.output, "w"))
    print("runtime of %s : %s" % (args.input, t2 - t1))

