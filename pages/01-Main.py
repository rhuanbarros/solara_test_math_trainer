import solara
import solara.lab

settings_addition = solara.reactive({
    "total_sum": 25,
    "number_questions": 2
 })

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
                            solara.Button("Start train")
                
                with solara.lab.Tab("Subtraction"):
                    solara.Markdown("World")
                
                
