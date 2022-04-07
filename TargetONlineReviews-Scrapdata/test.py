abc = ['Cushioned', '5', 'Would recommend', 'Starryktty ', '2021-10-09 10:09:33.731690', 'Hey bullseye reviewer',
       'These socks are very soft and feel nice on my feet. The little picture on them is so cute and they are at a nice height. They are comfortable and aren’t too tight. They wash well and are thin enough to be comfortable in a sneaker yet thick enough to keep your feet warm.']
for i in abc:
    if 'Hey bullseye reviewer' in i:
        abc.remove('Hey bullseye reviewer')
print(abc)
