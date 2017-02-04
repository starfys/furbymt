from hashlib import md5

# returns a number between 1-100 for a string value
def lucky(name):

	name = name.encode('utf-8')
	return (int(md5(name).hexdigest(), 16) % 100)