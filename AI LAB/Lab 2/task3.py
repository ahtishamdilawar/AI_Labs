def car_maintenance_check():
    issues = {
        "Engine noise": 4,
        "Check engine light": 5,
        "Poor fuel efficiency": 3,
        "Strange vibrations": 3,
        "Difficulty starting": 4,
        "Braking issues": 5,
        "Unusual exhaust smoke": 4,
        "Steering problems": 3
    }

    total_score = 0

    for issue, weight in issues.items():
        response = input(f"Are you experiencing {issue}? (Yes = 1, No = 0): ")
        if response == "1":
            total_score += weight

    if total_score > 15:
        print(
            "Based on the issues reported, your car may require maintenance. It is recommended to visit a mechanic for a thorough inspection.")
    else:
        print(
            "Based on the issues reported, your car does not seem to require immediate maintenance. However, if you are concerned, consulting a mechanic is always a good idea.")


car_maintenance_check()
