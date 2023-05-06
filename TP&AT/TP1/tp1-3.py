lista_nums = [1, 2, 3, 4, 5, 6]
def cumsum(nums):
    soma_list = []
    for i in nums:
        if i == 1:
            soma_list.append(i)
        else:
            index_i = nums.index(i)+1
            soma = sum(nums[0:index_i])
            soma_list.append(soma)
    print(soma_list)

cumsum(lista_nums)
