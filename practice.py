user_name = str(input("enter user name:"))
user_pass = int(input("enter user pass:"))
if(user_name =="omkar" and user_pass == 1234):
    print("login succefull")
else:
    print("login failed")
cand_age = int(input("cand age:"))
if(cand_age >= 18):
    print("approved")
else:
    print("not approved")