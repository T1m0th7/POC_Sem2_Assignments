def times2(a): return a * 2
def div2(a): return a / 2
def exp2(a): return a ** 2

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] #You make

mapped_times2 = map(times2, my_list)
mapped_div2 = map(div2, my_list)
mapped_exp2 = map(exp2, my_list)
#YOUDO:  repeat for div2, exp2

mapped_times2_list = list(mapped_times2)
print(mapped_times2_list)

mapped_div2_list = list(mapped_div2)
print(mapped_div2_list)

mapped_exp2_list = list(mapped_exp2)
print(mapped_exp2_list)
#YOUDO:  repeat for the other maps 