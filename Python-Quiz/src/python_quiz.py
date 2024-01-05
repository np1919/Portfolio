import numpy
import random
import pandas
import string as string_functions 
import pprint
from .values_generator import ValuesGenerator
import string 

class PythonQuiz(ValuesGenerator):
            
    def __init__(self):
        

        self.exit_strings = ['exit', 'exit()', 'quit', 'quit()',]

        
        
        ValuesGenerator.__init__(self) # inherit the ValuesGenerator

        self._total_score = 0
        self._total_tries = 0
        self.sos = 25 # size of samples
        
#         self.all_types = types 
        self.immutable_types = [bool, str, int, float, tuple]
        self.mutable_types = [list, dict, set]
        self.iterable_types = [str, tuple, set, list, dict] # bool, int, and float types are NOT ITERABLE --> use a pandas Series, or even a list to construct data
        
        
        self.reserved_words = ['False','def','if','raise','None','del','import','return','True','elif','in','try','and','else','is','while',
                                  'as','except','lambda','with','assert','finally','nonlocal','sum', 'sorted', 'any', 'all', 'max', 'min',
                                  'yield','break','for','not','class','form','or','continue','global','pass', 'zip', 'enumerate']

    # hidden variable, must be manually updated
        self._all_games = {'Guess the Output Type': self.guess_the_output_type,
                           'Input code to find out the type' : self.input_a_type,
                           'Simple Multiple Choice' : self.simple_multiple_choice,
                           'Guess the len()' : self.guess_the_len,
                           'Guess the index' : self.guess_the_index,
                           'Type Methods Multiple Choice' : self.type_methods_multiple_choice,
                           'Nested `list` indexing':self.guess_the_index_nested,
                           'Nested `dict` indexing practice':self.nested_dict_indexing,
                           }
        
        
        self.question_mappings = {dict:{'get': 'return the value from the dictionary using the given key. note: pass an additional argument to assign a default return value (currently `None`)',
                                    'setdefault': "create a location in the dictionary using the given key, if there wasn't one before -- if there was, return that value. note: pass an additional argument to assign a (default) value to the slot (currently `None`).",
                                    'pop': 'pop the item at the given key from the dictionary. this method both removes the item (and key) from the dictionary, while also returning the value that was stored there.',
                                    'popitem': 'pop both the key and the value from the dictionary, as a tuple. this method removes the pair from the dictionary in an immutable format, while simultaneously returning it (for potential variable assignment)',
                                    'keys': "return a `view` (not a list) of the dictionary's index -- it's keys.",
                                    'items': "return a `view` (not a list) of the dictionary's (key:value) pairs (they're returned as tuples, and need to be re-mapped to dict.)",
                                    'values': "return a `view` (not a list) of the dictionary's stored values.",
                                    'update': 'update the dictionary with a new key/value pairing. You can (re-)assign new values to a dictionary with simple bracket indexing -- this is an advanced function.',
                                    'fromkeys': 'called from the base class, `dict`, this function returns a dictionary with a key for each item in the given iterable.',
                                    'clear': 'clear all elements from the data container.',
                                    'copy': "create a 'shallow copy' of the dict. this creates a new pointer, which references the underlying objects in the first dict directly. we know that all the keys of the dict are immutable."
                                    }
                                    ,list : {'clear': 'remove all items from the list, in place.',
                                    'copy': "create a 'shallow copy' of the list. This creates a new pointer, but references the same things as in the original (creates a new list).",
                                    'append': 'append a single object to the list, in place.',
                                    'insert': 'insert an object into the list at the given (numeric) index.',
                                    'extend': 'extend the list by appending all items from the given iterable.',
                                    'pop': 'pop the item at the given index, in place. note: This method both returns the popped value, and removes it from the list.',
                                    'remove': 'remove the first occurrence of the singular given value from the list. Errors if the value is not found.',
                                    'index': 'find the (numeric) index of the given item in the list. Errors if the value is not found.',
                                    'count': 'count the instances of the given element in the list. returns int.',
                                    'reverse': 'reverse the indexing of the list, in place. (using the slicing idiom list[::-1] returns the reversed list; this method operates in place.)',
                                    'sort': 'sort the list in ascending order, in place. note: pass the keyword argument `reverse=True` to switch the order.'
                                    }
                                    ,str:{'split': 'split the string at any occurrences the given character sequence, for example whitespace or commas.',
                                    'strip': 'strip away any occurrences of the given character sequence from the both sides of the string.',
                                    'zfill': "pass an int to 'fill' string with 0s; to maintain string length consistency when working with numeric values",
                                    'join': "pass an iterable (ie a list; consisting of only strings) to be joined together using the calling string as separator; like 'collapse' in R",
                                    'capitalize': 'capitalize the first character in the string',
                                    'casefold': 'fold all character values (to lower case)',
                                    'upper': 'capitalize each character in the string',
                                    'lower': 'turn each character in the string to lowercase',
                                    'index': 'return the lowest index (int) in the string for the given sub-string',
                                    'count': 'return the count (int) of occurrences of a given sub-string',
                                    'replace': 'replace the given pattern in the string with the replacement pattern',
                                    'startswith': 'return a boolean value indicating whether the string begins with the given string',
                                    'isnumeric': 'indicate whether the calling string is composed entirely of numeric characters',
                                    'isalpha': 'indicate whether the calling string is composed entirely of alphabetical characters',
                                    'isalnum': 'indicate whether the calling string is composed entirely of alphabetical and numeric characters',
                                    'isascii': 'indicate whether the calling string is composed entirely of ascii characters'}
        ,}

    ############ END INIT ###########

    @property
    def all_games(self):
        return self._all_games
    
    @property
    def game_menu(self):
        return dict(zip(string.ascii_lowercase, list(self.all_games.keys())))
    
    @property
    def score(self):
        return self._total_score
    
    @property
    def tries(self):
        return self._total_tries

    @property
    def all_types(self):
        return self.mutable_types + self.immutable_types
    
    def increment_score(self):
        print('**** Correct! ****')
        self._total_score += 1
    
    def increment_tries(self):
        self._total_tries += 1
        self.response_statement()

    def response_statement(self):
        print(f'Your score is now {self.score} out of {self.tries}')
        print()

    # GAME A #   
    def guess_the_output_type(self, types=[str,int,float,tuple,list,set,dict]):

        response = ''
        while response not in self.exit_strings:
            response = ''

            question = self.simple_value(types=types)
            # set the answer of the question
            answer = type(question)

            # ask the question
            if str == answer:
                print(f"'{question}'")
            else:
                print(question)

            # get the answer
            response = input(f"What is the __name__ of the type above?: ")
            
            # scoring
            if response == answer.__name__:
                print(f"{question} is a {answer}. You picked {response}")
                self.increment_score()

            # response loop
            if response not in self.exit_strings:
                self.increment_tries()
            else:
                break


    # GAME B #
    def input_a_type(self):
        response = ''
        while response not in self.exit_strings:
            response = input('Enter your code below, and it will tell you its Python `type`. Remember, you can always use `type()` or `isinstance()` to check the type of your variables in a notebook. ')
            if response in self.exit_strings:
                break

            try:
                response = eval(response)
            except:
                print(response, "failed")

                if response in self.reserved_words:
                    print(f'{response} is a reserved word in Python')
                print('Woops, converting that to a string. Did you mean to enclose that in quotes?')
                response = f'"{response}"'
#             if response in self.exceptions:
#                 print('thats a reserved name in python!')
#                 if response in self.symbols:
#                     print('almost all symbols can be used in Python syntax, one way or another -- even in Pandas')
#                 if response in self.reserved_names:
#                     print('that name already has a definition in Python syntax')

            print(f"`{response}` is a {type(response)}. Nice!")
            print()

    # GAME C #
    def simple_multiple_choice(self, length_of_values=4):
        #[[type(x) for x in y] for y in PythonQuiz().make_nested_list()]   
        
        response = ''
        while response not in self.exit_strings:
            output_dict = dict()
            choices = ['a','b','c','d']
            right_answer = choices.pop(choices.index(random.choice(choices)))   
            input_list = self.simple_list(size=length_of_values)
            output_dict.update({right_answer:[type(x).__name__ for x in input_list]}) 
            for remaining in choices:
                output_dict.update({remaining:[random.choice([x for x in self.all_types if x not in output_dict.values()]).__name__ for x in range(len(input_list))]})
            print(f"What are the types of the elements inside the following list? {input_list}")
            [print(x) for x in sorted(output_dict.items())]
            print()
            response = input("Select your answer: ")
            if response == right_answer:
                self.increment_score()

            if response in self.exit_strings:
                break
            else:
                self.increment_tries()
                output_dict.clear()


    ## GAME D ###
    def guess_the_len(self):
        response = ''
        while response not in self.exit_strings:
            # generate an iterable value (something with a length)
            a = random.choice([self.simple_value(types=[x]) for x in self.iterable_types])
            # add quotes if its a string
            if type(a) == str:
                print(f"'{a}'")
            else:
                print(a)
            # ask the question
            response = input(f"What is the len() of the above data container? Hint: it's a {type(a)} ")

            # scoring
            if len(a) == int(response):
                self.increment_score()
            #
            if response in self.exit_strings:
                break
            else:
                self.increment_tries()

    ## GAME E ##   
    def guess_the_index(self):
        """guess the index of an element in the container. list; dict; or str"""
        response = ''
        while response not in self.exit_strings:

            temp = self.simple_value(types=[str, tuple, list, dict])
            my_index = random.choice(range(len(temp)))

            # set the index value (if not numeric)
            if type(temp) == dict: 
                key = list(temp.keys())[my_index]
                # if type(key) == str:
                    
            # wtf?
            else:
                while len(set(temp)) != len(temp):
                    temp = random.choice([self.simple_list(), self.simple_value(types=[str])])
                key = my_index
            print()
            print(temp) 
            printed_value = temp[key]
            if type(printed_value) == str:
                printed_value = f"'{printed_value}'"
            response = input(f"What is the index of {printed_value} in the above container? Hint: the container is a {type(temp)} ")
            print()
            if temp[eval(response)] == temp[key]:
                self.increment_score()
            if response not in self.exit_strings:
                self.increment_tries()
            else:
                break
    
    # GAME F
    def type_methods_multiple_choice(self):
        
        # enter the choices
        response = ''
        this_type = None
        objective = None
        while this_type not in [str,list,dict] + self.exit_strings:
            this_type = eval(input("Enter `str`, `list`, or `dict`: "))
            if this_type in self.exit_strings:
                break
        while objective not in ['key', 'value'] + self.exit_strings:  
            objective = input("Would you guess the `key`, or the `value`: ")
            if objective in self.exit_strings:
                break 
        
        mapping = self.question_mappings[this_type]
        
        assert isinstance(mapping, dict), 'mapping must be a dict' 
        assert objective in ['key', 'value'], 'objective must be key or value'

        number_of_options = 4
        #### MAIN LOOP ####

        ### 4 definitions, 1 key;
        response = ''
        while response not in self.exit_strings:

            if objective == 'key':
                options = []

                ### ensure the 4 options are distinct
                while len(options) < number_of_options:
                    # pick a question from the available mapping
                    new_q = random.choice([x for x in mapping.keys()])
                    # if we don't have it already, add the key to the list
                    if new_q not in options:
                        options.append(new_q) 

                # pick the right answer first
                correct_key = random.choice(options)
                # then define it's value, to check our response
                random_question = mapping[correct_key]

                # create a question format dictionary
                choices = dict(zip('abcdefghijkl',options))           
                # since these are all basic python data types, we know they have .__name__ attributes.
                    # in this case, the `keys` are all pre-defined class functions; reserved names (inside the class scope).
                    # stuff like __init__ and __name__ might seem intimidating at first; but they look like that on purpose.
                    # don't worry about them, you don't have to define them or use them at all.
                    # but at the end of the day, they're simply functions which operate (based) on the attributes of the class;
                    # basically they simply create it, destroy it, define it's equivalency (for sorting), what it looks like as a string.
                        # additionally you can define your own properties, which allows you to calculate a value based on other (potentially 'hidden') attributes.

                print(f"Which of the following `{this_type.__name__}` methods does the following?")
                pprint.pprint([choices])
                response = input(f"{random_question} ")
                if choices[response] == correct_key:
                    self.increment_score()

                if response not in self.exit_strings:
                    self.increment_tries()
                else:
                    break


            # give 4 keys; 1 definition        
            elif objective == 'value':
                keys=[]
                options = []
                while len(options) < 4:
                    key = random.choice([x for x in mapping.keys()])
                    value = mapping[key]
                    if value not in options:
                        options.append(value) 
                        keys.append(key)

                choices = dict(zip('abcdefghijkl',options))
                my_answer = random.choice(random.choice([x for x in choices.keys()]))
                answer_index = [x for x in choices.keys()].index(my_answer)
                my_key = keys[answer_index]
                my_definition = choices[my_answer]
                pprint.pprint([choices])
                print()
                print(f"Which of the `{this_type.__name__} method definitions belongs to: {my_key} ?")
                response = input(f"")

                try:
                    if choices[response] == my_definition:
                        self.increment_score()
                except:
                    pass
                if response not in self.exit_strings:
                    self.increment_tries()
                else:
                    break
  
      
    ### GAME G
    def guess_the_index_nested(self, dims=2,height=4,width=4, accepted_values=[tuple,set,float,int,str,bool]):
        response = ''
        while response not in self.exit_strings: 

            base = self.make_matrix(dims=dims,height=height, width=width, types=accepted_values)
            pprint.pprint(base) # only works in anaconda
            x = random.choice(len(height))
            y = random.choice(len(width))
            
            correct_value = eval(base[x][y])
            if type(correct_value) == str:
                correct_value = f"'{correct_value}'"
                
            #response = input(f"What is the row and column `x,y` (0-indexed) of {correct_value}? ")
            response = input(f"If the 2-D matrix is called `base`, how would you index for {correct_value}? ")

            if (eval(response) == correct_value):
                print('you got the right value')
                self.increment_score()
                
            if response not in self.exit_strings:
                self.increment_tries()

            else:
                break    


    ### GAME H
    def nested_dict_indexing(self, rows=4, size=4):
        response = ''
        key_type = int
        while response not in self.exit_strings:
            

            if key_type == str:
                key_type = int
            elif key_type == str:
                key_
            base, first_index, second_index, value = self.keys_and_values_nested(outer_keys=key_type,
                                                                                rows=rows,
                                                                                size=size)
            pprint.pprint(base)
            response = input(f"If this nested dictionary is called `base`, what is the correct way to index for value `{value}`? ")
            if response in self.exit_strings:
                break
            try:
                response = eval(response)
            except:
                response = f'{response}'
            #print(response,  f'base[{first_index}][{second_index}]' )
            if response == value:#f'base[{first_index}][{second_index}]':
                pprint.pprint('**** You Win ****!')
                self.increment_score()
            if response not in self.exit_strings:
                self.increment_tries()

#####################################################################################
 





############ RUNTIME #############
    
    def run_game(self, choice):
        '''each game is a function, and must be executed using parentheses'''
        return self.all_games[self.game_menu[choice]]()
    

    def start_menu(self):
        response = ''
        while response not in self.exit_strings:
            print('Pick a Game:')
            pprint.pprint(self.game_menu)
            response = input()
            try:
                self.run_game(response)
                print()

            except:
                #print(f'error running game {response}, please try again')
                pass


        ### if response in self.exit_strings:   
        try:   
            print(f'Exiting. You got {self.score} right, out of {self.tries} tries. Thats {round(self.score/self.tries*100,2)}%!')
        except ZeroDivisionError:
            pass

        
    
if __name__ == '__main__':
    a = PythonQuiz()
    a.start_menu()
