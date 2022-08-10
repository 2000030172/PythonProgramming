from pymongo import MongoClient
try:
    client = MongoClient('localhost:27017')
    db = client.pfsd
    collection=db.Skill12
    print('Database Connected Successfully......!')
except:
    print('Couldn\'t connect to MongoDB')
def main():
    while(True):
        print('*-*-* Web Applications and Database in Supermarket *-*-*')
        print('1. Insertion')
        print('2. Display')
        print('3. Update')
        print('4. Delete')
        choice = int(input('Enter your Choice : '))
        if choice == 1:
            try:
                web = [{
                    "Product_Id": "1",
                    "Name": "Fruits",
                    "Country": "Italy"
                },
                {
                    "Product_Id": "2",
                    "Name": "Species",
                    "Country": "India"
                },
                {
                    "Product_Id": "3",
                    "Name": "Clothes",
                    "Country": "US"
                },
                {
                    "Product_Id": "4",
                    "Name": "Makeup items",
                    "Country": "UK"
                },
                {
                    "Product_Id": "5",
                    "Name": "Electronics",
                    "Country": "Japan"
                }]
                collection.insert_many(web)
                print('Inserted Sucessfully....!')
            except Exception as e:
                print (e)
        elif choice==2:
            try:
                cursor=collection.find()
                for val in cursor:
                    print(val)
            except Exception as e:
                print (e)
        elif choice==3:
            try:
                collection.update_one(
                    {
                        "Product_Id": "4",
                    },
                    {
                        "$set":
                            {
                                "Name": "Energy Drinks",
                            }
                    }
                )
                print('Updated Successfully...!')
            except Exception as e:
                print (e)
        elif choice==4:
            try:
                collection.delete_one({"Name": "Clothes"})
                print('Deleted Successfully...!')
            except Exception as e:
                print (e)
        else:
            print('Improper Choice')
            exit()
main()