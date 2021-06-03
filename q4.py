def maxMeetings(s, f, n):
    selected_meeting = []
    # Combining all the elements to form group of start, end and position
    pair = []
    for i in range(n):
        p = [s[i], f[i], i]
        pair.append(p)

    # sorting the meeting pair with respect to ending value
    pair.sort(key = lambda x: x[1])

    # At least 1 meeting can take place
    count = 0
    selected_meeting.append(pair[count])
	
    # checking if meeting can take place
    for i in range(1, n):
	    if pair[i][0] > pair[count][1]:
		    selected_meeting.append(pair[i])
		    count = i
			
    return len(selected_meeting)


s = [75250, 50074, 43659, 8931, 11273, 27545, 50879, 77924]
f = [112960, 114515, 81825, 93424, 54316, 35533, 73383, 160252]
n = len(s)

print(maxMeetings(s, f, n))