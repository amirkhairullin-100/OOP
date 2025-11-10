class Person:
    def __init__(self, name, middle_name, surname, phones):
        self.name = name
        self.middle_name = middle_name
        self.surname = surname
        self.phones = phones
    def get_phone(self):
        return self.phones.get('private', None)
    def get_name(self):
        return f"{self.surname} {self.name} {self.middle_name}"
    def get_work_phone(self):
        return self.phones.get('work', None)
    def get_sms_text(self):
        return f"Уважаемый {self.name} {self.middle_name}! Примите участие в нашем беспроигрышном конкурсе для физических лиц"
class Company:
    def __init__(self, name, company_type, phones, *employees):
        self.name = name
        self.company_type = company_type
        self.phones = phones
        self.employees = employees
    def get_phone(self):
        if 'contact' in self.phones:
            return self.phones['contact']
        for emp in self.employees:
            if emp.get_work_phone() is not None:
                return emp.get_work_phone()
        return None
    def get_name(self):
        return self.name
    def get_sms_text(self):
        return f"Для компании {self.name} есть супер предложение! Примите участие в нашем беспроигрышном конкурсе для {self.company_type}"
def send_sms(*recipients):
    for rec in recipients:
        phone = rec.get_phone()
        if phone is not None:
            text = rec.get_sms_text()
            print(f"Отправлено СМС на номер {phone} с текстом: {text}")
        else:
            name = rec.get_name()
            print(f"Не удалось отправить сообщение абоненту: {name}")
person1 = Person("Ivan", "Ivanovich", "Ivanov", {"private": 123, "work": 456})
person2 = Person("Ivan", "Petrovich", "Petrov", {"private": 789})
person3 = Person("Ivan", "Petrovich", "Sidorov", {"work": 789})
person4 = Person("John", "Unknown", "Doe", {})
company1 = Company("Bell", "ООО", {"contact": 111}, person3, person4)
company2 = Company("Cell", "АО", {"non_contact": 222}, person2, person3)
company3 = Company("Dell", "Ltd", {"non_contact": 333}, person2, person4)
send_sms(person1, person2, person3, person4, company1, company2, company3)
print()
person5 = Person("Степан", "Петрович", "Джобсов", {"private": 555})
person6 = Person("Боря", "Иванович", "Гейтсов", {"private": 777, "work": 888})
person7 = Person("Семен", "Робертович", "Возняцкий", {"work": 789})
person8 = Person("Леонид", "Арсенович", "Торвальдсон", {})
company4 = Company("Яблочный комбинат", "ООО", {"contact": 111}, person1, person3)
company5 = Company("ПластОкно", "АО", {"non_contact": 222}, person2)
company6 = Company("Пингвинья ферма", "Ltd", {"non_contact": 333}, person4)
send_sms(person5, person6, person7, person8, company4, company5, company6)