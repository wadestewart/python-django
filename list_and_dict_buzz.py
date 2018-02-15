fizz_dict = {
    "fizz": [],
    "buzz": [],
    "fizzbuzz": [],
    "other": []
}

def fizzbuzz(max_num):
    for num in range(1, max_num):
        if num % 3 == 0 and num % 5 == 0:
            fizz_dict["fizzbuzz"].append(num)
        elif num % 3 == 0:
            fizz_dict["fizz"].append(num)
        elif num % 5 ==0:
            fizz_dict["buzz"].append(num)
        else:
            fizz_dict["other"].append(num)
    print fizz_dict
fizzbuzz(20)
