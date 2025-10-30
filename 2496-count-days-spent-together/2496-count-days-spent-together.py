class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        month_day = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        
        # Parse dates
        alice_month = int(arriveAlice[:2])
        bob_month = int(arriveBob[:2])
        alice_lmonth = int(leaveAlice[:2])
        bob_lmonth = int(leaveBob[:2])

        alice_day = int(arriveAlice[3:])
        bob_day = int(arriveBob[3:])
        alice_lday = int(leaveAlice[3:])
        bob_lday = int(leaveBob[3:])

        
        arrive_month = max(alice_month, bob_month)
        arrive_day = max(alice_day, bob_day) if alice_month == bob_month else (
            alice_day if arrive_month == alice_month else bob_day
        )

        leave_month = min(alice_lmonth, bob_lmonth)
        leave_day = min(alice_lday, bob_lday) if alice_lmonth == bob_lmonth else (
            alice_lday if leave_month == alice_lmonth else bob_lday
        )

        
        if (arrive_month > leave_month) or (arrive_month == leave_month and arrive_day > leave_day):
            return 0

        def count_day(am, lm, ad, ld):
            count = month_day[am - 1] - ad + 1  
            x = am + 1
            while x < lm: 
                count += month_day[x - 1]
                x += 1
            if x == lm:  
                count += ld
            return count

        if arrive_month == leave_month:
            return leave_day - arrive_day + 1
        else:
            return count_day(arrive_month, leave_month, arrive_day, leave_day)