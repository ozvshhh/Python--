x, y, w, h = map(int,input().split())

x_shortcut = x if x <= w-x else w-x
y_shortcut = y if y <= h-y else h-y

print(x_shortcut if x_shortcut <= y_shortcut else y_shortcut)