#!/usr/bin/env python
# coding: utf-8

# # Q1

# In[ ]:


if __name__ == '__main__':
    n = int(raw_input())
    arr = map(int, raw_input().split())
    
    maxi = max(arr)
    a = -9999999999
    for i in range(n):
        if arr[i] != maxi and arr[i] > a:
            a = arr[i]
    print a


# # Q2

# In[ ]:


score_list = [];
for _ in range(int(raw_input())):
    name = raw_input()
    score = float(raw_input())

    score_list.append([name, score])
second_highest = sorted(set([score for name, score in score_list]))[1]
print('\n'.join(sorted([name for name, score in score_list if score == second_highest])))


# # Q3

# In[ ]:


if __name__ == '__main__':
    n = int(raw_input())
    student_marks = {}
    for _ in range(n):
        line = raw_input().split()
        name, scores = line[0], line[1:]
        scores = map(float, scores)
        student_marks[name] = scores
    query_name = raw_input()
    
    output = list(student_marks[query_name])
    percentage = sum(output)/len(output);
    print("%.2f" % percentage);


# # Q4

# In[ ]:


if __name__ == '__main__':
    N = int(input())
    # Lists in Python - Hacker Rank Solution START
    Output = [];
    for i in range(0,N):
        ip = input().split();
        if ip[0] == "print":
            print(Output)
        elif ip[0] == "insert":
            Output.insert(int(ip[1]),int(ip[2]))
        elif ip[0] == "remove":
            Output.remove(int(ip[1]))
        elif ip[0] == "pop":
            Output.pop();
        elif ip[0] == "append":
            Output.append(int(ip[1]))
        elif ip[0] == "sort":
            Output.sort();
        else:
            Output.reverse();
    


# # Q5

# In[ ]:


if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    
    t = tuple(integer_list)
    print(hash(t));


# # Q6

# In[ ]:


def average(array):

    sum_arr = sum(set(array))
    len_arr = len(set(array))
    output = sum_arr/len_arr
    return output;


# # Q7

# In[ ]:


# Enter your code here. Read input from STDIN. Print output to STDOUT
io = input().split()
m = int(io[0])
n = int(io[1])

store = list()
count = 0

store = list(map(int, input().strip().split()))

A = set(map(int, input().strip().split()))
B = set(map(int, input().strip().split()))

for i in store:
    if i in A:
        count = count+1
    if i in B:
        count = count-1

print(count)


# # Q8

# In[ ]:


# Enter your code here. Read input from STDIN. Print output to STDOUT
A = int(input())
Aset = set(map(int, input().split()))
B = int(input())
Bset = set(map(int, input().split()))

mdef = Aset.difference(Bset)
ndef = Bset.difference(Aset)

output = mdef.union(ndef)

for i in sorted(list(output)):
    print(i)


# # Q9

# In[ ]:


# Enter your code here. Read input from STDIN. Print output to STDOUT
N = int(input())

country = set()

for i in range(N):
    country.add(input())

print(len(country))


# # Q10

# In[ ]:


n=int(input())
s=set(map(int,input().split()))
N=int(input())
for i in range(N):
  command=input().split()
  if command[0]=="remove":
      s.remove(int(command[1]))
  elif command[0]=="discard":
    s.discard(int(command[1]))
  else:
    s.pop()
print(sum(s))
    


# # Q11

# In[ ]:


# Enter your code here. Read input from STDIN. Print output to STDOUT
N1 = int(input())
store1 = set(input().split());

N2 = int(input())
store2 = set(input().split());

store3 = store1.union(store2)

print(len(store3))


# # Q12

# In[ ]:


# Enter your code here. Read input from STDIN. Print output to STDOUT
N1 = int(input())
store1 = set(input().split())

N2 = int(input())
store2 = set(input().split())

store3 = store2.intersection(store1)

print(len(store3))


# # Q13

# In[ ]:


# Enter your code here. Read input from STDIN. Print output to STDOUT
N1 = int(input())
store1 = set(input().split())

N2 = int(input())
store2 = set(input().split())

store3 = store1.difference(store2)

print(len(store3))


# # Q14

# In[ ]:


# Enter your code here. Read input from STDIN. Print output to STDOUTN1 = int(input())
N1 = int(input())
store1 = set(input().split())

N2 = int(input())
store2 = set(input().split())

store3 = store1.symmetric_difference(store2)

print(len(store3))


# # Q15

# In[ ]:


# Enter your code here. Read input from STDIN. Print output to STDOUT
len_set = int(input())

store = set(map(int, input().split()))

op_len = int(input())

for i in range(op_len):
    operation = input().split()
    if operation[0] == 'intersection_update':
        temp_store = set(map(int, input().split()))
        store.intersection_update(temp_store)
    elif operation[0] == 'update':
        temp_store = set(map(int, input().split()))
        store.update(temp_store)
    elif operation[0] == 'symmetric_difference_update':
        temp_store = set(map(int, input().split()))
        store.symmetric_difference_update(temp_store)
    elif operation[0] == 'difference_update':
        temp_store = set(map(int, input().split()))
        store.difference_update(temp_store)
    else :
        assert False

print(sum(store))


# # Q16

# In[ ]:


# Enter your code here. Read input from STDIN. Print output to STDOUT
N = int(input())

store = map(int, input().split())
store = sorted(store)

for i in range(len(store)):
    if(i != len(store)-1):
        if(store[i]!=store[i-1] and store[i]!=store[i+1]):
            print(store[i])
            break;
    else:
        print(store[i])


# # Q17

# In[ ]:


# Enter your code here. Read input from STDIN. Print output to STDOUT
S = int(input())

for _ in range(S):
    a = input()
    A = set(input().split())
    b = int(input())
    B = set(input().split())
    print(A.issubset(B))


# # Q18

# In[ ]:


# Enter your code here. Read input from STDIN. Print output to STDOUT
store = set(input().split())
N = int(input())
output = True

for i in range(N):
    store2 = set(input().split())
    if not store2.issubset(store):
        output = False
    if len(store2) >= len(store):
        output = False

print(output)

