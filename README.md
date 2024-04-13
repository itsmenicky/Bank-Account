<h1 align=center>Bank Account 💸</br></br><div align=center><img src="http://ForTheBadge.com/images/badges/made-with-python.svg"></div></h1>
<p text-align=justify>Considering that a bank agency has 5 customers and each customer has an account:</p>
<table align=center>
  <thead>
    <tr>
      <th>Customer</th>
      <th>Balance</th>
    </tr>
    <tr>
      <th>Marcos</th>
      <th>$ 1.000,00</th>
    </tr>
    <tr>
      <th>Julia</th>
      <th>$ 250,00</th>
    </tr>
    <tr>
      <th>João</th>
      <th>$ 2.500,00</th>
    </tr>
    <tr>
      <th>Roberto</th>
      <th>$ 3.000,00</th>
    </tr>
    <tr>
      <th>Janaína</th>
      <th>$ 4.500,00</th>
    </tr>
  </thead>
</table>

<p text-align=justify>An algorithm was developed in Python to manage these accounts. As the algorithm needs to deal with different bank accounts, I used the <strong>BankAccount</strong> class to store the account holder's name, account balance and password.</p>

<p text-align=justify>Considering that a new tax was created that must be applied to banking operations, for each withdrawal made, 0.25% of the amount withdrawn must be deducted from the customer's remaining balance. The discounted amounts are accumulated in a private attribute <strong>__cpmf</strong>, which has been added to the <strong>BankAccount</strong> class.
</p>

<p text-align=justify>The <strong>get_password</strong> and <strong>get_cpmf</strong> methods were also created in the <strong>BankAccount</strong> class.</p>

<h2>Main Program</h2>
<p text-align=justify>In the main program I created five instances of <strong>BankAccount</strong> and stored these objects in a list. I added an info function that receives the list of bank accounts and displays the data (account holder and balance) of all accounts on the screen. I also added the program's interactions with the user. For this, the <strong>withdraw_interaction</strong>, <strong>deposit_interaction</strong> and <strong>transfer_interaction</strong> functions were created; and implemented an options menu in the application.</p>

<p text-align=justify>A password authenticator was also implemented for greater security in the program's banking operations, through the <strong>password_authenticator</strong> function, which receives as parameters the <strong>account_index</strong> (index referring to the user's account that is carrying out the operation) and the password to be verified, <strong>verify</strong>.</p>
