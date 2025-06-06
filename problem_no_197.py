from collections import Counter
text = "nlaebolko"
freq = Counter(text)
b_count = freq["b"]
a_count = freq["a"]
l_count = freq["l"] // 2
o_count = freq["o"] // 2
n_count = freq["b"]
print(min(b_count, a_count, l_count, o_count, n_count))



    
