from collections import Counter
winners=["john","cathy","john","ria","john","cathy"]
d = Counter(winners)
print(d)
print(d.most_common(2))

