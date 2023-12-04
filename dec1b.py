file = open('input1.txt','r')
sum = 0
num_words = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
num_values = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
debug_line = 1

for line in file:
    calibration_value_string = ''
    word_present_in_line = False
    words_in_line = []
    
    for idx in range(len(num_words)):
        word = num_words[idx]
        start_idx = 0      
        while start_idx < len(line):
            index = line.find(word, start_idx)
            if index == -1:
                break # if word not found at all
            words_in_line.append((index, word, num_values[idx])) #throuple = (idx location, word, value)
            start_idx += len(word)
    if words_in_line != []:
        word_present_in_line = True
        first_word_idx, first_word, first_word_value = min(words_in_line)
        last_word_idx, last_word, last_word_value    = max(words_in_line)
   
    for idx in range(len(line)):
        try: 
            int(line[idx])
            if word_present_in_line is False:
                calibration_value_string += line[idx]
                break
            elif idx < first_word_idx and word_present_in_line:
                calibration_value_string += line[idx]
                break
        except:
            continue
    if calibration_value_string == '' and word_present_in_line:
        calibration_value_string += first_word_value
    
    for idx in range(len(line)-1, -1, -1):      
        try: 
            int(line[idx])
            if word_present_in_line is False:
                calibration_value_string += line[idx]
                break
            elif idx > last_word_idx and word_present_in_line:
                calibration_value_string += line[idx]
                break
        except:
            continue
    if len(calibration_value_string) == 1 and word_present_in_line:
        calibration_value_string += last_word_value     
    

    print(debug_line, calibration_value_string)
    debug_line += 1
    sum += int(calibration_value_string)

print(sum)

