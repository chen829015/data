data = []
c = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		c += 1
		if c % 1000 == 0:
			print(len(data))
print('loeaded, total', len(data), 'documents')

#calculate the avg. review lengh
sum_len = 0
for d in data:
	sum_len = sum_len + len(d)
print('average review lengh:', sum_len / len(data))

#filter review, "f = [d for d in data if len(d) < 100]"
f = []
for d in data:
	if len(d) < 100:
		f.append(d)
print('total', len(f),'reviews lengh < 100' )

# tips: gd = [d for d in data if 'good' in d]
gd = []
for d in data:
	if 'good' in d:
 		gd.append(d)
print('total mentioned', len(gd), 'good in reviews')



#outputr = [(number-1) for number in reference if number % 2 == 0]