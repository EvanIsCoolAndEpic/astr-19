def main():
    def f(x):
        return x**3 + 8
    print(f(9))
    if(f(9) > 27):
        print("Yay!")


if __name__ == '__main__':
    main()