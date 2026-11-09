facebook = True
twitter = False
instagram = True

count = 0
if facebook:
    count += 1
if twitter:
    count += 1
if instagram:
    count += 1

if count >= 2:
    print('You are a good influencer!')
