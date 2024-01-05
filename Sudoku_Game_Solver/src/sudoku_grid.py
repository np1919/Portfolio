
import pandas as pd
import numpy as np
from .cell import Cell
from .grids import hard_game, expert_game
from .nine_cell import Row, Column, Nonant


class SudokuGrid:
    
    def __init__(self, show_steps=False):
        # if cells == None:
        # # nonants
        # make the grid
        self.show_steps = show_steps
        self.cells = []
        self.rows = [Row(self, x) for x in range(1,10)] 
        self.columns = [Column(self, x) for x in range(1,10)]
        self.nonants = [Nonant(self, x) for x in range(1,10)]


        # make cells, assign column; row; nonagram
        for x in self.rows:
            for y in self.columns:

                if x.rownumber >= 7:
                    if y.colnumber >= 7:
                        self.cells.append(Cell(self, row=x, column=y, nonant=self.nonants[8]))
                    elif (y.colnumber <= 6) and (y.colnumber >= 4):
                        self.cells.append(Cell(self, row=x, column=y, nonant=self.nonants[7]))
                    elif y.colnumber <= 3:
                        self.cells.append(Cell(self, row=x, column=y, nonant=self.nonants[6]))

                if (x.rownumber <= 6 ) and (x.rownumber >= 4):
                    if y.colnumber >= 7:
                        self.cells.append(Cell(self, row=x, column=y, nonant=self.nonants[5]))
                    elif (y.colnumber <= 6 ) and (y.colnumber >= 4):
                        self.cells.append(Cell(self, row=x, column=y, nonant=self.nonants[4]))
                    elif y.colnumber <= 3:
                        self.cells.append(Cell(self, row=x, column=y, nonant=self.nonants[3]))

                if x.rownumber <= 3:
                    if y.colnumber >= 7:
                        self.cells.append(Cell(self, row=x, column=y, nonant=self.nonants[2]))
                    elif (y.colnumber <= 6) and (y.colnumber >= 4):
                        self.cells.append(Cell(self, row=x, column=y, nonant=self.nonants[1]))
                    elif y.colnumber <= 3:
                        self.cells.append(Cell(self, row=x, column=y, nonant=self.nonants[0]))

        for ninecell in self.rows + self.columns + self.nonants:
            ninecell.grid = self
        
    
    @property
    def make_df(self):
        out = pd.DataFrame(np.array(self.cells).reshape(9,9), index=range(1,10), columns=range(1,10))

        return out
    
    @property
    def show_grid(self):
        '''for easy visual inspection..'''
        def highlight_3x3_blocks(val):
            if val.nonant.number not in range(0,9,2):
                rgba_color = 'rgba(174, 214, 241, 0.6)'  # Light blue with lower opacity
                return f'background-color: {rgba_color}; border: 2px solid white' #
            else:
                rgba_color = 'rgba(213, 245, 227, 0.6)'  # Light green with lower opacity
                return f'background-color: {rgba_color}; border: 2px solid white;'

        df = self.make_df
        styled_df_blocks = df.style.map(highlight_3x3_blocks)

        try:
            display(styled_df_blocks)
        except:
            print(styled_df_blocks)



    @property
    def total_trues(self):
        return sum([1 for x in self.cells if x.value is not None])
    
    @property
    def show_untrues(self):
        data = [len(x.not_these) if x.value == None  else "" for x in self.cells]
        return pd.DataFrame(np.array(data).reshape(9,9), index=range(1,10), columns=range(1,10))

    @property
    def show_possibles(self):
        return pd.DataFrame(np.array([x for x in self.possibles]).reshape(9,9), index=range(1,10), columns=range(1,10))

    @property
    def possibles(self):
        return [x.possible if x.value == None else set() for x in self.cells ] 

        # return [x.not_these.symmetric_difference(set([1,2,3,4,5,6,7,8,9])) if x.value == None else x.value for x in self.cells] 
    
    @property
    def show_impossibles(self):
        return pd.DataFrame(np.array([x for x in self.impossibles]).reshape(9,9), index=range(1,10), columns=range(1,10))

    @property
    def impossibles(self):
        return [x.not_these if x.value == None else set() for x in self.cells] 
    
    @property
    def show_nonants(self):
        return pd.DataFrame(np.array([x.nonant.nonant for x in self.cells]).reshape(9,9), index=range(1,10), columns=range(1,10))

    def __repr__(self):
        return str(self.show_grid)
    
    # def setup(self):
    #     for k,v in load_game().items():
    #         self.cells[k].value = v
    #         self.cells[k].in_ink = True

    def solve(self):
        while self.total_trues != 81:                
            for _ in [x for x in self.cells if x.value == None]:
                    solved = _.solve_cell()
                    # if solved == True:
                    if solved == True:
                        for x in _.row.cells + _.column.cells + _.nonant.cells:
                            if x.value is None:
                                x.solve_cell()
            # print(self.total_trues)

    
    # def make_random(self):
    #     import random 

    #     random.shuffle(self.cells)
    #     for x in self.cells:
            
if __name__ == '__main__':
    a=SudokuGrid()
    hard_game(a)
    a.show_grid
    # a.show_nonants
    # a.show_possibles
    # a.len_untrues
    # a.trues