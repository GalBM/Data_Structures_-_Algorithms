class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name

def is_user_in_group(user=None, group=None):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """
    """
    The recursive function check if the  user exists in the group
    if yes- it return True , if not it call the function to check the sub-group
    until it check every group and sub_group
    """
    # if input is missing
    if user==None or group==None:
        return"please insert appropriate input"
    users_list=group.get_users()
    for key in users_list:
        # the break step- if the user equal to the input
        if key==user:
            return True
    # the recursive section- if there are sub-group, the function repeat with the sub group
    for sub_group in group.get_groups():
        return is_user_in_group(user,sub_group)
    return False



##test1- regular case
parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")

sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)

child.add_group(sub_child)
parent.add_group(child)
print(is_user_in_group("sub_child_user", parent))
#return True, the user exists in the group

## Test2 - regular case- the user doensnt exist in the group
print(is_user_in_group("sub_child_users", parent))
#return False, the user doensnt exist in the group

##test3- empty group
empty_group=Group("empty")
print(is_user_in_group("sub_child_user",empty_group))
## return False

##test4- null input
print(is_user_in_group("sub_child_user"))
## return please insert appropriate input



