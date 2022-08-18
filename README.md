#Controlador por Atraso de Fase

Programa em python para projetar uma controlador por avanço de fase.

Nele é necessário adicionar a Função de Transferência (g), a Margem de Fase Desejada (pmd), o valor para o Erro Estacionário (ess), a fórmula para a Constante de Erro Estático da Velocidade (kv), a fórmula para cálculo do ganho (k) e o Ângulo de Avanço (anguloAvanco).

Todos os valores que precisam ser adicionados conforme especificação do projeto são informados nos comentários do código. Além disso, é feito o print dos principais resultados calculados.

P.S: A função interp1d apresenta limitações, devido à isso podem haver exemplos de aplicação em que a mesma não é capaz de executar. Esta falha costuma ocorrer para aplicação que apresentam um alto valor para o ganho (k).