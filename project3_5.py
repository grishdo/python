def enter_str():
    return input("Введите строку чисел, разделенных пробелом либо спецсимвол чтобы выйти: ")


def main():
    sum = 0
    while True:
        choice = enter_str()
        list_nums = choice.split()
        main_exit = False
        for num in list_nums:
            if num in '.,:;!_*-+()/#¤%&':
                main_exit = True
                break
            else:
                num = int(num)
                sum = sum + num

        print(sum)
        if main_exit:
            break


main()
