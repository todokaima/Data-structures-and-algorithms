#Select Sort
def select(seq,start):
    minIndex = start

    for j in range(start + 1, len(seq)):
        if seg[minIndex] > seq[j]:
            minIndex = j
    return minIndex
def selSort(seq):
    for i in range(len(seq)-1):
        minIndex = select(seq,i)
        tmp = seq[i]
        seq[i] = seq[minIndex]
        seq[minIndex] = tmp

#Merge Sort
def merge(seq,start,mid,stop):
    lst = []
    i = start
    j = mid

    while i < mid and j <stop:
        if seq[i] < seq[j]:
            lst.append(seq[i])
            i+=1
        else:
            lst.append(seq[j])
            j+=1
    while i < mid:
        lst.append(seq[i])
        i+=1
    while j < stop:
        lst.append(seq[j])
        j += 1
    for i in range(len(lst)):
        seq[start + i] = lst[i]

def mergeSortRecursively(seq,start,stop):
    if start >=  stop -1:
        return
    mid = (start+stop)//2
    mergeSortRecursively(seq,start,mid)
    mergeSortRecursively(seq,mid,stop)
    merge(seq,start,mid,stop)

def mergeSort(seq):
    mergeSortRecursively(seq,0,len(seq))

#Quick Sort

import random

def partition(seq, start, stop):
    pivotIndex = start
    pivot = seq[pivotIndex]
    i = start+1
    j = stop-1

    while i <= j:
        while i<=j and not pivot < seqp[i]:
            i+=1
        while i <= j and pivot <seq[j]:
            j -=1
        if i < j:
            tmp = seq[i]
            seq[i] = seq[j]
            seq[j] = tmp
            i+=1
            j-=1
        seq[pivotIndex] = seq[j]
        seq[j] = pivot

        return j
def quicksortRecursively(seq, start, stop):
    if start >= stop -1:
        return
    pivotIndex = partition(seq, start, stop)
    quicksortRecursively(seq,start, pivotIndex)
    quicksortRecursively(seq, pivotIndex+1,stop)


def quicksort(seq):
    for i in range(len(seq)):
        j = random.randint(0,len(seq)-1)
        tmp = seq[i]
        seq[i] = seq[j]
        seq[j] = tmp
    quicksortRecursively(seq,0,len(seq))

