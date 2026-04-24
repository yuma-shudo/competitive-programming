import sys
input = sys.stdin.readline

def main():
    t = int(input())
    for _ in range(t):
        n, a, b = map(int, input().split())
        
        if n % 2 != 0 or (a + b) % 2 == 0:
            print("No")
            continue
            
        print("Yes")
        
        ans_head = ""
        ans_bottom = ""
        ans_mid = ""
        
        index_count = 0
        passed_a = False
        
        for i in range(n // 2):
            index_count += 2
            
            if not passed_a and (index_count - 1 == a or index_count == a):
                passed_a = True
                continue  
                
            if not passed_a:
                ans_head += "R" * (n - 1) + "D" + "L" * (n - 1) + "D"
            else:
                ans_bottom += "D" + "L" * (n - 1) + "D" + "R" * (n - 1)
                
        column_count = 0
        for j in range(n // 2):
            column_count += 2
            
            if column_count < b:
                ans_mid += "DRUR"
            
            elif column_count - 1 == b or column_count == b:
                if b % 2 != 0:
                    ans_mid += "RDR"
                else:
                    ans_mid += "DRR"
                
                for _ in range((n - column_count) // 2):
                    ans_mid += "URDR"
                
                ans_mid = ans_mid[:-1]

                break
                
        ans = ans_head + ans_mid + ans_bottom
        print(ans)

if __name__ == "__main__":
    main()