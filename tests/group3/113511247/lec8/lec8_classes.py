from math import gcd
#################
## EXAMPLE: simple Coordinate class
#################
class Coordinate(object):
    # "object" is the base class for all classes in Python 2.x
    """ A coordinate made up of an x and y value """
    def __init__(self, x, y):
        # initializes the x and y values
        # "self" refers to the instance of the class (Coordinate)
        # in this case, self contains variables x and y
        """ Sets the x and y values """
        self.x = x
        self.y = y
    def __str__(self):
        """ Returns a string representation of self """
        return "<" + str(self.x) + "," + str(self.y) + ">"
    def distance(self, other):
        """ Returns the euclidean distance between two points """
        x_diff_sq = (self.x-other.x)**2
        y_diff_sq = (self.y-other.y)**2
        return (x_diff_sq + y_diff_sq)**0.5


# c = Coordinate(3,4)
# origin = Coordinate(0,0)
# print(c.x, origin.x)
# print(c.distance(origin))
# print(Coordinate.distance(c, origin))
# print(origin.distance(c))
# print(c)


#################
## EXAMPLE: simple class to represent fractions
## Try adding more built-in operations like multiply, divide
### Try adding a reduce method to reduce the fraction (use gcd)
#################
class Fraction(object):
    """
    A number represented as a fraction
    """
    # use __xxx__ to avoid name clashes with built-in functions
    def __init__(self, num, denom):
        # demoninator (除數, 分母)
        """ num and denom are integers """
        assert type(num) == int and type(denom) == int, "ints not used"
        assert denom != 0, "denominator can't be zero"
        self.num = num
        self.denom = denom
    def __str__(self):
        # modified by Gino at 2025.4.30
        """ Returns a string representation of self """
        x=self.num/self.denom
        if x != int(x):
            return str(self.num) + "/" + str(self.denom)
        else:
            return str(int(x))
    def __add__(self, other):
        """ Returns a new fraction representing the addition """
        top = self.num*other.denom + self.denom*other.num
        bott = self.denom*other.denom
        factor = gcd(top, bott)
        top //= factor
        bott //= factor
        return Fraction(top, bott)
    def __sub__(self, other):
        """ Returns a new fraction representing the subtraction """
        top = self.num*other.denom - self.denom*other.num
        bott = self.denom*other.denom
        factor = gcd(top, bott)
        top //= factor
        bott //= factor
        return Fraction(top, bott)
    def __float__(self):
        """ Returns a float value of the fraction """
        return self.num/self.denom
    def inverse(self):
        """ Returns a new fraction representing 1/self """
        return Fraction(self.denom, self.num)
##////////below are written by Gino at 2025.4.30////////////////////##
    def __multuply__(self, other):
        """ Returns a new fraction representing the multiplication """
        top = self.num*other.num
        bott = self.denom*other.denom
        factor = gcd(top, bott)
        top //= factor
        bott //= factor
        return Fraction(top, bott)
    def __divide__(self, other):
        """ Returns a new fraction representing the division """
        top = self.num*other.denom
        bott = self.denom*other.num
        factor = gcd(top, bott)
        top //= factor
        bott //= factor
        return Fraction(top, bott)

a = Fraction(1,4)
b = Fraction(3,4)
c = a + b
# "+" means calling __add__ method, c is a Fraction object
print(c) # __str__ method is called
print(float(c))
print(Fraction.__float__(c))
print(float(b.inverse()))
##c = Fraction(3.14, 2.7) # assertion error
##print a*b # error, did not define how to multiply two Fraction objects


##############
## EXAMPLE: a set of integers as class
##############
class intSet(object):
    """
    An intSet is a set of integers
    The value is represented by a list of ints, self.vals
    Each int in the set occurs in self.vals exactly once
    """
    def __init__(self):
        """ Create an empty set of integers """
        self.vals = []

    def insert(self, e):
        """ Assumes e is an integer and inserts e into self """
        if not e in self.vals:
            self.vals.append(e)

    def membercheck(self, e):
        """ Assumes e is an integer
        Returns True if e is in self, and False otherwise """
        # "in" is a built-in operator that checks membership
        return e in self.vals

    def remove(self, e):
        """ Assumes e is an integer and removes e from self
        Raises ValueError if e is not in self """
        try:
            self.vals.remove(e)
        except:
            raise ValueError(str(e) + ' not found')

    def __str__(self):
        """ Returns a string representation of self """
        self.vals.sort() # change the list itself
        return '{' + ','.join([str(e) for e in self.vals]) + '}'
        #results be like {1,2,3,10}



s = intSet()
print(s)
s.insert(3)
s.insert(4)
s.insert(3)
print(s)
s.membercheck(3)
s.membercheck(5)
s.insert(6)
print(s)
#s.remove(3)  # leads to an error
print(s)
s.remove(3)