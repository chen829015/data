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

#文字記數
wc = {} #word_count
for d in data:
	words = d.split()
	for word in words:
		if word in wc:
			wc[word] += 1 #如果word有出現在wc ditionary裡就+1 
		else:
			wc[word] = 1 #新增Key進dictionary
for word in wc:
	if wc[word] > 1000000:
		print(word, wc[word])

while True:
	word = input('search word:')
	if word == 'q':
		break
	if word in wc:
		print(word, 'have:', wc[word], 'time')
	else:
		print('there is no the word!')
print('thanks for searching!')