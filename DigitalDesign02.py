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

        return q

    def t_flipflop(self, t, q_prev, clk):
        if clk == 1 and t == 1:
            q = 1 - q_prev
        else:
            q = q_prev

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
            else: 
                q = 1 - q_prev

        return q
    
"""
以上為class 請勿亂碰
"""

dd = DigitalDesign()

q_master = 0
q_slave = 0   

def master_slave_d(d, clk):
    global q_master, q_slave

    q_master = dd.d_flipflop(d, q_master, clk)

    slave_clk = dd.comp(clk)
    q_slave = dd.d_flipflop(q_master, q_slave, slave_clk)

    print(f"Master(En={clk}) → Y={q_master}")
    print(f"Slave(En={slave_clk}) → Q={q_slave}")

    return q_slave

print("\n=== Master–Slave D Flip-Flop (Manual Input) ===")
print("輸入 D 與 CLK（0/1）")
print("輸入 end 結束\n")

while True:
    user_input_d = input("D > ")

    if user_input_d.lower() == "end":
        print("結束模擬")
        break

    user_input_clk = input("CLK > ")

    try:
        d = int(user_input_d)
        clk = int(user_input_clk)

        if d not in (0, 1) or clk not in (0, 1):
            print("D 與 CLK 必須是 0 或 1\n")
            continue

        print(f"\nInput: D={d}, CLK={clk}")
        q = master_slave_d(d, clk)
        print(f"Output Q = {q}\n")

    except ValueError and KeyboardInterrupt:
        print("格式錯誤，請輸入 0 / 1 或 end\n")
        print("或是ctrl+C中止程式")