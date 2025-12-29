
package com.mycompany.labactivity4;
import java.io.FileNotFoundException;
import java.util.Scanner;
import java.io.FileReader;
import java.io.PrintWriter;
import java.text.DecimalFormat;


public class LabActivity4 {

    public static void main(String[] args) throws FileNotFoundException {
        DecimalFormat form = new DecimalFormat("00.00");
        Scanner console = new Scanner(new FileReader("grade.dat"));
        String firstName, lastName;
        double average;
        PrintWriter outFile = new PrintWriter("average.txt");
        
        for (int j = 0; j < 5; j++) {
            average = 0;
            firstName = console.next();
            lastName = console.next();
        
            for (int i = 0; i < 5; i++) {
                average += console.nextDouble();
            }
            average = average / 5;
        
            outFile.println(firstName + " " + lastName + "\t–\tAverage: " + form.format(average));
        }
        outFile.close();
        console.close();
    }
}
