def calculate_grade(marks):
    """
    Calculate letter grade based on marks.
    
    Args:
        marks: A numeric value (int or float) between 0 and 100
        
    Returns:
        str: Letter grade (A, B, C, D, F) or error message
        
    Grade Scale:
        A: 90-100
        B: 80-89
        C: 70-79
        D: 60-69
        F: Below 60
    """
    # Input validation
    try:
        marks = float(marks)
    except (ValueError, TypeError):
        return "Error: Marks must be a number"
    
    if marks < 0 or marks > 100:
        return "Error: Marks must be between 0 and 100"
    
    # Grade calculation with improved scale
    if marks >= 90:
        return "A"
    elif marks >= 80:
        return "B"
    elif marks >= 70:
        return "C"
    elif marks >= 60:
        return "D"
    else:
        return "F"


def get_grade_description(grade):
    """Get description for a letter grade."""
    descriptions = {
        "A": "Excellent",
        "B": "Good",
        "C": "Average",
        "D": "Below Average",
        "F": "Fail"
    }
    return descriptions.get(grade, "Unknown")


if __name__ == "__main__":
    print("=" * 40)
    print("Grade Calculator")
    print("=" * 40)
    
    # Test cases
    test_marks = [95, 82, 75, 65, 58, -5, 105, "abc"]
    
    print("\nTest Results:")
    for marks in test_marks:
        grade = calculate_grade(marks)
        if grade.startswith("Error"):
            print(f"Marks: {marks:>5} → {grade}")
        else:
            description = get_grade_description(grade)
            print(f"Marks: {marks:>5} → Grade: {grade} ({description})")
    
    print("\n" + "=" * 40)
    print("Interactive Mode:")
    print("=" * 40)
    
    try:
        user_marks = input("Enter your marks (0-100): ")
        grade = calculate_grade(user_marks)
        
        if grade.startswith("Error"):
            print(f"❌ {grade}")
        else:
            description = get_grade_description(grade)
            print(f"✓ Your Grade: {grade} ({description})")
    except KeyboardInterrupt:
        print("\nProgram terminated by user.")
