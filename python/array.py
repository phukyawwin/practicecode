#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    
    for a in range(n):
        print(arr[n-a-1],end=' ')
        
        
