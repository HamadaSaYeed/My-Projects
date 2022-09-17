                                                       // calculator

#include <iostream>

using namespace std;

void sum(int num1,int num2);       //  '+'

void subtract(int num1,int num2);  //  '-'

void multiply(int num1,int num2);  //  '*'

void dividing(int num1,int num2);  //  '/'



int main()
{
        
    cout<<"What's operator is used  ";
    cout<<"[ +  ,  -  ,  /  ,  * ] ? ";
    char op;
    cin >> op;
    
    
    int number_1 ;
    cout << "Enter a number_1 : ";
    cin >> number_1 ;
    
    
    int number_2 ;
    cout << "Enter a number_2 : ";
    cin >> number_2 ;
    
    
    
    if(op == '+')
    {
        sum(number_1,number_2);    
    }
    else if(op == '-')
    {
        subtract(number_1,number_2);    
    }
    else if(op == '/')
    {
        dividing(number_1,number_2);    
    }
    else if(op == '*')
    {
        multiply(number_1,number_2);    
    }
    else
    {
            cout << "Not Found !" << endl;
    }

    return 0;
}



void sum(int num1,int num2)
{ 
        
        int sum_1 = num1 + num2;

        cout << num1 << " + " << num2 << " = " << sum_1 << endl;
        
}


void subtract(int num1,int num2) 
{ 
        
        int sum_2 = num1 - num2;
        
        cout << num1 << " - " << num2 << " = " << sum_2 << endl;
        
}


void multiply(int num1,int num2) 
{ 

        int sum_3 = num1 * num2;
        
        cout << num1 << " * " << num2 << " = " << sum_3 << endl;
        
}


void dividing(int num1,int num2) 
{ 

        int sum_4 = num1 / num2;
        
        cout << num1 << " / " << num2 << " = " << sum_4 << endl;
        
}