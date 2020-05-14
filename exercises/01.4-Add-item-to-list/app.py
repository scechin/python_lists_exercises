#Remember import random function here:
import random
#random_numbers = []
random_number = random.sample(range(0, 10), 10)
#random_numbers += random_number
my_list = [4,5,734,43,45] + random_number
#my_list = my_list + random_number
print(my_list)
#The magic is here:
