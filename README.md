# ReferrerMaintanence
This is a python script which will maintain the user and referrer relationship along with the count of number of user's referred by each user.

# Steps to run the project
1. create a blank data.json file in the root directory.
2. run the maintaner.py script file.

# There are two methods:
1. addNewData(name,referred_by)
  * this will add a new user to the system

2. showAllData()
  * this will show all the data present in the system.


# Logic:
1. currently all the data is saved and retrieved from a file for persistance.
1. If a user A is entered and he is not refereed by anyone, he becomes the parent with no parent, hence his referred_by field will be None and referred_count will be 0.
1. Now if a user B enters who is referred by A, then his referred_by field will contain A and count 0, and for A the count will become 1
1. subsequently C enters who is now referred by B, then C's referred by becomes B and the count of both A and B increases by one.
