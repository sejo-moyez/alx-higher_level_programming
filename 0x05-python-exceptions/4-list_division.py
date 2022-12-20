#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):

    result = []
    for i in range(list_length):
        try:
            division = my_list_1[i] / my_list_2[i]
        except TypeError:
            division = 0
            print("wrong type")
        except ZeroDivisionError:
            division = 0
            print("division by 0")
        except IndexError:
            division = 0
            print("out of range")
        finally:
            result.append(division)
    return result

