def devolverDistinto(num1, num2, num3):
    sum = num1 + num2 + num3
    
    if (sum < 10):
        valorMenour = min(num1, num2, num3)
        print(f"Número menor: {valorMenour}")
    elif (sum > 15):
        valorMayor = max(num1, num2, num3)
        print(f"Número mayor: {valorMayor}")
    else:
        if (num1 > num2) and (num1 < num3):
            print(f"Número intermedio: {num1}")
        elif (num2 > num1) and (num2 < num3):
            print(f"Número intermedio: {num2}")
        else:
            print(f"Número intermedio: {num3}")

devolverDistinto(12, 2, 7)