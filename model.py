

class main_class():

    def mistake_count(self,original, user_test):
        word_mistake = 0

        for i in range(len(original)):
            try:
                if original[i] != user_test[i]:
                    word_mistake += 1
            except:
                word_mistake += 1
        return word_mistake

    def time_calculation(self,s_time, e_time):
        s_time = float(s_time)
        e_time = float(e_time)

        difference = (e_time - s_time)
        round_difference = round(difference)
        if round_difference > 60:
            minute = round((round_difference / 60), 2)
            # print(f"Total time taken : {minute} minutes")

            return minute

        elif round_difference < 60:
            # print(f"Total time taken : {round_difference} seconds")
            return round_difference
