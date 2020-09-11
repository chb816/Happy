korean, english, mathmatics, science = map(int, input().split())

def get_min_score(korean, english, mathmatics, science) :
    min_score = min(korean, english, mathmatics, science)
    return min_score
def get_max_score(korean, english, mathmatics, science) :  
    max_score = max(korean, english, mathmatics, science)
    return max_score
def get_averege(korean, english, mathmatics, science) :
    averege = (korean+english+mathmatics+science)/4
    return averege

def result(korean, english, mathmatics, science):
    min_score = min(korean, english, mathmatics, science)
    max_score = max(korean, english, mathmatics, science)
    averege = (korean+english+mathmatics+science)/4
    return min_score, max_score, averege

maxs = get_max_score(korean, english ,mathmatics, science)
mins = get_min_score(korean, english, mathmatics, science)
avr = get_averege(korean, english, mathmatics, science)

maxr, minr, avrr = result(korean, english, mathmatics, science)

print("낮은점수 : {0:.2f}, 높은점수 : {1:.2f}, 평균 : {2:.2f}".format(maxr, minr, avrr))

print("낮은점수 : {0:.2f}, 높은점수 : {1:.2f}, 평균 : {2:.2f}".format(mins, maxs, avr))

