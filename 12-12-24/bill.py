def print_percentage(salary, bill1, bill2, bill3):
    percentage = ((bill1 + bill2 + bill3) / salary) * 100
    print(int(percentage))

if __name__ == '__main__':
    print_percentage(5000, 100, 200, 300)
