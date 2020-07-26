def min_platforms(arrival, departure):
    """
    :param: arrival - list of arrival time
    :param: departure - list of departure time
    TODO - complete this method and return the minimum number of platforms (int) required
    so that no train has to wait for other(s) to leave
    """
    '''
    1. 逻辑：
    忽视具体的车次，只计算出入站的情况。
    每次入站一趟车，则站台需求量+1。每次出站一辆则-1。
    追踪站台需求量的变化，输出最大需求量即可。
    
    2. 过程：
    - 准备阶段
    将arrival和departure都从小到大排序，初始化platform_required 和 max_platform_required
    
    - 求每个节点的platform_required
    i指针指向arrival
    j指针指向departure
    
    每次移动较小的那个时间对应的指针，如果是arrvial指针，则platform_required + 1，如果是departure则-1
    如果本节点的platform_required比max大，则更新。
    
    两个指针都移动到列表的尽头外(i,j 超出index范围)，才算结束。
    
    出错的地方：
    1. 用arrival[i]之前没有验证i是不是在范围内（因为我的while是or链接的，所以会出现arrival已经到了尽头，但是departure没走完的情况）
    2. 实际上不需要用or链接两个表格没走完的条件，因为departure一定是后走完的，而且还不影响我们获得max_platform_required.
    3. 严格 arrival[i] < departure[j]时才增加一辆车，
       意思是，如果有两个车在同一时间一进一出，要先等出去的车出去了，进来的车才进来。
       毕竟要的是“最小站台数量”。
       如果 arrival[i] <= departure[j]时增加一辆车，会认为arrival的车优先级更大，先进来。导致站台数比最小数量多。
    '''
    # 准备阶段
    arrival.sort()
    departure.sort()
    platform_required = 0
    max_platform_required = 0
    # 求每个时间节点的站台需求量
    i = 0
    j = 0
    while i < len(arrival) or j < len(departure):
        # if i^th arrival is scheduled before than j^th departure, 
        # increment platform_required and i as well.
        if i < len(arrival) and arrival[i] < departure[j]:
            platform_required += 1
            print(f'{arrival[i]} \t Arrival \t {platform_required}')
            i += 1
            
            # Update the max value if necessary
            if platform_required > max_platform_required:
                max_platform_required = platform_required
        # Otherwise, decrement platform_required count, and increase j.        
        elif j < len(departure):
            platform_required -= 1
            print(f'{departure[j]} \t Departure \t {platform_required}')
            j += 1
                      
    print(f'return {max_platform_required}')
    return max_platform_required

# TEST
def test_function(test_case):
    arrival = test_case[0]
    departure = test_case[1]
    solution = test_case[2]
    
    output = min_platforms(arrival, departure)
    if output == solution:
        print("Pass")
    else:
        print("Fail")
        
        
arrival = [900,  940, 950,  1100, 1500, 1800]
departure = [910, 1200, 1120, 1130, 1900, 2000]
test_case = [arrival, departure, 3]

test_function(test_case)


arrival = [200, 210, 300, 320, 350, 500]
departure = [230, 340, 320, 430, 400, 520]
test_case = [arrival, departure, 2]
test_function(test_case)