f1file = open('./Followers.txt', 'r', encoding="utf-8")
F1file = open('./Following.txt', 'r', encoding="utf-8")
f2open = open('./FollowersFormatted.txt', 'w', encoding="utf-8")
F2open = open('./FollowingFormatted.txt', 'w', encoding="utf-8")
for line in f1file:
    if '\'s profile picture' in line:
        lineFormatted = line.replace('\'s profile picture', '')
        f2open.write(lineFormatted)
for line in F1file:
    if '\'s profile picture' in line:
        lineFormatted = line.replace('\'s profile picture', '')
        F2open.write(lineFormatted)
f2open.close()
F2open.close()

f2file = open('./FollowersFormatted.txt', 'r', encoding="utf-8")
F2file = open('./FollowingFormatted.txt', 'r', encoding="utf-8")
EXfile = open('./Exclusions.txt', 'r', encoding="utf-8")
followers = []
exclusions = []
for line in EXfile:
    exclusions.append(line)
for line in f2file:
    followers.append(line)
for line in F2file:
    if line not in followers and line not in exclusions:
        print(line)