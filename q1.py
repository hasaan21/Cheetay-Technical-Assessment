def activitySelection(start, end, N):    
    pair = []
    selected_activity = []

    # Combining all the elements to form pair of start and end
    for i in range(n):
        p = [start[i], end[i]]
        pair.append(p)

    # sorting the meeting pair with respect to ending value
    pair.sort(key = lambda x: x[1])

    # At least 1 activity can take place
    count = 0
    selected_activity.append(pair[count])
	
    # checking if activity can be performed
    for i in range(1, n):
	    if pair[i][0] > pair[count][1]:
		    selected_activity.append(pair[i])
		    count = i
			
    return len(selected_activity)
    

start = [1, 3, 2, 5]
end = [2, 4, 3, 6]
n = len(start)

print(activitySelection(start, end, n))    