def main():
    f = open("user_data.csv", mode="r")

    data = f.read()
    print(type(f))

    f.close()

    print(data)



if __name__ == '__main__':
    main()