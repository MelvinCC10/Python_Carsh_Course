import TryItYourSelf_9_8 as userObj

print('\n\n\n\n')
admin1 = userObj.Admin('john','deer',30)
admin1.describe_user()
print('\n')

admin1.set_user_name('Reven10')
print('\n')
admin1.describe_user()
admin1.privileges.show_privileges()
