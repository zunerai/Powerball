# Powerball story:
#
# As a Greenphire employee I would like to add my favorite 6 numbers to
# consider for a powerball entry ticket so that I can win 1 billion dollars.
#
#
# 1.Capture the name of the employees entering the number.
# 2.The first 5 favorite numbers will need to be in the range of 1 to 69 and unique. (remember that this is a drawing so there cannot be duplicates
# in this range of 5 numbers)
# 3.6th favorite number will need to be in the range of 1 to 26 and flagged as the 6th Powerball number.
# 4.Keep count of each individual favorite number provided to determine which numbers to use in our final winning number. (ie count the duplicates).
# 5.Retrieve the max count of each unique duplicate number and use them as the powerball numbers.
# 6.if there is a tie based on the max counts randomly select the tied number.
# 7.Display all employees with their corresponding number entries.
# 8.Display the final powerball number based on the requirements above.
#
#
#
#
# Sample output:
# Enter your first name: Wade
# Enter your last name: Wilson
# select 1st # (1 thru 69): 12
# select 2nd # (1 thru 69 excluding 12): 20
# select 3rd # (1 thru 69 excluding 12 and 20): 23
# select 4th # (1 thru 69 excluding 12, 20, and 23): 56
# select 5th # (1 thru 69 excluding 12, 20, 23, and 56): 30
# select Power Ball # (1 thru 26): 25
#
# Wade Wilson 15 26 33 60 34 powerball: 16
# Frank Castle 15 26 34 56 61 powerball: 16
#
# Powerball winning number:
# 15 26 34 55 63 powerball: 16


class Employee(object):

    def __init__(self, first_name=None, last_name=None, numbers=set()):
        """Class representing each employee"""
        self.first_name = first_name
        self.last_name = last_name
        self.numbers = numbers

    def __str__(self):
        """Pretty string representation"""
        reg_nums = self.numbers[0:-1]
        powerball = self.numbers[-1]
        number_string = " ".join(str(x) for x in reg_nums)
        number_string += " powerball: {}".format(powerball)
        return "{} {} {}"\
            .format(self.first_name, self.last_name, number_string)


def get_number_input(prompt, existing_numbers=[], is_powerball=False):
    """Asks a user for a number"""
    if existing_numbers:
        excludes = "excluding "
        for i in range(len(existing_numbers)):
            # some formatting stuff this is kind of ugly.
            if i == len(existing_numbers) - 1 and len(existing_numbers) > 1:
                excludes += "and " + str(existing_numbers[i])
            elif len(existing_numbers) == 1:
                excludes += str(existing_numbers[i])
            elif len(existing_numbers) == 2:
                excludes += str(existing_numbers[i]) + " "
            else:
                excludes += str(existing_numbers[i]) + ", "

        prompt = "{} {}):".format(prompt, excludes)
    num = int(raw_input(prompt))
    while num in existing_numbers:
        print "Already chose that number, please choose again"
        num = int(raw_input(prompt))
    if not is_powerball:
        while num > 69 or num < 1:
            print "Number outside of bounds, please choose again"
            num = int(raw_input(prompt))
    else:
        while num > 26 or num < 1:
            print "Powerball number outside of bounds, please choose again"
            num = int(raw_input(prompt))

    return num


def create_employee_from_user_input():
    """Get input from a user and create an employee"""
    fname = raw_input("Enter your first name: ")
    lname = raw_input("Enter your last name: ")

    numbers = []
    numbers.append(get_number_input("select 1st # (1 thru 69): "))
    numbers.append(get_number_input("select 2nd # (1 thru 69", existing_numbers=numbers))
    numbers.append(get_number_input("select 3rd # (1 thru 69", existing_numbers=numbers))
    numbers.append(get_number_input("select 4th # (1 thru 69", existing_numbers=numbers))
    numbers.append(get_number_input("select 5th # (1 thru 69", existing_numbers=numbers))
    numbers.append(get_number_input("select powerball # (1 thru 26)", is_powerball=True))

    employee = Employee(first_name=fname, last_name=lname, numbers=numbers)
    return employee


def print_powerball_winning_number(employees):
    """Get the winning powerball number

    Gets the max count of duplicates for each position in numbers
    """
    # Each entry in the list represents the positional number
    number_instances = [{}, {}, {}, {}, {}, {}]
    for e in employees:
        for i in range(len(e.numbers)):
            if e.numbers[i] not in number_instances[i]:
                number_instances[i][e.numbers[i]] = [e]
            else:
                number_instances[i][e.numbers[i]].append(e)

    # Now we have positional number of times each person chose an umber
    # grab the max for each position for the winning powerball number
    powerball_winning_number = []
    for position_dict in number_instances:
        powerball_winning_number.append(
            max(position_dict.iterkeys(), key=(lambda key: len(position_dict[key])))
        )
    reg_nums = " ".join(str(num) for num in powerball_winning_number[0:-1])
    powerball_num = powerball_winning_number[-1]
    print "Powerball winning number:\n{} powerball: {}".format(reg_nums, powerball_num)


def main():
    """Main execution loop"""
    # Shortcut for testing
    # e1 = Employee(first_name="Zunera", last_name="Irshad", numbers=[1, 2, 3, 4, 5, 6])
    # e2 = Employee(first_name="Bob", last_name="Ross", numbers=[1, 2, 3, 8, 9, 10])
    # e3 = Employee(first_name="Kim", last_name="Lee", numbers=[1, 5, 2, 6, 10, 9])
    # e4 = Employee(first_name="Matt", last_name="Damon", numbers=[5, 6, 7, 8, 9, 10])
    # e5 = Employee(first_name="Ben", last_name="Affleck", numbers=[10, 20, 30, 50, 4, 25])
    # e6 = Employee(first_name="Taylor", last_name="Swift", numbers=[1, 2, 3, 4, 5, 6])
    # all_employees = [e1, e2, e3, e4, e5, e6]

    # Create employees from user input
    all_employees = []
    num_employees = int(raw_input("Enter # of employees: "))
    i = 0
    while i < num_employees:
        #print num_employees
        #print i
        all_employees.append(create_employee_from_user_input())
        i += 1
    # Print everyone's numbers
    for e in all_employees:
        print e

    # Print the winning number
    print_powerball_winning_number(all_employees)

if __name__ == '__main__':
    main()



