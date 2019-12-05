items = {
            "flint" : 0,   #打火石

            "grass" : 24,  #草
            "hay" : 0,      #干草

            "tree" : 34,   #树
            "log" : 0,      #原木

            "sapling" : 26, #树苗
            "twig" : 10,      #细枝

            "boulder" : 6,   #卵石
            "rock" : 0,       #岩石

            "pickaxe" : 0,    #镐
            "axe" : 0,        #斧头

            "firepit" : 0,    #火堆
            "tent" : 0,       #帐篷

            "torch" : 1,      #火把
        }



#rules to make new objects
craft = {
            "hay" : { "grass" : 1 },
            "twig" : { "sapling" : 1 },
            "log" : { "axe" : 1, "tree" : 1 },
            "axe" : { "twig" : 3, "flint" : 1 },
            "tent" : { "twig" : 10, "hay" : 15 },
            "firepit" : { "boulder" : 5, "log" : 3, "twig" : 1, "torch" : 1 },
            "torch" : { "flint" : 1, "grass" : 1, "twig" : 1 },
            "pickaxe" : { "flint" : 2, "twig" : 1 }
        }



while True:
    '''
    iwant=input('输入你想要合成的东西: ')
    if iwant in craft:
        print('yes, you can craft ' + iwant)

        #for i in craft[iwant]:
            #print('you need:  ' + str(craft[iwant][i])+' ' +i + ' to craft ' + iwant+" and you have " + str(items[i]))       



        for i in craft[iwant]:
            if craft[iwant][i]>items[i]:
                print('you do not have enough ' + i+' ,跳出合成')
                #break
            else:
                print('sure,you can make it because you have enough '+i + ' ，开始合成！' )

          

    else:
        print('sorry, you can not craft it')
