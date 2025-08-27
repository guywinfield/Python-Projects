from datetime import date
import inflect

def main():
    user_date = input("Date of Birth ('YYYY-MM-DD'): ")
    calc = Time(user_date)
    print(f"{calc.get_minutes_in_words()} minutes")


class Time:
    def __init__(self, birth_date):

        if len(birth_date.split("-")) != 3 and len(birth_date) != 10:
            sys.exit("Entered invalid date format")
        else:
            self.birth = date.fromisoformat(birth_date)
        self.today = date.today()

    def get_minutes(self):
        date_diff = self.today - self.birth
        return date_diff.days * 24 * 60

    def get_minutes_in_words(self):
        p = inflect.engine()
        words = p.number_to_words(self.get_minutes(), andword="")
        return words.capitalize()



if __name__ == "__main__":
    main()
