class Employee():
    def register_hour(self, hours):
        print('Hours registered...')
    
    def show_tasks(self):
        print('Did a lot of things...')

class Alura(Employee):
    def show_tasks(self):
        print('Did a lot of thing in Alura')
    
    def get_questions_without_answers(self):
        print('Showing questions with no answers in the Forum')

class Caelum(Employee):
    def show_tasks(self):
        print('Did a lot of thins in Caelum')
    
    def get_month_course(self, month=None):
        print(f'Showing courses - {month}' if month else 'Showing this month courses')
    
class Junior(Alura):
    pass

class Pleno(Alura, Caelum):
    pass

jose = Junior()
jose.get_questions_without_answers()

luan = Pleno()
luan.get_questions_without_answers()
luan.get_month_course()
luan.show_tasks()