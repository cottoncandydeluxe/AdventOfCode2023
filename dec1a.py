file = open('input1.txt','r')
sum = 0

for line in file:
    calibration_value_string = ''
    
    for ch in line:
        try: 
            int(ch)
            calibration_value_string += ch
            break
        except:
            continue
    
    for ch in reversed(line):
        try:
            int(ch)
            calibration_value_string += ch
            break
        except:
            continue      
    
    sum += int(calibration_value_string)

print(sum)

