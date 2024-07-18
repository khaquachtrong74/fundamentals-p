#
# Example file for working with loops
# LinkedIn Learning Python course by Joe Marini
#


def main():
    x = 0

    # TODO: define a while loop
    while(x < 3):
        print(x)
        x+=1

    # TODO: define a for loop
    for a in range(3):# từ 0 tới 9
        print(a)
    # TODO: use a for loop over a collection
    days = ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
    for thu in days:
        print(thu)

    # TODO: use the break and continue statements
    for i in range(10):
        if i % 2 == 0:
            continue
        if i == 7:
            print(i)
            break

    # TODO: using the enumerate() function to get index 
    for idx, i in enumerate(range(6)):
        print(f"{idx}<=>{i}")
  
if __name__ == "__main__":
    main()