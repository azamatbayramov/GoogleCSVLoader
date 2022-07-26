class User:
    def __init__(self, lst: list[str], dict_n: dict):
        self.lst = lst

        self.full_name = self.lst[dict_n['Name']]
        self.name = self.lst[dict_n['Given Name']]
        self.middle_name = self.lst[dict_n['Additional Name']]
        self.surname = self.lst[dict_n['Family Name']]
        self.nickname = self.lst[dict_n['Nickname']]

        self.birthday = self.lst[dict_n['Birthday']]

        self.groups = self.lst[dict_n['Group Membership']].split(' ::: ')[:-1]

        self.phones = []

        for i in range(1, 10 ** 10):
            index = dict_n.get(f"Phone {i} - Value")
            if not index:
                break

            phone = self.lst[index]
            if not phone:
                break

            self.phones.append(phone)

        self.websites = []

        for i in range(1, 10 ** 10):
            index = dict_n.get(f"Website {i} - Value")
            if not index:
                break

            website = self.lst[index]
            if not website:
                break

            self.websites.append('https://' + website if 'https' not in website else website)

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

