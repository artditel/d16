def f():
	try:
		l = int(input())
		d = int(input())
		import turtle
		turtle.speed('slow')

		def tri(length, depth):
			draw_serpinsky(length/2, depth-1)
			turtle.left(120)
			turtle.forward(length/2)
			draw_serpinsky(length/2, depth-1)
			turtle.left(120)
			turtle.forward(length/2)
			turtle.left(120)
			turtle.forward(length)
			turtle.left(120)
			turtle.forward(length/2)
			turtle.left(120)
			draw_serpinsky(length/2, depth-1)
			turtle.forward(length/2)

		def draw_serpinsky(length, depth):
			if depth == 0:
				turtle.forward(length)
				turtle.left(120)
				turtle.forward(length)
				turtle.left(120)
				turtle.forward(length)
			else:
				tri(length,depth)
		draw_serpinsky(l,d)
	except :
		f()
		print("Numbers are required")
f()
