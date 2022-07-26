# GoogleContactsCSVLoader
Module for loading information from Google Contacts CSV into user-friendly Python class

## How to use

### 1. Export Google Contacts CSV file

![image](https://user-images.githubusercontent.com/58120335/180963638-bbebf5f0-5675-4807-b136-06689be7263b.png)

![image](https://user-images.githubusercontent.com/58120335/180963981-75901b64-3b4c-4aa4-8d85-0cc29ee2f98b.png)

### 2. Call the get_contacts(filename) function
    from google_contacts_csv_loader import get_contacts
    
    contacts = get_contacts("C:/Users/USERNAME/Downloads/contacts.csv")
    
### 3. Done! You have a list of Contacts. You can use it.

    ...
    contacts_without_birthday = [c for c in contacts if not c.get_birthday()]
    
    teachers_with_phones = [c for c in contacts if "Teacher" in c.get_groups() and c.get_phones()]
    
    friends_without_websites = [c for c in contacts if "Friend" in c.groups() and not c.get_websites()]
    
