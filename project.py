import random 

finger_pattern_a =[["x-0-2-2-2-0"], ["5-x-7-6-5-x"],]

def difficulty(patterns) -> list:
    labeled_patterns = []
    for index, pattern in enumerate(patterns):
        #Assign label "easy" to the first sublist, "hard" to the rest
        if index == 0:
            diff = "Easy"
        else:
            diff = "Hard"
        labeled_patterns.append((pattern, diff))
    return(labeled_patterns)
labeled_patterns = difficulty(finger_pattern_a) 

for pattern, diff in labeled_patterns:
    print(f"{diff}: {pattern}")



finger_pattern_b =[["x-2-4-4-4-2"], ["y"]]

finger_pattern_c = 124124

finger_pattern_d =3123

finger_pattern_e =512452

finger_pattern_f =5151

finger_pattern_g =5151

finger_pattern_Gflator_Fflat =51

finger_pattern_Dflat_Csharp =51

finger_pattern_Aflat =51

finger_pattern_Eflat =51

finger_pattern_Bflat =51













major_C_scale = ["C", "G", "F", "Dm", "Am", "Em"]

user_input = "yes"

x = input()
print(x)

def chords_in_c(major_C_scale) -> list:
    
    if user_input.lower() == "yes":
        

        #without_c = [chord for chord in major_C_scale if chord != "C"]
        
        without_c2 = []

        for chord in major_C_scale:
            if chord != "C":
                without_c2.append(chord)
        
        shuffled_chords = random.sample(without_c2, 3)
        
        result = (["C"] + shuffled_chords[:3])
        
        print(result)

    elif user_input.lower() == "no":
        result = random.sample(major_C_scale, 4)
        print(result)

random_chords = chords_in_c(major_C_scale)

    










Circle_fifths_major_G = [["G", ]]







Circle_fifths_major_D = [["D", ]]








Circle_fifths_major_A = [["A", ]]






Circle_fifths_major_E = [["E", ]]






Circle_fifths_major_B = [["B", ]]





Circle_fifths_major_Gf = [["Gf", ]]






Circle_fifths_major_Df = [["Df", ]]







Circle_fifths_major_Af = [["Af", ]]
Circle_fifths_major_Ef = [["Ef", ]]
Circle_fifths_major_Bf = [["C", ]]
Circle_fifths_major_F = [["F", ]]