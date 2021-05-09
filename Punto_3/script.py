from time import time

text = 'afoolishconsistencyisthehobgoblinoflittlemindsadoredbylittlestatesme' \
       'nandphilosophersanddivineswithconsistencyagreatsoulhassimplynothingt' \
       'odohemayaswellconcernhimselfwithhisshadowonthewallspeakwhatyouthinkn' \
       'owinhardwordsandtomorrowspeakwhattomorrowthinksinhardwordsagainthoug' \
       'hitcontradicteverythingyousaidtodayahsoyoushallbesuretobemisundersto' \
       'odisitsobadthentobemisunderstoodpythagoraswasmisunderstoodandsocrate' \
       'sandjesusandlutherandcopernicusandgalileoandnewtonandeverypureandwis' \
       'espiritthatevertookfleshtobegreatistobemisunderstood'


def get_substrings(text: str):
    result_dict = dict()
    for i in range(len(text)):
        for j in range(i+2, len(text)):
            text_aux = text[i:j]
            if text_aux == text_aux[::-1]:
                if text_aux in result_dict:
                    result_dict[text_aux] += 1
                else:
                    result_dict[text_aux] = 1
    return result_dict


start_time = time()
result_dict = get_substrings(text=text)
print(result_dict)
elapsed_time = time() - start_time
print('End Process: ', elapsed_time)


