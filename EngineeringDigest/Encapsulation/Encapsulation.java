class Encapsulation{
    public static void main(String[] args){
        Bank bank = new Bank(1000);
        bank.deposit(1000);
        System.out.println("Balance after deposit: " + bank.getBalance());

        bank.withdraw(500);
        System.out.println("Balance after withdrawal: " + bank.getBalance());

        bank.withdraw(0); // Attempting to withdraw more than the balance
    }
}

class Bank{
    private int balance=0 ;
    
    public Bank(int initialBalance) {
        // Constructor to initialize the bank account with a balance of 0
        this.balance = initialBalance;
    } 

    public void deposit(int amount){
        this.balance+= amount;
    }

    public void withdraw(int amount){
        if (amount > this.balance && amount != 0) {
            System.out.println("Insufficient balance");
            int z=amount - this.balance;
            System.out.println("Over balance: " + z);
        } else {
            this.balance -= amount;
            System.out.println("Withdrawal successful. Amount withdrawn: " + amount);
        } 
    }
    public int getBalance() {
        return this.balance;
    }
    }