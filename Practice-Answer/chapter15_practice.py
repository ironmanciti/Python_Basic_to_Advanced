doc1 = "apple banana everyone like likely watch card holder"
doc2 = "apple banana coupon passport love you"

tokenized_doc1 = doc1.split()
tokenized_doc2 = doc2.split()

print(tokenized_doc1)
print(tokenized_doc2)

union = set(tokenized_doc1).union(set(tokenized_doc2))
print(union)
print(len(union))

inter = set(tokenized_doc1).intersection(set(tokenized_doc2))

print(inter)

print("두 문서간의 Jaccard 유사도 : {:.2f} ".format(len(inter)/len(union)))
