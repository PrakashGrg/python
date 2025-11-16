
a = 45
b = 12

def perform_division(a, b):
    try:
        result = a / b
        print(a+b)
    except Exception as e:
        return f"An errror occured. {e}"
    finally:
    
        print(f"db id closed by{a+b}")
    
    return result
print(perform_division(a,b))