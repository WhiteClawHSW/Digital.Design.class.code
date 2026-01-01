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
            else:  # j == 1 and k == 1
                q = 1 - q_prev

        return q