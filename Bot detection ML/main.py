# Bot Detection - Python Data Structures

# LIST
accounts = ["user1", "user2", "user3", "user4"]

print("LIST")
print(accounts)

accounts.append("user5")
accounts.remove("user2")

print("After changes:", accounts)
print("First account:", accounts[0])


# TUPLE
account = ("user1", 500, 300, 5)

print("\nTUPLE")
print(account)

print("Username:", account[0])
print("Followers:", account[1])

username, followers, following, posts_per_day = account

print("Username:", username)
print("Followers:", followers)
print("Following:", following)
print("Posts per day:", posts_per_day)


# DICTIONARY
user = {
    "username": "user1",
    "followers": 500,
    "following": 300,
    "posts_per_day": 5
}

print("\nDICTIONARY")
print(user)

print("Username:", user["username"])
print("Followers:", user["followers"])

user["likes_per_day"] = 100
user["followers"] = 600

print("After changes:", user)

del user["likes_per_day"]

print("After deletion:", user)

print("Keys:", user.keys())
print("Values:", user.values())
print("Items:", user.items())


# SET
followers = {"user1", "user2", "user3", "user4"}
following = {"user3", "user4", "user5", "user6"}

print("\nSET")
print("Followers:", followers)
print("Following:", following)

print("Union:", followers | following)
print("Intersection:", followers & following)
print("Difference:", following - followers)
print("Symmetric Difference:", followers ^ following)

followers.add("user7")
followers.remove("user2")

print("After changes:", followers)
