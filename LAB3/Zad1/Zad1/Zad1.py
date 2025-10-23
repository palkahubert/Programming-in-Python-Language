from dataclasses import dataclass, asdict
import json

@dataclass
class Person:
    name: str
    surname: str
    address: str
    post_code: str
    pesel: str

    def save_to_file(self, file: str):
        with open(file, 'w', encoding='utf-8') as f:
            json.dump(asdict(self), f, ensure_ascii=False, indent=4)
    
    @staticmethod
    def load_from_file(file: str):
        with open(file, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return Person(**data)

if __name__ == "__main__":
    person = Person("Jan", "Kowalski", "Krakow, ul. Dluga 25", "31-112", "90000000000")
    person.save_to_file("person.json")

    new_person = Person.load_from_file("person.json")
    print(new_person);
