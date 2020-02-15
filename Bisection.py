def bisect(L,num):

    def bisecthelp (L, num, low, high):
        if high == low:
            return L[high] == num

        mid = (high+low)//2

        if num == L[mid]:
            return True

        elif L[mid] < num:
            # if low == mid:
            #     return False
            # else:
            return bisecthelp(L,num,mid+1,high)
        else:
            if low == mid:
                return False
            else:
                return bisecthelp(L,num, low, mid-1)
    if len(L) == 0:
        return False
    else:
        return bisecthelp(L,num, 0, len(L)-1)


L = [1, 4, 10, 23, 35, 40, 78]
num = int(input("Enter a number to search the list: "))

# num = 1
#
#
IsPresent = bisect(L,num)
# print(IsPresent)

if IsPresent == True:
    print("number", num, "in the list")
else:
    print("number", num, " not in the list")
