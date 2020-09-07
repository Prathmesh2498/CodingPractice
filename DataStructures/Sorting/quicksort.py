# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 10:49:23 2020

@author: Admin
"""


def partition(a, low, high):
    pivot = a[high]
    index = low-1
    for j in range(low,high):
        if(a[j]<pivot):
            index+=1
            a[index], a[j] = a[j], a[index]
    
    #The step below swaps the current pivot to it's correct position        
    a[index+1],a[high] = a[high], a[index+1] 
    
    return index+1 #Return position of pivot

def quicksort(a, low, high):
    if low < high: 
        pi = partition(arr,low,high) #To obtain correct positon of pivot
        #Now sort before and after pivot
        quicksort(arr, low, pi-1) 
        quicksort(arr, pi+1, high) 
    

if __name__ == '__main__':    
    arr = []       
    n=int(input("Enter no of elements"))
    for i in range(0,n):
        t = int(input("Enter element: "))
        arr.append(t)    
    quicksort(arr, 0, len(arr)-1)
    for i in arr:
        print(i)
