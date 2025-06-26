import sys
input = lambda: sys.stdin.readline().rstrip()

def main():
    lv = int(input())

    def query(q, d1, d2):
        if lv >= d2:
            return 100
        elif lv >= d1:
            return 300
        elif lv >= q:
            return 500
        return 0
    
    print(
        query(200, 210, 220), query(210, 220, 225), query(220, 225, 230),
        query(225, 230, 235), query(230, 235, 245), query(235, 245, 250), 
    )
    print(
        query(260, 265, 270), query(265, 270, 275), query(270, 275, 280),
        query(275, 280, 285), query(280, 285, 290), query(285, 290, 295), 
        query(290, 295, 300),
    )

main()