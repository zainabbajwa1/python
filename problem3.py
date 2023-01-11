# Problem # 3
# Using keys and indexing, grab the 'hello' from the following dictionaries:
dict_1={'simple_key':'hello'}
dict_2={'k1':{'k2':'hello'}}
dict_3={'k1':[{'nest_key':['this is deep',['hello']]}]}
# grab the "hello" from dictionaries:
print("Answers")
print(dict_1['simple_key'])
print(dict_2['k1']['k2'])
print(dict_3['k1'][0]['nest_key'][1][0])