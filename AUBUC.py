def main() -> int:
    try:
        AuBuC = int(input("What is A union B union C:\n"))
        A = int(input("Enter A:\n"))
        B = int(input("Enter B:\n"))
        C = int(input("Enter C:\n"))
        AnB = int(input("Enter A intersection B:\n"))
        BnC = int(input("Enter B intersection C:\n"))
        CnA = int(input("Enter C intersection A:\n"))
        AnBnC = int(input("Enter A intersection B intersection C:\n"))
    except:
        print("Not an integer")
        return -1

    unknown = AuBuC - (A+B+C-AnB-BnC-CnA+AnBnC)
    return unknown

if __name__ == "__main__":
    print(main())
    