def main():
    f = open("user_data.csv", mode="r")

    data = f.read()
    # print(type(f))

    # close前


    print("close()する前", f. closed)

    f.close()

    print("close()した後", f.closed)



if __name__ == '__main__':
    main()