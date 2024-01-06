with open("input.txt", "r") as f:
    data = f.read().splitlines()

def part_one(data) -> int:
    sum = 0

    for line in data:
        
        a = -1
        b = -1
        
        for character in range(len(line)):
            if a == -1 and (ord(line[character]) > 47 and ord(line[character]) < 58):
                a = line[character]
            
            if b == -1 and (ord(line[len(line)-character-1]) > 47 and ord(line[len(line)-character-1]) < 58):
                b = line[len(line)-character-1]

            if a != -1 and b != -1:
                sum += int(a+b)
                break
    return sum
print(part_one(data)) 
    
           