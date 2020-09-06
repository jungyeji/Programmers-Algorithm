def solution(cacheSize, cities):
    answer = 0
    
    if cacheSize == 0 :
        answer = len(cities)*5
    else:
        cache = []
        for city in cities:
            city = city.lower()
            if city in cache:
                cache.pop(cache.index(city))
                cache.append(city)
                answer += 1
            else:
                if len(cache) < cacheSize:
                    cache.append(city)
                    answer += 5
                else:
                    cache.pop(0)
                    cache.append(city)
                    answer += 5
        
    return answer
