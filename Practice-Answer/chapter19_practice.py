test_list = ['this is a book', 'good morning', 'apple', 'apple orange pear', 'hello python and functional programmiong']

for s in test_list:
    print((lambda x: len(x))(s.split(' ')))