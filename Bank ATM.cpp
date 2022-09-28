
#include <iostream>

using namespace std;

int main()
{
    int pin;
    int choice;
    int balance = 1000;
    int Withdrow;
    int deposit;
    
    
    cout << "\n\n               Welcon to Madrasatech ATM Servic Banking                \n\n";
    
    
    while(pin != 1234)
    {
            cout << "Enter your pin : ";
            cin >> pin;
    }
    
    
    
    do {
            cout << "1. Check account " << endl;
            cout << "2. Withdrow Cash " << endl;
            cout << "3. Deposit Cash  " << endl;
            cout << "4. Quit " << endl;
            
            
        cout << "chose from the menu : ";
        cin >> choice;
        
        
            switch(choice) 
            {
                    case 1 :
                        cout << "Your current balance is : " << balance << " $" << endl;
                        break;
           
           
                    case 2 :
                        cout << "Enter the amount to Withdrow : " ;
                        cin >> Withdrow;
                        
                        if(Withdrow > balance)
                        {
                                cout << "You don't have Money .....";
                        }
                        else
                        {
                             balance -= Withdrow;
                             cout << "Your current balance is : " << balance << " $" << endl;
                             break;   
                        }
                        
                        
                    case 3 :
                        cout << "Enter the amount : ";
                        cin >> deposit;
                        
                        balance += deposit;
                        cout << "Your current balance is : " << balance << " $" << endl;
                        break;
                        
                        
                   case 4 :
                        cout << "********** Thank You For Using Madrasatech Bank **********" << endl;
                        break;
                        
                        
                   default :
                        cout<< "The number does not exist .....";
                        break;
            }
            
    } while(true);
    

    return 0;
}
