if True:  # 4 spaces no need of {}
    print("ZAIN")
    #single line comment
    '''
    multi
    line
    comment
    '''
    name = "ZAIN"  #string
    age = 17  #integer
    # python automatic consider variable is string on integer
    print(name)  # don't use double column to print variable
    x = 5
    y = 9
    print(x + y)
    # to write more then 1 statement in 1 line use semicolumn
    total = 4 + 5 + 7 + \
            8 + 9
    print(total)  # to break line mean to write data in multiple line use \
    circle = (
            9 + 9 +
            9 + 9
    )
    print(circle)
    square = [
        9, 9
    ]
    print(square)
    '''
     if you use () or [] the date written inside doesn't need
     any backslash it will automatically consider it one part
    '''


    # to make function use keyword def
    def function():
        print("Hello!")


    function()
    # to print function just write name of function end with()
    single_line = "This is single line string"
    multi_line = '''This
        is multi 
        line string'''
    # for single line string use '', ""
    # for multi line string start and end as multi line comment '''''', '''''' ''''''
    print(single_line)
    print(multi_line)
    h = 9
    j = 10
    print(h)
    print(j)
    #space doesn't matter but use one space for better vision
    # also avoid extra spacing and avoid inconsistency
    import math

    print(math.sqrt(4))
    # to import a library use import function and function name
    # then you can use library in print function as normal
    '''
    reserved words cannot be used as variable
    if else for while def true false
    '''
    print("This is keyword example")
    # variables are in python are containers that store data in it
    name = "Ahmed"  # String
    ages = 25  # Integer
    height = 6.5  # Float

    # python automatically detect the data type of variable

    print(name, ages, height)

    '''
    variable can contain letter number and underscore
    cannot start with number
    variable ara case sensitive mean A is different from a
    cannot use python keywords as variable
    like def
    '''

    # Data types in Python

    '''
    DATA TYPE                DESCRIPTION                            EXAMPLE
    
    int             whole number+,- without decimal(.)            age = 30
    float           number with decimal points                    price = 19.99
    str             sequence of character                         name = "ZAIN"
    bool            Boolean values: True or False                 is_active = True
    list            ordered and changeable                        fruits = ["Apple","Banana"]
    tuple           ordered but cannot changeable                 coordinates = (10,20)
    dict            key-value pairs                               person = {"name":"ZAIN","age":"17"}
    set             unordered form of unique data                 unique_nums = {1,2,3}
    '''

    # although python understand data type itself
    # but it necessary to have knowledge
    # so in complex situations we can use it