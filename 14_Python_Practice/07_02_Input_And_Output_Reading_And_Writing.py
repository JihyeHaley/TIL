# 'w' = only writing
# 'a' = only appending
# 'r+' = both reading and writing
# 'r' = will be assume dif it's omitted
# 'b' = open files as binary mode

f = open('workfile', 'w')

with open('workfile') as f:
    read_data = f.read()

f.read()