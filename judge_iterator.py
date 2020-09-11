class  TimeIterator :
    def __init__(self, st_time, end_time):
        self.st_time = st_time
        self.end_time = end_time
    
    def __getitem__(self, index):
        if self.st_time < self.end_time:
            t = self.st_time
            h = int((t / 3600) % 24)
            m = int((t / 60) % 60)
            s = int(t % 60)
            rt = '{0:02d}:{1:02d}:{2:02d}'.format(h,m,s)
            #문자열 사용시 format 이용할것.
            self.st_time = self.st_time + 1
            return rt
        else :
            raise StopIteration
        
        if index < self.end_time and index < 10 :
            return  index
        else :
            raise IndexError
    
st_time, end_time, index = map(int, input().split())

for  i  in TimeIterator(st_time, end_time) :
    print(i)

print(TimeIterator(st_time, end_time)[index])
