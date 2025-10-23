# 1. Write a function to check if a number is even.
def is_even(n):
    return n % 2 == 0


# 2. Write a function to check if a number is palindrome.
def is_palindrome(s):
    return s == "".join(reversed(s))


# 3. Write a function to check if a number is power of 2.
def is_power_of_two(n):
    if n == 0:
        return True

    while n % 2 == 0:
        n = n / 2
        if n == 1:
            return True

    return False


# 4. Write a function to convert a given string to all uppercase if it contains at least 2
# uppercase characters in the first 4 characters.
def to_uppercase(str):
    count = 0
    for i in range(min(4, len(str))):
        if str[i].isupper():
            count += 1

    if count == 2:
        return str.upper()
    return str


# 5. Given a list iterate it and display numbers which are divisible by 5 and if you
# find number greater than 150 stop the loop iteration
def dividable(l, divisor=5, limit=150):
    for i in l:
        if i > limit:
            break

        if i % divisor == 0:
            print(i, end=" ")


# 6.Write a function that takes a list of words and groups the words by their length
# using a dictionary
def group_by_length(words):
    grouped_words = {}

    for word in words:
        length = len(word)

        if length in grouped_words:
            grouped_words[length].append(word)
        else:
            grouped_words[length] = [word]

    return grouped_words


# 7. Create a class Person with first_name and last_name as constructor
# parameters. The class should have a function get_fullname which returns the
# person’s full name (first_name + last_name). Create another class Student,
# inheriting from Person. Student’s get_fullname function should return students
# full name followed by ‘-st.’
class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def get_fullname(self):
        return self.first_name + " " + self.last_name


class Student(Person):
    def get_fullname(self):
        return super().get_fullname() + " " + "-st"


def main():

    print("Testing is_even:")
    print(4 , is_even(4))
    print(7, is_even(7))
    print()

    print("Testing is_palindrome:")
    print(121, is_palindrome("121"))
    print(123, is_palindrome("123"))
    print()

    print("Testing is_power_of_two:")
    print(9, is_power_of_two(9))
    print(16, is_power_of_two(16))
    print()

    print("Testing to_uppercase:")
    print("HeLlo", '->', to_uppercase("HeLlo"))
    print("AbcdE", '->', to_uppercase("AbcdE"))
    print("ABcd", '->', to_uppercase("ABcd"))
    print()

    print("Testing dividable:")
    numbers = [10, 25, 30, 160, 10]
    print("Original: ", numbers)
    dividable(numbers)
    print("\n")

    print("Testing group_by_length:")
    words = ["Lorem", "ele", "sit", "incididunt", "a", "su", "dom", "ouch", "ipsum"]
    print(group_by_length(words))
    print()


    print("Testing Person and Student:")
    p = Person("John", "Doe")
    s = Student("Mateo", "Kodra")
    print(p.get_fullname())
    print(s.get_fullname())
    print()


if __name__ == "__main__":
    main()
