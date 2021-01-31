def main():
     i = 1
     j = 7

     while i <=9:
        for volta in range(1,4):
            print(f"I = {i} J = {j}")
            j -=1
        
        i += 2
        j += 5

if __name__=="__main__":
    main()