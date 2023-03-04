
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

