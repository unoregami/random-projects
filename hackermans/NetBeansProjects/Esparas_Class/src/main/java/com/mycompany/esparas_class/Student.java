package com.mycompany.esparas_class;

public class Student {
    private int studentNo;
    private String fname, lname, course;
    
    public Student(){
        studentNo = 0;
        fname = null; lname = null; course = null;
    }

    public void setStudentNo(int studentNo) {
        this.studentNo = studentNo;
    }
    public void setFname(String fName) {
        this.fname = fName + " ";
    }
    public void setLname(String lName) {
        this.lname = lName;
    }
    public void setCourse(String course) {
        this.course = course;
    }
    public int getStudentNo() {
        return this.studentNo;
    }
    public String getFname() {
        return this.fname;
    }
    public String getLname() {
        return this.lname;
    }
    public String getCourse() {
        return this.course;
    }
    
}
