def convert(_2d : list):
    r = []
    for arr in _2d:
        for i in arr:
            r.append(i)
    return r

print(convert([[
    1,2,3
    ],
    [
        4,5,6
    ]
               ]))