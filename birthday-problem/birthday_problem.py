def find_duplicate_birthday(classroom):

    seen_birthdays = set()

    for birthday in classroom:

        if birthday in seen_birthdays:
            return birthday

        seen_birthdays.add(birthday)

    return "No matching pair found"


test_classroom = ["22-11", "22-11", "03-01", "15-05", "30-12"]

result = find_duplicate_birthday(test_classroom)

print(f"Search result: {result}")