#print numbers 1 to n
class NamePrinter:
    def print_name(self,i, n):
        if i > n:
            return
        print(i)
        self.print_name(i+1, n)

val = NamePrinter()
val.print_name(1,5)
print("")
class NumberPrinter:
    def print_numbers(self,n):
        if n == 0:
            return
        self.print_numbers(n-1)
        print(n)

val2 = NumberPrinter()
val2.print_numbers(5)