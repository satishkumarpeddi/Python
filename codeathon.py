class Codeathon:
    def __init__(self,year,coordinator,university):
        self.year=year
        self.coordinator=coordinator
        self.university=university
    def detail(self):
        return f"Detail Of Codeathon:\nYear ==> {self.year}\nCoordinator ==> {self.coordinator}\nUniversity ==> {self.university}\n"
class Champion(Codeathon):
    def detail(self):
         return f"Detail Of Codeathon:\nYear ==> {self.year}\nCoordinator ==> {self.coordinator}\nUniversity ==> {self.university}\n"
year = int(input("Enter year : "))
coordinator = input("Enter name of the coordinator : ")
university = input("Enter name of the university : ")
# codeathon = Codeathon(year,coordinator,university)
champion = Champion(year,coordinator,university)
# print(codeathon.detail())
print(champion.detail())