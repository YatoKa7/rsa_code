import sys
with open ('write.txt' ,'w') as f:
    original_stdout = sys.stdout
    sys.stdout = f
    print("Hello text file")
