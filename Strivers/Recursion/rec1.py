count = 0
def func():
    global count
    if (count == 4):
        return
    print(count)
    count += 1
    func()


func()