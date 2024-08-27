from CustomException import InvalidAgeException


class ElectionCommission:

    def checkEligibility(self, age):
        if age < 18:
            raise InvalidAgeException
        else:
            print("You are eligible to vote")


ec = ElectionCommission()
try:
    ec.checkEligibility(12)
except InvalidAgeException:
    print("You are not eligible to vote")