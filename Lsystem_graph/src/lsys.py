# -*- coding: utf-8 -*-
"""
Created on Sun May 14 12:18:23 2023

@author: Evgeniy
"""

import py5

"""
"""

class LSystem:
    def __init__(self, axiom, ruleset):
        self.sentence = axiom
        self.ruleset = ruleset
        self.generation = 0

  # Generate the next generation
    def generate(self):
        # 
        nextgen = []
        # For every character in the sentence
        for  i in range(0, len(self.sentence),1): 
            # What is the character
            curr_char = self.sentence[i]
            # We will replace it with itself unless it matches one of our rules
            replace = "" + curr_char
            for j in range(0, len(self.ruleset), 1):
                a = self.ruleset[j].getA()
                # if we match the Rule, get the replacement String out of the Rule
                if a == curr_char:
                    replace = self.ruleset[j].getB()
                    break 
            # Append replacement String
            nextgen.append(replace)
        # Replace sentence
        self.sentence = "".join(nextgen)
        # Increment generation
        self.generation += 1
    
    def get_sentence(self):
        return self.sentence 

    def get_generation(self):
        return self.generation 