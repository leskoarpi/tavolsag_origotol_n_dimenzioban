from math import sqrt
def tavolsag_n_d(*nums):
    lista=[]
    result = 0
    index = 0
    for i in nums:
        lista.append(nums[index])
        index+=1
    index = 0
    finalresult = 0
    retkeslista =[]
    for x in lista:
        negyzet = lista[index]**2
        retkeslista.append(negyzet)
        index += 1
    finalresult = sqrt(sum(retkeslista))

    return finalresult


print(tavolsag_n_d(1,2,3,5,6,14))
