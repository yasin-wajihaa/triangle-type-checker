
"""Triangle type checker CLI
Usage:
    python triangle_checker.py
    """
from __future__ import annotations
def triangle_type(a: int,b: int,c: int) -> str:
    """Return triangle type based on intereger side lenghts
    
    Raises:
        ValueError : if any side lenght <= 0 or if the sides don't make a triangle
    """
    if(a <= 0 or b <= 0 or c<= 0):
        raise ValueError("Side lenghts must be positive integers.")
    #checks triangle inequality theorem
    if not (a + b > c and a + c > b and b + c > a):
        raise ValueError("The given side lenghts do not form a triangle.")
    if a==b==c:
        return "Equilateral Triangle"
    elif a==b or b==c or a==c:
        return "Isosceles Triangle"
    else:
        return "Scalene Triangle"
    
def get_positive_ineteger(prompt: str) -> int:
    """Prompt user until they enter valid ineteger fo rside lenght > 0"""
    while True:
        raw=input(prompt).strip()
        try:
            value=int(raw)
        except ValueError:
            print("Invalid input! Please enter a valid integer.")
            continue
        if value <= 0:
            print("Side lenght must be a positive ineteger greater than zero")
            continue
        return value
    
def main() -> None:
    try:
        while True:
            a=get_positive_ineteger("Enter triangle' first side length: ")
            b=get_positive_ineteger("Enter triangle' second side length: ")
            c=get_positive_ineteger("Enter triangle' third side length: ")
            print("Triangle's sides are:", a, b, c)
            try:
                t=triangle_type(a,b,c)
            except ValueError as ve:
                print(f"Not a valid triangle: {ve}")
            else:
                a_or_an="an" if t[0].lower() in "aeiou" else "a"
                print(f"This is {a_or_an} {t} triangle.")
            continue_input = input("Try another? (Y/N)").strip().lower()
            if continue_input != "y":
                print("Exiting the triangle checker.")
                break
    except (KeyboardInterrupt, EOFError):
        print("\nExiting (received interrupt). Goodbye.")
        
if __name__=="__main__":
    main()
