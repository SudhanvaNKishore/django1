from django.http import HttpResponse
import math

def cal_fact(request,num):
    
    num=int(num)
    if num == 0:
        return HttpResponse("Factorial is 0")
    elif num == 1:
        return HttpResponse("Factorial is 1")
    else:
        return HttpResponse(f'The factorial of {num} is {math.factorial(num)}')
    

def number(request):
    
    list2 = []
    list3 = []
    for i in range(0,10,2):
        list2.append(i)
        list3.append(i+1)
        
        
    return HttpResponse(list3)


def number_list(request):
    even_numbers = []
    odd_numbers = []
    
    for number in range(0,10): 
        if number % 2 == 0:
            even_numbers.append(str(number))
        else:
            odd_numbers.append(str(number))
    
    result_str = f"Even numbers are: {', '.join(even_numbers)}<br>"
    result_str += f"Odd numbers are: {', '.join(odd_numbers)}"
    
    return HttpResponse(result_str)



def multiplication_table(request):
    all_tables = "<h1>Multiplication Tables</h1><br>"
    
    for num in range(1, 21):  # This will generate numbers from 1 to 20
        table = f"<h3>Table of {num}:<h3><br>"
        for i in range(1, 11):  # This will generate numbers from 1 to 10
            result = num * i
            table += f"{num} x {i} = {result}<br>"
        all_tables += table + "<br>"

    return HttpResponse(all_tables)