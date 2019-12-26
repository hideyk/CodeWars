def digital_root(n):
    while n > 9:
        num_list = [int(i) for i in str(n)]
        n = sum(num_list)
    return n

def digital_rootwtf(n):
  return n%9 or n and 9

num = 92378
digroot = digital_root(num)
print(digroot)


