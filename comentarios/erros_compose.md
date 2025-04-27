cmd como adm

netstat -ano | findstr :5002

retorno
  TCP    0.0.0.0:5002           0.0.0.0:0              LISTENING       15151
  TCP    [::]:5002              [::]:0                 LISTENING       14141
  TCP    [::1]:5002             [::]:0                 LISTENING       13131

anotar o pid

taskkill /PID NUMERO_PID /F

taskkill /PID 15151 /F

retorno
ÊXITO: o processo com PID 15368 foi finalizado.
ou
ERRO: o processo "15368" não foi encontrado.

fecha o processo


