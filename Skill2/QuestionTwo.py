class Patient(object):
    def __init__(self, name):
        print(name, 'is Recovered from his health issue.')
class Doctor(Patient):
    def __init__(self):
        print('Doctor Class contains doctor qualifications')
        super().__init__('Patient')
class Medicine(Doctor):
    def __init__(self):
        print('Medicine Class contains different types of medicines')
        super().__init__()
m=Medicine()