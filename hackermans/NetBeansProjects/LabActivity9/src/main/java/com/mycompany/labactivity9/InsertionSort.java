/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 */

package com.mycompany.labactivity9;

import java.util.Scanner;
import java.util.Arrays;

public class InsertionSort {
    int[] array;
    
    void insertionSort() {
        int n = array.length;
        System.out.println(Arrays.toString(array));
        for (int i = 1; i < n; ++i) {
            int key = array[i];
            System.out.print("Key: " + key);
            int j = i - 1;
            System.out.println("\tJ: " + j);
            
            while (j >= 0 && array[j] > key) {
                array[j + 1] = array[j];
                j = j - 1;
            }
            array[j + 1] = key;
            System.out.println(Arrays.toString(array));
        }
    }
    
    public static void main(String[] args) {
        Scanner console = new Scanner(System.in);
        InsertionSort obj = new InsertionSort();
        
        System.out.print("Length: ");
        int n = console.nextInt();
        obj.array = new int[n];
        
        for (int i = 0; i < n; i++) {
            System.out.print("Value " + i + ": ");
            obj.array[i] = console.nextInt();
        }
        
        obj.insertionSort();
    }
}
