import json

data = {
    "Emp1":{
        "Name":input("Enter your name: "),
        "Age":int(input("Enter your age: ")),
        "Employed":(input("Enter you are employed or not: ")),
        "Salary":input("Enter your salary expetation: ")
        
    },
}

main_data = open("/home/balaji/Documents/output of json/input server data.json", "w")
json.dump(data, main_data, indent=6)
main_data.close()