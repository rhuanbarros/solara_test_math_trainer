import solara
import pandas as pd

answer = solara.reactive(None)
answer_list = solara.reactive([])
df = solara.reactive( None )
show_df = solara.reactive( 0 )
# df = None

@solara.component
def Page():
    def update_list(data):
        if answer.value != None and answer.value != "":
            answer_list.value.append( { "number": data } )
        answer.value = ""
        show_df.value += 1
        
    # solara.Button(label=f"Clicked: {answer}", on_click=update_list, color=color)
    
    with solara.Card("Edit"):
        solara.InputInt(label="Answer", value=answer, on_value=update_list)
    
    if show_df.value:
        df = pd.DataFrame( answer_list.value )
        # solara.DataFrame( df )
        solara.display( df )
    