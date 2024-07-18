#
# Example file for working with conditional statements
# LinkedIn Learning Python course by Joe Marini
#



def main():
    x, y = int(input("Nhap x ")),  int(input("Nhap y "))

    # conditional flow uses if, elif, else
    # if x < y:
    #     return "X is less than y"
    # elif x > y:
    #     return "X is greater than y"
    # else:
    #     return "X = y"
    
    
    # conditional statements let you use "a if C else b"
    ketqua = "X is less than y " if x < y else "X is greater or equal to y"
    print(ketqua)
    # match-case makes it easy to compare multiple values
    value = input("Nhap = ")
    match value: 
        case "one":
            return 1
        case "two" | "three":
            return (2,3)
        case _:
            return -1

if __name__ == "__main__":
    print(main())