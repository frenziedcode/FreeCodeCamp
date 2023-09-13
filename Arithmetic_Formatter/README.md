# Arithmetic Formatter

Formatador Aritmético
Você estará trabalhando neste projeto com nosso código inicial Replit.

Comece importando o projeto no Replit.
Em seguida, você verá uma janela .replit.
Select Use run command and click the Done button.
Os alunos da escola primária geralmente organizam problemas aritméticos verticalmente para torná-los mais fáceis de resolver. Por exemplo, "235 + 52" se torna:

  235
+  52
-----
Crie uma função que receba uma lista de strings que são problemas aritméticos e retorne os problemas organizados verticalmente e lado a lado. A função deve, opcionalmente, ter um segundo argumento. Quando o segundo argumento é definido como True, as respostas devem ser exibidas.

Exemplo
Chamada de Função:

arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])
Saída:

   32      3801      45      123
+ 698    -    2    + 43    +  49
-----    ------    ----    -----
Chamada de Função:

arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True)
Saída:

  32         1      9999      523
+  8    - 3801    + 9999    -  49
----    ------    ------    -----
  40     -3800     19998      474
Regras
A função retornará a conversão correta se os problemas fornecidos estiverem formatados corretamente, caso contrário, retornará uma string que descreve um erro que é significativo para o usuário.

Situações que retornarão um erro:
Se houver muitos problemas fornecidos à função. O limite é cinco, qualquer coisa a mais retornará:Error: Too many problems.
Os operadores apropriados que a função aceitará são adição e subtração. A multiplicação e a divisão retornarão um erro. Outros operadores não mencionados neste marcador não precisarão ser testados. O erro retornado será:Error: Operator must be '+' or '-'.
Cada número (operando) deve conter apenas dígitos. Caso contrário, a função retornará:Error: Numbers must only contain digits.
Cada operando (também conhecido como número de cada lado do operador) tem um máximo de quatro dígitos de largura. Caso contrário, a string de erro retornada será:Error: Numbers cannot be more than four digits.
Se o usuário forneceu o formato correto dos problemas, a conversão que você retornar seguirá estas regras:
Deve haver um único espaço entre o operador e o maior dos dois operandos, o operador estará na mesma linha que o segundo operando, ambos os operandos estarão na mesma ordem fornecida (o primeiro será o superior e o segundo será o inferior).
Os números devem estar alinhados à direita.
Deve haver quatro espaços entre cada problema.
Deve haver traços na parte inferior de cada problema. Os traços devem percorra toda a extensão de cada problema individualmente. (O exemplo acima mostra como isso deve ser.)
Desenvolvimento
Write your code in arithmetic_arranger.py. For development, you can use main.py to test your arithmetic_arranger() function. Click the "run" button and main.py will run.

Testes
The unit tests for this project are in test_module.py. We are running the tests from test_module.py in main.py for your convenience. The tests will run automatically whenever you hit the "run" button. Alternatively you may run the tests by inputting pytest in the console.

Enviando
Copie o URL do seu projeto e envie-o abaixo.




This is the boilerplate for the Arithmetic Formatter project. Instructions for building your project can be found at https://www.freecodecamp.org/learn/scientific-computing-with-python/scientific-computing-with-python-projects/arithmetic-formatter
