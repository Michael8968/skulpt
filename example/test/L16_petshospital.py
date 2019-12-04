pet={   'dog':{ 'name':"二花",
                'breed':'哈士奇',
                'age':3,
                'city':'上海',
                '病因':'不吃饭'
             },
        'cat':{ 'name':"小白",
                'breed':'中华田园猫',
                'age':5,
                'city':'哈尔滨',
                '病因':'发烧',
             },
        'fish':{ 'name':'奥莉',
                 'breed':'小丑鱼',
                 'age':'3个月',
                 'city':'北京',
                 'sex':'Female',
                 '病因':'没毛病',
              },
         'bird':{ 'name':'小翠',
                  'breed':'虎皮鹦鹉',
                  'age':'1岁',
                  'city':'南京',
                  'sex':'Male',
                  '病因':"不吃饭"
              }

}

'''
print(pet.values())
for value in pet.values():
	print(value['病因'])

for key in pet:
	print(pet[key]['病因'])
'''
