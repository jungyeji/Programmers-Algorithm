def solution(genres, plays):
    answer = []
    genres_dict = {}
    genres_plays = {}
    for i in range(len(genres)):
        if genres[i] not in genres_dict:
            genres_dict[genres[i]]=[(plays[i],i)]
            genres_plays[genres[i]] = plays[i]
        else:
            genres_dict[genres[i]].append((plays[i],i))
            genres_plays[genres[i]] += plays[i]
            
    sorted_genres_plays = sorted(genres_plays.items(), key=lambda x: x[1], reverse=True)
    
    for genre,_ in sorted_genres_plays:
        songs = genres_dict[genre]
        sorted_songs = sorted(songs, key=lambda x: x[0], reverse=True)
        if len(sorted_songs)>1:
            answer.append(sorted_songs[0][1])
            answer.append(sorted_songs[1][1])
        elif len(sorted_songs)==1:
            answer.append(sorted_songs[0][1])
        

    return answer
