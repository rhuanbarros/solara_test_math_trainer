import solara
import pandas as pd
import random
import time

# code to import package in parent directory
from inspect import getsourcefile
import os.path
import sys
current_path = os.path.abspath(getsourcefile(lambda:0))
current_dir = os.path.dirname(current_path)
parent_dir = current_dir[:current_dir.rfind(os.path.sep)]
sys.path.insert(0, parent_dir)

from state import settings_addition, start_train

# --------------------------------- STATE
answer = solara.reactive(None)
answer_list = solara.reactive([])
df = solara.reactive( None )
update_screen = solara.reactive( 0 )

# --------------------------------- CONSTANS
OPERATION = "+"
        
# --------------------------------- FUNCTIONS
def QuestionAnswered(n1, n2, operation, correct_answer, user_answer=None):
    return {"n1": n1, "n2": n2, "operation": operation, "correct_answer": correct_answer, "user_answer": user_answer}
    
def summed_max_generator(max, operation):
    while True:
        n1 = random.randint(1,99)
        n2 = random.randint(1,99)
        correct_answer = n1 + n2
        if correct_answer < max:
            yield QuestionAnswered(n1, n2, operation, correct_answer)

def summed_max_list():
    return [ next( summed_max_generator(settings_addition.value["total_sum"], OPERATION ) ) for n in range( settings_addition.value["number_questions"] ) ]

def update_list(data):
    global question
    if answer.value != None and answer.value != "":
        question.value["user_answer"] = data
        answer_list.value.append( question.value )
        answer.value = ""
        update_screen.value += 1
        global start_train
        start_train.set( False )
        
@solara.component
def Page():
    global questions
    if start_train.value == True:
        questions = solara.reactive( summed_max_list() )
        answer_list.set( [] )
    
    global question
    # global s
    
    if len(questions.value):
        question = solara.reactive( questions.value.pop() )
        
        if 'n1' in question.value:
            with solara.Card("Edit"):
                solara.Markdown(f"""{question.value['n1']} {question.value['operation']} {question.value['n2']}""")
        
            with solara.Card("Edit"):
                solara.InputInt(label="Answer", value=answer, on_value=update_list)
            
            if update_screen.value:
                df = pd.DataFrame( answer_list.value )
                # solara.DataFrame( df )
                solara.display( df )
    else:
        # global start_train
        start_train.set( False )
        
        solara.Markdown(f"""Acabaram as questoes""")
        
        df = pd.DataFrame( answer_list.value )
        # solara.DataFrame( df )
        solara.display( df )
        
        