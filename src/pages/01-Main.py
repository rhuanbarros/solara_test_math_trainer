import solara
import solara.lab

from inspect import getsourcefile
import os.path
import sys

current_path = os.path.abspath(getsourcefile(lambda:0))
current_dir = os.path.dirname(current_path)
parent_dir = current_dir[:current_dir.rfind(os.path.sep)]

sys.path.insert(0, parent_dir)

from state import settings_addition, start_train

def vai():
    print("FOIIIIII")
    start_train.set( True )

@solara.component
def Page():
    
    with solara.Column(margin="10"):
        solara.Markdown(
            """
            ## Settings
            """
        )
        with solara.Column(margin="10", gap="12px"):
            with solara.lab.Tabs():
                with solara.lab.Tab("Addition"):
                    with solara.Column(margin="0", gap="22px"):
                        solara.InputInt(label="Total sum of operators", value=settings_addition.value["total_sum"])
                        solara.InputInt(label="Number of questions", value=settings_addition.value["number_questions"])
                
                        with solara.Link("/addition"):
                            solara.Button("Start train", on_click=vai)
                
                with solara.lab.Tab("Subtraction"):
                    solara.Markdown("World")
                
                
