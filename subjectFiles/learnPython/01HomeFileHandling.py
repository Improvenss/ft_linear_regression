# Open file.
f = open("demofile.txt", "r")
print(f.read(), '\n') # This .read() function returns full readed data.

# Open with full path.
f = open("/Users/yuandre/Desktop/ft_linear_regression/subjectFiles/learnPython/demofile.txt", "r")
print(f.read(5), '\n') # But you can read only 5 character. (Hello)
# ---------------------

# Read lines
f = open("demofile.txt", "r")
print(f.readline()) # output -> (Hello! Welcome to demofile.txt)

f = open("demofile.txt", "r")
print(f.readline(4)) # You can read only 4 character from readed line. output-> (Hell)
# ---------------------

f = open("demofile.txt", "r")
for x in f:
	print(x)