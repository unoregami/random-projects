/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package com.mycompany.labactivity7;

/**
 *
 * @author ACER-PC
 */
public class Clock {
    private int hours;
    private int minutes;
    private int seconds;
    
  
    public int incHours(int hr){
        if (hr <= 23)
            return hr;
        hr -= 24;
        this.hours = hr;
        return incHours(hr);
    }
    public int incMinutes(int min){
        if (min <= 59)
            return min;
        this.hours++;
        min -= 60;
        this.minutes = min;
        incHours(this.hours);
        return incMinutes(min);
    }
    public int incSeconds(int sec){
        if (sec <= 59)
            return sec;
        this.minutes++;
        sec -= 60;
        incMinutes(this.minutes);
        return incSeconds(sec);
    }
    
    public void setHours(int hr){
        if (hr >= 0 && hr <= 23){
            this.hours += hr;
            incHours(this.hours);
        } else if (hr > 23)
            this.hours += incHours(hr);
        else
            this.hours += 0;
    }
    public void setMinutes(int min){
        if (min >= 0 && min <= 59){
            this.minutes += min;
            incMinutes(this.minutes);
        } else if (min > 59)
            this.minutes += incMinutes(min);
        else 
            this.minutes += 0;
    }
    public void setSeconds(int sec){
        if (sec >= 0 && sec <= 59)
            this.seconds = sec;
        else if (sec > 59)
            this.seconds = incSeconds(sec);
        else
            this.seconds = 0;
    }
    
    public void setTime(int hr, int min, int sec){
        this.hours = 0; this.minutes = 0;
        this.setSeconds(sec);
        this.setMinutes(min);
        this.setHours(hr);
    }
    
    public String displayTime(){    //27:53:
        String time = "";
        
        if (this.hours < 10)
            time = time + "0";
        time = time + this.hours + ":";
        
        if (this.minutes < 10)
            time = time + "0";
        time = time + this.minutes + ":";
        
        if (this.seconds < 10)
            time = time + "0";
        time = time + this.seconds;
        
        if (this.hours > 11)
            time = time + " PM";
        else
            time = time + " AM";
        
        return time;
    }
}
