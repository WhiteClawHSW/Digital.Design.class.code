import time

class DigitalDesign:
    def __init__(self):
        print("Digital Design Tool (Flip-Flop Simulator)")
        print("Author: HSW\n")

    def comp(self, p):
        return 1 - p

    def d_flipflop(self, d, q_prev, clk):
        if clk == 1:
            q = d
        else:
            q = q_prev

        print(f"D={d} CLK={clk} → Q={q}")
        return q

    def t_flipflop(self, t, q_prev, clk):
        if clk == 1 and t == 1:
            q = 1 - q_prev
        else:
            q = q_prev

        print(f"T={t} CLK={clk} → Q={q}")
        return q
    
    def jk_flipflop(self, j, k, q_prev, clk):
        if clk == 0:
            q = q_prev
        else:
            if j == 0 and k == 0:
                q = q_prev
            elif j == 0 and k == 1:
                q = 0
            elif j == 1 and k == 0:
                q = 1
            else:  # j == 1 and k == 1
                q = 1 - q_prev

        print(f"J={j} K={k} CLK={clk} → Q={q}")
        return q


"""
主程式
"""

dd = DigitalDesign()
clk = 0
mode = input("Select FF type (D / T / JK): ").upper()
while True:
    q = input("Initial Q (0/1): ")
    try:
        q = int(q)
        if q == 0 or q == 1:
            break
    except:
        print('try again')
print("\n--- Simulation Start (Ctrl+C to stop) ---\n")

try:
    while True:
        if mode == "D":
            d = int(input("Input D (0/1): "))
            if d == 0 or d == 1:
                q = dd.d_flipflop(d, q, clk)
            else:
                print("\nSimulation stopped.")
                break

        elif mode == "T":
            t = int(input("Input T (0/1): "))
            if t == 0 or t == 1:
                q = dd.t_flipflop(t, q, clk)
            else:
                print("\nSimulation stopped.")
                break

        elif mode == "JK":
            j = int(input("Input J (0/1): "))
            k = int(input("Input K (0/1): "))
            if (j == 0 or j == 1) and (k == 0 or k == 1):
                q = dd.jk_flipflop(j, k, q, clk)
            else:
                print("\nSimulation stopped.")
                break

        else:
            print("Unknown mode")
            break

        clk = 1 - clk   # clock toggle
        time.sleep(1)

except KeyboardInterrupt and ValueError:
    print("\nSimulation stopped.")



