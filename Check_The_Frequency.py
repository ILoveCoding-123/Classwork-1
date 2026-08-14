test_dict = {'Soccer' : 10, 'and' : 10, 'Cricket' : 18, 'are' : 18, 'my' : 10, 'favorite' : 18, 'sports' : 10}


print("The original dictionary is : " + str(test_dict))


K = 2



res = 0
for key in test_dict:
    if test_dict[key] == K:
        res += 1




print("The frequency of K is : " + str(res))