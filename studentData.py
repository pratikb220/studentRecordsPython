import json

class StudentRecords:
    def __init__(self):
        self.records = []

    def add_student(self, name, address, city, country, pin_code, sat_score):
        result = 'Pass' if sat_score > 30 else 'Fail'
        student = {
            'Name': name,
            'Address': address,
            'City': city,
            'Country': country,
            'Pin Code': pin_code,
            'SAT Score': sat_score,
            'Result': result
        }
        self.records.append(student)
        self.save_records()

    def show_all(self):
        return json.dumps(self.records, indent=4)

    def find_rank(self, name):
        sorted_records = sorted(self.records, key=lambda x: x['SAT Score'], reverse=True)
        for i, student in enumerate(sorted_records, start=1):
            if student['Name'] == name:
                return i
        return None

    def update_score(self, name, new_score):
        for student in self.records:
            if student['Name'] == name:
                student['SAT Score'] = new_score
                student['Result'] = 'Pass' if new_score > 30 else 'Fail'
                self.save_records()
                return True
        return False

    def delete_student(self, name):
        for student in self.records:
            if student['Name'] == name:
                self.records.remove(student)
                self.save_records()
                return True
        return False

    def average_score(self):
        if not self.records:
            return 0
        total = sum(student['SAT Score'] for student in self.records)
        return total / len(self.records)

    def filter_by_result(self, result):
        filtered = [student for student in self.records if student['Result'] == result]
        return json.dumps(filtered, indent=4)

    def save_records(self):
        with open('student_data.json', 'w') as f:
            json.dump(self.records, f, indent=4)

def main_menu():
    system = StudentRecords()

    while True:
        print("\nMenu:")
        print("1. Add Student")
        print("2. Show All Records")
        print("3. Find Student Rank")
        print("4. Update SAT Score")
        print("5. Delete Student Record")
        print("6. Calculate Average SAT Score")
        print("7. Filter by Result (Pass/Fail)")
        print("8. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            name = input("Name: ")
            address = input("Address: ")
            city = input("City: ")
            country = input("Country: ")
            pin_code = input("Pin Code: ")
            sat_score = int(input("SAT Score: "))
            system.add_student(name, address, city, country, pin_code, sat_score)
            print("Student added.")

        elif choice == '2':
            print("All Records:")
            print(system.show_all())

        elif choice == '3':
            name = input("Enter Name: ")
            rank = system.find_rank(name)
            if rank:
                print(f"{name} is ranked {rank}")
            else:
                print("Student not found.")

        elif choice == '4':
            name = input("Enter Name: ")
            new_score = int(input("Enter New SAT Score: "))
            if system.update_score(name, new_score):
                print("SAT score updated.")
            else:
                print("Student not found.")

        elif choice == '5':
            name = input("Enter Name: ")
            if system.delete_student(name):
                print("Student record deleted.")
            else:
                print("Student not found.")

        elif choice == '6':
            print(f"Average SAT Score: {system.average_score()}")

        elif choice == '7':
            result = input("Filter by (Pass/Fail): ")
            print(f"Students who {result}:")
            print(system.filter_by_result(result))

        elif choice == '8':
            break

        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main_menu()
