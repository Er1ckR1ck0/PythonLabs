import math
from ast import literal_eval
import time
def number1():
    a = input("> Enter a number: ")
    b = input("> Enter a number: ")
    n = input("> Enter a number: ")
    x = input("> Enter a number: ")
    def check(a, b, n, x):
        while a.isdigit() and b.isdigit() and n.isdigit() and x.isdigit() is False:
            if not a.isdigit():
                a = input("> Enter a number for a: ")
            if not b.isdigit():
                b = input("> Enter a number for b: ")
            if not n.isdigit():
                n = input("> Enter a number for x: ")
            if not x.isdigit():
                x = input("> Enter a number for n: ")
        return int(a), int(b), int(n), int(x)
    a,b,n,x = check(a, b, n, x)[0], check(a, b, n, x)[1], check(a, b, n, x)[2], check(a, b, n, x)[3]
    
    function = (5*a**(n*x) / n+x ) - math.sqrt(abs(math.cos(x**(3**n))))
    return function

def number2():
    tuple_list = ("hello", -123, (1,2,3), -2.421, -3, [1,2])
    def print_tuple(tuple_list):
        print(tuple_list)
    def add_element(tuple_list):
        item = eval(input('> Enter new item (or <Enter> to quit): '))
        tuple_list = tuple_list + (item,)
        print("> New tuple is ", tuple_list)
        return tuple_list
        
    def delete_tuple_element(tuple_list):
        print("> Lenth of the elements is ", len(tuple_list), end="\n\n")
        print(str(tuple_list)[1:-1])
        for i in range(0, len(tuple_list)):
            print(" "+ " "*(len(str(tuple_list[i]))//2) + str(i+1) + " "*(len(str(tuple_list[i]))//2), end=" ")
            if i == len(tuple_list)-1:
                print("\n")
        input_number = input("> Enter a number of task: ")
        print(f"> Element {input_number} ({tuple_list[int(input_number)-1]}) deleted")
        tuple_list = [i for i in tuple_list if i != tuple_list[int(input_number)-1] ]
        print(f"> New tuple: {list(tuple_list)}")

    def create_float_tuple(tuple_list):
        tuple_values = [num for num in tuple_list if isinstance(num, float) and num < 100]
        print("> Tuple values:", tuple_values)
        
    def find_multiply(tuple_list):
        tuple_values = [num for num in tuple_list if isinstance(num, int) and num < 0]
        multiply = 1
        for i in tuple_values:
            multiply *= i
        print(multiply)
    
    def find_word(tuple_list):
        word = input("> Enter a word: ")
        print("> Count elements of {word} is: ",tuple_list.count(word))
        tuple_string = ""
        for i in tuple_list:
            tuple_string = tuple_string + str(i) + " "
        print("> Your string is: ", tuple_string)
    
    def symmetric_difference(tuple_list):
        try:
            new_tuple = eval(input("> Enter tuple M1: "))
            while type(new_tuple) is not tuple:
                new_tuple = eval(input("> Please, rewrite tuple: "))
            new_tuple = set(new_tuple)
            tuple_list = set(tuple_list)
            print("> Symmetric difference of M1 and M2:", new_tuple.symmetric_difference(tuple_list))
        except:
            print("> My appologies, but in M1 or M2 there was founded list. That's why command doesn't work. Wait while list will be deleted")
            time.sleep(2)
            new_tuple = set([item for item in new_tuple if type(item) != list])
            tuple_list = set([item for item in tuple_list if type(item) != list])
            print("> Symmetric difference of M1 and M2:", new_tuple.symmetric_difference(tuple_list)) 
    def creating_dictionary(tuple_list):
        dict = {}
        for i in range(0, len(tuple_list)):
            dict.update({i:tuple_list[i]})
            if i % 2 == 1:
                print(dict[i])   
# def main():
#     input_number = input("> Enter a number of task: ")
#     def check(input_number):
#         while not input_number.isdigit() or int(input_number) > 3:
#             input_number = input("> Plese, rewrite your number: ")
#         return input_number

#     input_number = int(check(input_number))
    
#     match input_number:
#         case 1:
#             print(number1())
    
    
# if __name__ == "__main__":
#     main()