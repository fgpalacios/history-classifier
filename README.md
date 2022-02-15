# History Classifier

***Tips de armado de entorno***

- Para crear el contenedor ejecutar start.sh

***Tips de Desarrollo***

Si se desea re-entrenar agregando nuevas entradas al dataset almacenado en data, usar classification-trainer.ipynb

Luego realizar un restar de docker para que tome los cambios

docker restart [image]

Se puede usar test.ipynb para probar que retorna desde un entorno python

***Funcionalidad***

Retorna un json con etiquetados y probalidades de acuerdo a los valores entrenados

Ejemplo de llamado: 

curl -X POST http://localhost:8884/predictor -H 'Content-Type: application/json' -d '{"input_text":"Messi y sus amigos"}'

Retorna:

#4. mi madurez : 0.6096104549682914
#2. mi infancia : 0.3042363024488902
#3. mi adolescencia y juventud : 0.06099918753578126
#1. quien soy yo? : 0.025154055047037174


