import solara

settings_addition = solara.reactive({
    "total_sum": 25,
    "number_questions": 2
 })

start_train = solara.reactive( True )