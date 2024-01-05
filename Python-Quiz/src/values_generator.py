import numpy
import random
import pandas
import string as string_functions 


class ValuesGenerator:
    
    def __init__(self):
            
        self.reserved_words = ['False','def','if','raise','None','del','import','return','True','elif','in','try','and','else','is','while',
                                    'as','except','lambda','with','assert','finally','nonlocal','sum', 'sorted', 'any', 'all', 'max', 'min',
                                    'yield','break','for','not','class','form','or','continue','global','pass', 'zip', 'enumerate']
    #### END INIT ####

    def choose_length(self):
        '''for choosing the length of tuple, set, list and dict values'''
        return int(numpy.random.normal(3, .667))


    def simple_value(self, types=[str,int,float,tuple]):  
        '''return a random value of one of the types in `types`
            this function calls the type-creator functions below to generate a value based on the rules set in each of those functions
        accepts:
            types (list[type]) --> the types of values you want to randomly choose from'''
        allowed_types = [bool,str,int,float,tuple,set,list,dict]
        generators = [self.make_bool, self.make_str, self.make_int, self.make_float, self.make_tuple, self.simple_set, self.simple_list, self.simple_dict]
        mapping = dict(zip(allowed_types,generators))
        if 'all' in [types]:
            #print('adding all types')
            kind = random.choice(allowed_types)
        else:
            # use the argument passed to function to select a type
            kind = random.choice([x for x in types if x in allowed_types])
        # call the function based on the mapping
        value = mapping[kind]()
        return value


    def make_bool(self):
        '''return a random bool value'''
        return random.choice([True, False])
        

    def make_str(self,
                 max_length:int=8,
                 force_length:bool=False,
                 add_symbols:bool=False):
        """return a str value with certain constraints
            arguments:
                max_length (int) --> if force_length = False, the returned string will be of a random length between 1 and this value
                force_length (bool) --> if true, the returned string will be equal to the max value
                add_symbols (bool) --> if True, the string can include symbols. otherwise, the string will be alphanumeric characters only

            The function intentionally has a chance of returning reserved keywords (as strings). This is to 'trick' the user into recognizing string values (as opposed to type/function names, which do not have quotes)"""
        # determine output str length
        if force_length != False:
            calculated_length = force_length
        else:
            calculated_length = random.randrange(1,max_length)
        # determine valid characters for the str
        characters = [x for x in string_functions.ascii_lowercase]
        if add_symbols == True:
            characters += [x for x in """<>?/"':;|\}]{[+=_-*%)($%^&#@!~`"""] 
        # additionally include a random assortment of reserved words (trick questions)
        reserved_words = self.reserved_words
        # generate a random list of strings from the accepted values + reserved words
        random_words = [''.join([random.choice(characters) for i in range(calculated_length)]).capitalize() for x in range(50)] 
        wordlist = reserved_words + random_words
        # ensure that the max_length requirement is met
        if force_length==True:
            wordlist = [x for x in wordlist if len(x) == force_length]
        # final str selection
        output = random.choice(wordlist)   
        return output
    

    def make_int(self, scale=50):
        ''' return a random integer which is normally distributed around 0'''
        return int(numpy.random.normal(0,scale))


    def make_float(self, scale=50):
        '''return a random float which is composed of an integer normally distributed around 0, and a 2-digit decimal value'''
        return random.choice([round(x + y,2) for x, y in zip([float(x) for x in numpy.random.normal(0,scale,size=100)], [int(x) for x in numpy.random.random_sample(100)])])


    def make_tuple(self,
                   size:int=None,
                   types:list[type]=[str,int,float]):
        """return a tuple composed of values included in 'types' argument. This function calls 'simple_value' to generate the values inside the returned tuple
        accepts:
            size(int), default None --> the length of the tuple. If None, the length is randomly generated
            types(list[type]) --> the types of values you want to create. these must be immutable types. type verification occurs inside the `simple_values` function."""
        if not size:
            length = self.choose_length()
        else:
            length = size
        output = tuple([self.simple_value(types=types) for x in range(length)])
        return output
    

    def simple_set(self, size=None, types=[str,int,float]):
        '''returns a set of length `size`, composed of values included in `types` argument. 
        accepts:
            size(int, default None) --> the length of the set. if not chosen, the length is randomly selected from a normal distribution centering around 3
            types (list[type]) --> the types of values to be included in the set. The actual values are generated by `simple_value` function'''
        if not size:
            length = self.choose_length()
        else:
            length = size         
        output = [self.simple_value(types=types) for x in range(length)]
        # output = set(self.simple_list(length, types=types))
        output = set(output)
        return output


    def simple_list(self, size=None, types=[bool,str,int,float,tuple]):
        '''returns a list of length `size`, composed of values in `types` argument.
        accepts:
            size(int, default None) --> the length of the list. If not chosen, the length is randomly selected from a normal distribution centering around 3
            types (list[type]) --> the types of values to be included in the list. the actual values are generated by the `simple_value` function. '''
        if not size:
            length = self.choose_length()
        else:
            length = size
        output = [self.simple_value(types=types) for x in range(length)]
        #types = [type(x) for x in outputs]
        return output


    def simple_dict(self, size=None, types=[str,int,float]):
        '''returns a list of length `size`, composed of values in `types` argument.
        accepts:
            size(int, default None) --> the length of the dict. If not chosen, the length is randomly selected from a normal distribution centering around 3
            types (list[type]) --> the types of values to be included in the dict. the actual values are generated by the `simple_value` function. '''
        if not size:
            length = self.choose_length()
        else:
            length = size
        output = {x:y for (x, y) in [(self.simple_value(types=types),self.simple_value(types=types)) for x in range(length)]}
        return output
    

#####################################################################################

    ### LIST PRACTICE    
    def make_matrix(self, dims=2, height=4, width=4, types=[str,int,float,set,tuple,bool]):
        """ensures all values are unique"""
        output = []
        for nesting in range(dims): # ie 2-D matrix
            # for each row in height
            for i in range(height):
                # make a list of values of length == width
                row = [self.simple_value(types=types) for x in range(width)]
                # ensure unique values in each row
                while len(set(row)) != len(row):
                    row = [self.simple_value(types=types) for x in range(width)]
                output.append(row)
        return output


    def nested_list_indexing(self, dims=2, width=4):
        mtrx = self.make_matrix(dims=dims, width=width)
        c = pandas.DataFrame(mtrx).shape
        random_index = random.choice(range(1,c[0]*c[1]+1))
        rows = 0
        while random_index > 3:
            rows += 1
            random_index -= 4
        
        return mtrx, (rows,random_index), mtrx[rows][random_index]
    
    #### DICT PRACTICE 
    
    def keys_and_values(self, size=4):
        base = self.simple_dict(size=size)
        pair_selection = random.choice([x for x in base.keys()]) 
        return base,pair_selection,base[pair_selection]
        
        
    def keys_and_values_nested(self, outer_keys=int,rows=4, size=4):              
        if int == outer_keys:
            base = dict(enumerate([self.simple_dict(size=size) for i in range(rows)]))
        elif str == outer_keys:
            base = dict([(self.make_str(force_length=1), self.simple_dict(size=size)) for i in range(rows)])   
            
        dict_selection = random.choice([x for x in base.keys()]) 
        pair_selection = random.choice([x for x in base[dict_selection].keys()]) 
        return base, dict_selection, pair_selection, base[dict_selection][pair_selection]
        
     #####################################################################################