class User:
    def __init__(self, lst, dict_n):
        self.lst = lst

        self.full_name = self.lst[dict_n['Name']]
        self.name = self.lst[dict_n['Given Name']]
        self.middle_name = self.lst[dict_n['Additional Name']]
        self.surname = self.lst[dict_n['Family Name']]
        self.nickname = self.lst[dict_n['Nickname']]

        self.birthday = self.lst[dict_n['Birthday']]

        self.groups = self.lst[dict_n['Group Membership']].split(' ::: ')[:-1]

        self.phones = []

        i = 0
        while True:
            i += 1
            q = dict_n.get(f"Phone {i} - Value")
            if q:
                phone = self.lst[q]
                if phone:
                    self.phones.append(phone)
                else:
                    break
            else:
                break
        self.websites = []

        i = 0
        while True:
            i += 1
            q = dict_n.get(f"Website {i} - Value")
            if q:
                website = self.lst[q]
                if website:
                    self.websites.append('https://' + website if 'https' not in website else website)
                else:
                    break
            else:
                break

    def get_full_name(self):
        return self.full_name

    def get_birthday(self):
        return self.birthday

    def get_groups(self):
        return self.groups

    def get_phones(self):
        return self.phones

    def get_websites(self):
        return self.websites

    def __str__(self):
        return f'User[Name: {self.full_name}, Birthday: {self.birthday}, Groups: {self.groups}, Phones: {self.phones}, Websites: {self.websites}]'

    def __repr__(self):
        return self.__str__()

