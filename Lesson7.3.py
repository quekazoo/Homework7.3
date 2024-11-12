def second_index():
    text = input("Write your text: ")
    some_str = input("Write some string: ")
    first_index = text.find(some_str)
    if first_index == -1:
        return None
    second_index = text.find(some_str, first_index + 1)
    if second_index != -1:
        print(second_index)
        return second_index
    else:
        print("None")
        return None
second_index()