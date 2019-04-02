package niks;

/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 *
 * @author student
 */
public class Cla {
    public static void main(String[] args) {
        //args[0]args[1] and so on
        int num1=Integer.parseInt(args[0]); //parseint convert string nto integer
        int num2=Integer.parseInt(args[1]);
        int sum=num1+num2;
        System.out.println("sum of number through command line argument"+sum);
        
    }
    
}
