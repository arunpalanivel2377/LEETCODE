#print name n times using recursion

class NamePrinter:
    def print_name(self,i, n):
        if i > n:
            return
        print("Arun")
        self.print_name(i+1, n)

val = NamePrinter()
val.print_name(1,5)