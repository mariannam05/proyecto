questions=[
{
"question": "¿Cuál es el valor de out de la siguiente lógica? a, b = False, True, out = (a and b and not a) or (not b) or (b and a) or (a and not a and not b) ",
"answer": "False"
},
{
"question": "¿Cuál es el valor de out de la siguiente lógica? a, b = False, True, out = (a and b and a) or (b) or (b or a) or (a and not a and not b)",
"answer": "True"
}
]

p1 = questions[0]
p2 = questions[1]
pregunta1 = p1['question']
respuesta1 = p1['answer']
pregunta2 = p2['question']
respuesta2 = p2['answer']

print(pregunta1)