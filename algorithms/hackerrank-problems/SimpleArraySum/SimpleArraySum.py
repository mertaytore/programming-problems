#!/bin/python

"""
Given an array of N integers, can you find the sum of its elements?

Input Format
The first line contains an integer, N , denoting the size of the array.
The second line contains N space-separated integers representing the array's elements.

Output Format
Print the sum of the array's elements as a single integer.

"""

number_of_elements = int(raw_input().strip())
arr = map(int, raw_input().strip().split(' '))
print sum(arr)
