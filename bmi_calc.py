weight=input("Write here your weight: ")
height=input("Write here your height: ")

wheight_as_int = int(weight)
hight_as_float = float(height)

bmi=wheight_as_int/hight_as_float**2

bmiresult = int(bmi)

print(bmiresult)