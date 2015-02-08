stratset = None
def fair(me, enemy):
	global stratset
	if len(enemy) == 99:
		return False
	if stratset != None:
		if stratset:
			if all(enemy):
				return True
			else:
				return False
		return stratset
	if len(enemy) < 3:
		return True
	if not any(enemy) and len(enemy) == 3: #we are playing against 'angry'
		statset = False
		return False
	if all(enemy) and len(enemy) == 3: #kind or unforgiving maybe?
		stratset = True
		return True


