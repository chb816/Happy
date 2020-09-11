class Time:
    def __init__(self, hour, minute, second) :
        self.hour = hour
        self.minute = minute
        self.second = second
    
    @classmethod
    def form_string(cls, string_time) :
        
        hour, minute, second = map(int, string_time.split(':'))
        cls_time = cls(hour, minute, second)
        return cls_time
    
    @staticmethod
    def is_time_valid(string_time) :
        hour, minute, second = map(int, string_time.split(':'))
        return hour < 25 and minute < 60 and second < 61 


string_time = input()

if Time.is_time_valid(string_time) :
    t = Time.form_string(string_time)
    print(t.hour, t.minute, t.second)
else :
    print("잘못된 시간 형식입니다.")
            
