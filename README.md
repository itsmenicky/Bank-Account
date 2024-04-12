<h1 align=center>Bank Account 💸</h1>
<p text-align=justify>Considerando que uma agência bancária tem 5 clientes e cada cliente possui uma conta:</p>
<table align=center>
  <thead>
    <tr>
      <th>Cliente</th>
      <th>Saldo em Conta Corrente</th>
    </tr>
    <tr>
      <th>Marcos</th>
      <th>R$ 1.000,00</th>
    </tr>
    <tr>
      <th>Julia</th>
      <th>R$ 250,00</th>
    </tr>
    <tr>
      <th>João</th>
      <th>R$ 2.500,00</th>
    </tr>
    <tr>
      <th>Roberto</th>
      <th>R$ 3.000,00</th>
    </tr>
    <tr>
      <th>Janaína</th>
      <th>R$ 4.500,00</th>
    </tr>
  </thead>
</table>

<p text-align=justify>Foi desenvolvido um algoritmo em Python para gerenciar essas contas. Como o algoritmo precisa lidar com diferentes contas bancárias, utilizei a classe <strong>BankAccount</strong> para
armazenar o nome do correntista, saldo da conta e senha.</p>

<p text-align=justify>Considerando que foi criado um novo imposto que deve ser aplicado às operações bancária, para cada saque realizado deve-se descontar 0.25% do valor sacado do saldo restante do cliente. Os valores descontados são acumulados em um atributo privado <strong>__cpmf</strong>, que foi incluído na classe <strong>BankAccount</strong>.</p>

<p text-align=justify>Foram criados também na classe <strong>BankAccount</strong> os métodos <strong>get_password</strong> e <strong>get_cpmf</strong></p>

<h2>Programa Principal</h2>
<p text-align=justify>No programa principal criei cinco instâncias da <strong>ContaBancaria</strong> e armazenei esses objetos em uma lista.
Adicionei uma função <strong>info</strong> que recebe a lista de contas bancárias e exibe na tela os dados
(correntista e saldo) de todas as contas.
Também adicionei as interações do programa com o usuário. Para isso, foram criadas as funções
<strong>withdraw_interaction</strong>, <strong>deposit_interaction</strong> e  <strong>transfer_interaction</strong>; e implementei um menu de opções na aplicação.</p>

<p text-align=justify>Foi implementado também um autenticador de senhas para maior segurança nas operações bancárias do programa, através da função <strong>password_authenticator</strong>, que recebe como parâmetros o <strong>account_index</strong>(índice referente a conta do usuário que está realizando a operação) e a senha a ser verificada, <strong>verify</strong>.</p>
