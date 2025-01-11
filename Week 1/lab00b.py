#CS-171

# A function to average six grade components
def calculateGrade(lab, hw, rd, lect, midterm, final):
 average = (lab + hw + rd + lect + midterm + final) / 6 
 return average
# The code below will test the calculateGrade function
if __name__ == "__main__":
 result = calculateGrade(100, 90, 100, 90, 79, 84) 
 print("Your overall grade is", result)