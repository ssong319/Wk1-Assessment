# PART ONE

# 1. We have some code which is meant to calculate an item cost
#    by adding tax. Tax is normally 5% but it's higher in
#    California (7%).

#    Turn this into a function. Your function will pass in
#    the default tax amount (5%), a state abbreviation, and the
#    cost amount as parameters.

#    If the state is California, apply a 7% tax within the function.
#    Your function should return the total cost of the item,
#    including tax.

#    If the user does not provide a tax rate it should default to 5%
def item_cost(cost, state, tax=.05):
    """
    Calculates item cost by adding tax

    This function takes in a cost, state, and tax with a default tax rate of 5%
    and calculates the cost of the item with tax included. If the state is CA,
    tax is set to 7%
    """
    if state == 'CA':
        tax = .07
    total = cost + cost * tax
    return total



#####################################################################
# PART TWO

# 1. (a) Write a function, `is_berry()`, which takes a fruit name as a string
#        and returns a boolean if the fruit is a "strawberry", "cherry", or 
#        "blackberry".
def is_berry(fruit):
    """returns true if fruit is a berry

    This function takes a string as a parameter and returns a boolean indicating
    whether the string is one of the three berries specified
    """

    if fruit == 'strawberry' or fruit == 'cherry' or fruit == 'blackberry':
        return True
    else:
        return False

#    (b) Write another function, shipping_cost(), which calculates shipping cost
#        by taking a fruit name as a string, calling the `is_berry()` function 
#        within the `shipping_cost()` function and returns `0` if ``is_berry()
#        == True``, and `5` if ``is_berry() == False``.

def shipping_cost(fruit):
    """calculates shipping cost based on whether the fruit is a berry

    This function takes a fruit name as a string and calls the is_berry function
    using the fruit name as the parameter. It returns 0 or 5 depending on the
    result of calling is_berry
    """
    if is_berry(fruit) == True:
        return 0
    else:
        return 5


# 2. (a) Write a function, `is_hometown()`, which takes a town name as a string
#        and evaluates to `True` if it is your hometown, and `False` otherwise.

def is_hometown(town):
    """Takes a town name as a string and returns a boolean indicating whether
    the town is my hometown
    """
    if town == 'torrance':
        return True
    else:
        return False
#
#    (b) Write a function, `full_name()`, which takes a first and last name as
#        arguments as strings and returns the concatenation of the two names in
#        one string.
def full_name(first, last):
    """Takes a first and last name and returns the concatenation of the first
    and last name in one string
    """
    return first + " " + last

#    (c) Write a function, `hometown_greeting()`, which takes a home town, a
#        first name, and a last name as strings as arguments, calls both
#        `is_hometown()` and `full_name()` and prints "Hi, 'full name here',
#        we're from the same place!", or "Hi 'full name here', where are you
#        from?" depending on what `is_hometown()` evaluates to.
def hometown_greeting(first, last, town):
    if is_hometown(town) == True:
        print "Hi, {}, we're from the same place!".format(full_name(first, last))
    else:
        print "Hi {}, where are you from?".format(full_name(first, last))

#####################################################################

# PART THREE

# 1. Write a function ``increment()`` with a nested inner function, ``add()``
#    inside of it. The outer function should take ``x``, an integer which
#    defaults to 1. The inner function should take ``y`` and add ``x`` and ``y`` together.
def increment(x=1):
    """returns a function that adds x and y with default value of x at 1

    Increment returns an inner function 'add' that takes in parameter y and returns
    the result of calling x and y
    """
    def add(y):
        return x + y
    return add
# 2. Call the function ``increment()`` with x = 5. Assign what is returned to a variable name, addfive. Call
#    addfive with y = 5. Call again with y = 20.
addfive = increment(5)
addfive(5)
addfive(20)
# 3. Make a function that takes in a number and a list of numbers. It should append
#    the number to the list of numbers and return the list.
def add_to_list(num, list_of_nums):
    """appends a number to a list and returns the list
    """
    list_of_nums.append(num)
    return list_of_nums



#####################################################################