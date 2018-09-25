import pandas as pd
from collections import defaultdict
import io

file = "Dand_Prakriya.xlsx"
xl = pd.ExcelFile(file)
df = xl.parse('Sheet')

df.rename(columns={'THE CODE OF CRIMINAL PROCEDURE, 1973 ACT NO. 2 OF 1974 [25th January, 1974.] An Act to consolidate and amend the law relating to Criminal Procedure. BE it enacted by Parliament in the twenty-fourth Year of the Republic of India as follows:-': 'english', 'दण्ड प्रक्रिया संहिता , 1973 (1974 का अधिनियम संख्यांक 2) [25 जनवरी , 1974] दण्ड प्रक्रिया संबंधी विधि का समेकन और संशोधन करने के लिए अधिनियम भारत गणराज्य के चौबीसवें वर्ष में संसद् द्वारा निम्नलिखित रूप में यह अधिनियमित हो : -': 'hindi'}, inplace=True)
stopwordsInHindi = ["अंदर","अत","अदि","अप","अपना","अपनि","अपनी","अपने",
                    "अभि","अभी","आदि","आप","इंहिं","इंहें","इंहों","इतयादि",
                    "इत्यादि","इन","इनका","इन्हीं","इन्हें","इन्हों","इस","इसका",
                    "इसकि","इसकी","इसके","इसमें","इसि","इसी","इसे","उंहिं",
                    "उंहें","उंहों","उन","उनका","उनकि","उनकी","उनके","उनको",
                    "उन्हीं","उन्हें","उन्हों","उस","उसके","उसि","उसी","उसे","एक",
                    "एवं","एस","एसे","ऐसे","ओर","और","कइ","कई","कर","करता",
                    "करते","करना","करने","करें","कहते","कहा","का","काफि",
                    "काफ़ी","कि","किंहें","किंहों","कितना","किन्हें","किन्हों","किया",
                    "किर","किस","किसि","किसी","किसे","की","कुछ","कुल","के",
                    "को","कोइ","कोई","कोन","कोनसा","कौन","कौनसा","गया",
                    "घर","जब","जहाँ","जहां","जा","जिंहें","जिंहों","जितना","जिधर",
                    "जिन","जिन्हें","जिन्हों","जिस","जिसे","जीधर","जेसा","जेसे",
                    "जैसा","जैसे","जो","तक","तब","तरह","तिंहें","तिंहों","तिन",
                    "तिन्हें","तिन्हों","तिस","तिसे","तो","था","थि","थी","थे","दबारा",
                    "दवारा","दिया","दुसरा","दुसरे","दूसरे","दो","द्वारा","न","नहिं",
                    "नहीं","ना","निचे","निहायत","नीचे","ने","पर","पहले","पुरा",
                    "पूरा","पे","फिर","बनि","बनी","बहि","बही","बहुत","बाद",
                    "बाला","बिलकुल","भि","भितर","भी","भीतर","मगर","मानो",
                    "मे","में","यदि","यह","यहाँ","यहां","यहि","यही","या","यिह",
                    "ये","रखें","रवासा","रहा","रहे","ऱ्वासा","लिए","लिये","लेकिन",
                    "व","वगेरह","वरग","वर्ग","वह","वहाँ","वहां","वहिं","वहीं",
                    "वाले","वुह","वे","वग़ैरह","संग","सकता","सकते","सबसे","सभि",
                    "सभी","साथ","साबुत","साभ","सारा","से","सो","हि","ही","हुअ",
                    "हुआ","हुइ","हुई","हुए","हे","हें","है","हैं","हो","होता","होति",
                    "होती","होते","होना","होने"]
char_to_remove = ["1","2","3","4","5","6","7","8","9","0",
                  ",","-","|",":",";","a","b","c","d","e",
                  "f","g","h","i","j","k","l","m","n","o",
                  "p","q","r","s","t","u","v","w","x","y",
                  "z","(","}","]","?","'",'"',"*","+","_",")",
                  ".","[","{","A","B","C","D","E","F","G",
                  "H","I","J","K","L","M","O","P","Q","R",
                  "S","T","U","V","W","X","Y","Z"]

new_dict = defaultdict(list)
j = 2
for item in df["hindi"]:
    temp = item.split()
    for i in temp:
        flag = False
        for x in char_to_remove:
            if(x in i):
                flag = True
                break
        if(flag == False):
                new_dict[i].append(j)
    j = j + 1;

for sw in stopwordsInHindi:
    if sw in new_dict:
        del new_dict[sw]

def booleanAndModel(a, b):
    final_set = set()
    if(new_dict[a] and new_dict[b]):
        set_a = set()
        set_b = set()
        for v in new_dict[a]:
            set_a.add(v)
        for v in new_dict[b]:
            set_b.add(v)
        final_set = set_a.intersection(set_b)
        return final_set
    else:
        return final_set
def booleanOrModel(a, b):
    final_set = set()
    if(new_dict[a] and new_dict[b]):
        set_a = set()
        set_b = set()
        for v in new_dict[a]:
            set_a.add(v)
        for v in new_dict[b]:
            set_b.add(v)
        final_set = set_a.union(set_b)
        return final_set
    else:
        return final_set
def booleanNotModel(a, b):
    final_set = set()
    if(new_dict[a] and new_dict[b]):
        set_a = set()
        set_b = set()
        for v in new_dict[a]:
            set_a.add(v)
        for v in new_dict[b]:
            set_b.add(v)
        final_set = set_a.difference(set_b)
        return final_set
    else:
        return final_set

def main():
    input_1 = input('Enter first word:')
    input_2 = input('Enter second word:')
    op = input('Enter the operator(and, or, not) note that operator name is case sensitive:')
    if(op == 'and'):
        result = booleanAndModel(input_1, input_2)
        print(' '.join(['%1d' %n for n in sorted(result)]))
    elif (op == 'or'):
        result = booleanOrModel(input_1, input_2)
        print(' '.join(['%1d' % n for n in sorted(result)]))
    elif (op == 'not'):
        result = booleanNotModel(input_1, input_2)
        print(' '.join(['%1d' % n for n in sorted(result)]))

if __name__ == "__main__":
    main()
