from pprint import pprint

def merge(l1, l2):
	resp_val = []
	length = max(len(l1), len(l2))
	while l1 or l2:
		if not l1:
			val = l2[0]
			l2 = l2[1:]
		elif not l2:
			val = l1[0]
			l1 = l1[1:]
		elif l1[0] > l2[0]:
			val = l2[0]
			l2 = l2[1:]
		else:
			val = l1[0]
			l1 = l1[1:]
		resp_val.append(val)
	return resp_val

def mergesort(l):
	if not l:
		return []
	elif len(l) == 1:
		return l
	mid = len(l) / 2
	l1 = l[:mid]
	l2 = l[mid:]
	return merge(mergesort(l1), mergesort(l2))

a = [5,1,10,4,5,2,7,23,14,11]
print 'Starting list:'
pprint(a)
print '\nEnding list:'
pprint(mergesort(a))
print '\nList length: ' + str(len(a)) 