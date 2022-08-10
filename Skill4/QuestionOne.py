from pymongo import MongoClient
def main():
    while (True):
        print('*-*-* CURD Operations in MongoDB *-*-*')
        print('1. Insertion')
        print('2. Deletion')
        print('3. Display')
        print('4. Update')
        choice = int(input('Enter your Choice'))
        if choice == 1:
            try:
                name = input('Enter Name of the Student : ')
                Roll_number = int(input('Enter Roll Number of The Student : '))
                Branch = input('Enter branch of the Student : ')
                db.Skill.insert_one(
                    {
                        "_id": Roll_number,
                        "name": name,
                        "Branch": Branch
                    }
                )
                print('Inserted Data Successfully..........!')
            except Exception as e:
                print(e)
        elif choice == 2:
            try:
                roll_num = int(input('Enter Roll Number to delete : '))
                db.Skill.delete_one({"_id": roll_num})
                print('Deletion Successfully......!')
            except Exception as e:
                print(e)
        elif choice == 3:
            try:
                print('Data Available ')
                pfsd = db.Skill.find()
                for val in pfsd:
                    print(val)
            except Exception as e:
                print(e)
        elif choice == 4:
            try:
                num = input('Enter Roll Number to update : ')
                name = input('Enter the name to update : ')
                db.Skill.update_one({
                    "_id": num
                },
                    {
                        "$set": {
                            "name": name
                        }
                    })
                print('Updated Successfully')
            except Exception as e:
                print(e)
        else:
            print("Improper selection")
            exit()


client = MongoClient('localhost:27017')
db = client.pfsd
main()
