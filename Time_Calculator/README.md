Você estará trabalhando neste projeto com nosso código inicial Replit.

Comece importando o projeto no Replit.
Em seguida, você verá uma janela .replit.
Select Use run command and click the Done button.
Write a function named add_time that takes in two required parameters and one optional parameter:

um horário de início no formato de relógio de 12 horas (terminando em AM ou PM)
um tempo de duração que indica o número de horas e minutos
(opcional) um dia de início da semana, sem distinção entre maiúsculas e minúsculas
A função deve adicionar o tempo de duração ao horário de início e retornar o resultado.

If the result will be the next day, it should show (next day) after the time. If the result will be more than one day later, it should show (n days later) after the time, where "n" is the number of days later.

Se a função receber o parâmetro opcional do dia inicial da semana, a saída deve exibir o dia da semana do resultado. O dia da semana na saída deve aparecer após o horário e antes do número de dias depois.

Abaixo estão alguns exemplos de diferentes casos com os quais a função deve lidar. Preste muita atenção ao espaçamento e à pontuação dos resultados.

add_time("3:00 PM", "3:10")
# Returns: 6:10 PM

add_time("11:30 AM", "2:32", "Monday")
# Returns: 2:02 PM, Monday

add_time("11:43 AM", "00:20")
# Returns: 12:03 PM

add_time("10:10 PM", "3:30")
# Returns: 1:40 AM (next day)

add_time("11:43 PM", "24:20", "tueSday")
# Returns: 12:03 AM, Thursday (2 days later)

add_time("6:30 PM", "205:12")
# Returns: 7:42 AM (9 days later)
Não importe nenhuma biblioteca Python. Suponha que os horários de início sejam horários válidos. Os minutos no tempo de duração serão um número inteiro menor que 60, mas a hora pode ser qualquer número inteiro.

Desenvolvimento
Write your code in time_calculator.py. For development, you can use main.py to test your time_calculator() function. Click the "run" button and main.py will run.

Testes
The unit tests for this project are in test_module.py. We imported the tests from test_module.py to main.py for your convenience. The tests will run automatically whenever you hit the "run" button.

Enviando
Copie o URL do seu projeto e envie-o para o freeCodeCamp.