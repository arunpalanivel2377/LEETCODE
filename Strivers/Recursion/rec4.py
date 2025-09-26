
class num:
    def print_num(self,n):
        if n == 0:
            return
        print(n)
        self.print_num(n-1)

val = num()
val.print_num(5)