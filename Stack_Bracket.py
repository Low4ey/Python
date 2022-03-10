def Bracketbalanced(bracket):
	l1 = []
	for char in bracket:
		if char.isalpha() or char in ["+","-","=","/","//","*"]:
			continue
		if char in ["(", "{", "["]:
			l1.append(char)
		else:
			if not l1:
				return False
			current_char = l1.pop()
			if current_char == '(':
				if char != ")":
					return False
			if current_char == '{':
				if char != "}":
					return False
			if current_char == '[':
				if char != "]":
					return False
	if l1:
		return False
	return True
bracket = input()
if Bracketbalanced(bracket):
	print("Balanced")
else:
	print("Not Balanced")

