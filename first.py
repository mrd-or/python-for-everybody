def compute(hours, rate):
    if hours > 40:
        return (45-40) * rate * 1.5 + rate * 40
    else:
        return hours * rate


hr = input("Enter Hours: ")
x = float(hr)
rt = input("Enter Rate: ")
y = float(rt)
p = compute(x, y)
print("Pay", p)
