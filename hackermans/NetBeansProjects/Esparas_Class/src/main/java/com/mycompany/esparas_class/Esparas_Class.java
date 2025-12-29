/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 */

package com.mycompany.esparas_class;

/**
 *
 * @author ACER-PC
 */
public class Esparas_Class {

    public static void main(String[] args) {
        Student obj = new Student();
        
        obj.setStudentNo(202080783);
        obj.setFname("Adolfo I ");
        obj.setLname("Esparas");
        obj.setCourse("BCS");
        
        System.out.println("Student No: " + obj.getStudentNo() + "\nName: " + obj.getFname() + obj.getLname() + "\nCourse: " + obj.getCourse());
    }
}
