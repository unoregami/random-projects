/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 */

package com.mycompany.jumpsearch;

import java.util.Arrays;

public class JumpSearch {
    
    public static int jumpSearch(int[] array, int x) {
        int n = array.length;
        int step = (int)Math.sqrt(array.length);    //step is the jump per index
        int prev = 0;   //stores the previous jump index
        
        for (int i = step; array[i] < x;) {
            if (array[i] == x) {
                return i;
            }
            prev = (i + 1); //inc by one since it is confirmed that i is not the position of x
            i+=step;        //inc is moved here since if array is out of bounds we can break it without triggering the ArrayOutOfBounds Exception in line 16
            if (i >= n) {
                break;
            }
        }
        
        while (array[prev] < x) {
            prev++;
        }
        
        if (array[prev] == x) {
                return prev;
            }
        return - 1;
    }

    public static void main(String[] args) {
        int[] sample = {1, 3, 6, 7, 18, 23, 41, 65, 94};
        int x = sample[(int)(Math.random() * sample.length)];
        System.out.println(Arrays.toString(sample));
        System.out.println(x);
        
        int ret = jumpSearch(sample, x);
        System.out.println("Position " + ret);
    }
}
