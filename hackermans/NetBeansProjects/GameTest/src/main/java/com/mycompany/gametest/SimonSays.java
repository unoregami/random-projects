/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/GUIForms/JFrame.java to edit this template
 */
package com.mycompany.gametest;

import java.util.Arrays;
import java.awt.Color;
import javax.swing.JOptionPane;

public class SimonSays extends javax.swing.JFrame {

    /**
     * Creates new form SimonSays
     */
    public SimonSays() {
        initComponents();
        this.setLocationRelativeTo(null);
        randomColor();
    }
    
    
    @SuppressWarnings("unchecked")
    // <editor-fold defaultstate="collapsed" desc="Generated Code">//GEN-BEGIN:initComponents
    private void initComponents() {

        jFrame1 = new javax.swing.JFrame();
        jPanel1 = new javax.swing.JPanel();
        red = new javax.swing.JButton();
        orange = new javax.swing.JButton();
        green = new javax.swing.JButton();
        leaf = new javax.swing.JButton();
        grey = new javax.swing.JButton();
        pink = new javax.swing.JButton();
        yellow = new javax.swing.JButton();
        cyan = new javax.swing.JButton();
        blue = new javax.swing.JButton();
        x3 = new javax.swing.JLabel();
        x1 = new javax.swing.JLabel();
        x2 = new javax.swing.JLabel();

        javax.swing.GroupLayout jFrame1Layout = new javax.swing.GroupLayout(jFrame1.getContentPane());
        jFrame1.getContentPane().setLayout(jFrame1Layout);
        jFrame1Layout.setHorizontalGroup(
            jFrame1Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGap(0, 400, Short.MAX_VALUE)
        );
        jFrame1Layout.setVerticalGroup(
            jFrame1Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGap(0, 300, Short.MAX_VALUE)
        );

        setDefaultCloseOperation(javax.swing.WindowConstants.EXIT_ON_CLOSE);
        setResizable(false);

        jPanel1.setBackground(new java.awt.Color(12, 12, 12));

        red.setBackground(new java.awt.Color(89, 0, 0));
        red.setCursor(new java.awt.Cursor(java.awt.Cursor.HAND_CURSOR));
        red.setPreferredSize(new java.awt.Dimension(150, 150));
        red.addMouseListener(new java.awt.event.MouseAdapter() {
            public void mousePressed(java.awt.event.MouseEvent evt) {
                redMousePressed(evt);
            }
            public void mouseReleased(java.awt.event.MouseEvent evt) {
                redMouseReleased(evt);
            }
        });
        red.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                redActionPerformed(evt);
            }
        });

        orange.setBackground(new java.awt.Color(89, 35, 0));
        orange.setCursor(new java.awt.Cursor(java.awt.Cursor.HAND_CURSOR));
        orange.setPreferredSize(new java.awt.Dimension(150, 150));
        orange.addMouseListener(new java.awt.event.MouseAdapter() {
            public void mousePressed(java.awt.event.MouseEvent evt) {
                orangeMousePressed(evt);
            }
            public void mouseReleased(java.awt.event.MouseEvent evt) {
                orangeMouseReleased(evt);
            }
        });
        orange.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                orangeActionPerformed(evt);
            }
        });

        green.setBackground(new java.awt.Color(0, 89, 16));
        green.setCursor(new java.awt.Cursor(java.awt.Cursor.HAND_CURSOR));
        green.setPreferredSize(new java.awt.Dimension(150, 150));
        green.addMouseListener(new java.awt.event.MouseAdapter() {
            public void mousePressed(java.awt.event.MouseEvent evt) {
                greenMousePressed(evt);
            }
            public void mouseReleased(java.awt.event.MouseEvent evt) {
                greenMouseReleased(evt);
            }
        });
        green.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                greenActionPerformed(evt);
            }
        });

        leaf.setBackground(new java.awt.Color(66, 89, 21));
        leaf.setCursor(new java.awt.Cursor(java.awt.Cursor.HAND_CURSOR));
        leaf.setPreferredSize(new java.awt.Dimension(150, 150));
        leaf.addMouseListener(new java.awt.event.MouseAdapter() {
            public void mousePressed(java.awt.event.MouseEvent evt) {
                leafMousePressed(evt);
            }
            public void mouseReleased(java.awt.event.MouseEvent evt) {
                leafMouseReleased(evt);
            }
        });
        leaf.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                leafActionPerformed(evt);
            }
        });

        grey.setBackground(new java.awt.Color(89, 78, 59));
        grey.setCursor(new java.awt.Cursor(java.awt.Cursor.HAND_CURSOR));
        grey.setPreferredSize(new java.awt.Dimension(150, 150));
        grey.addMouseListener(new java.awt.event.MouseAdapter() {
            public void mousePressed(java.awt.event.MouseEvent evt) {
                greyMousePressed(evt);
            }
            public void mouseReleased(java.awt.event.MouseEvent evt) {
                greyMouseReleased(evt);
            }
        });
        grey.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                greyActionPerformed(evt);
            }
        });

        pink.setBackground(new java.awt.Color(89, 0, 89));
        pink.setCursor(new java.awt.Cursor(java.awt.Cursor.HAND_CURSOR));
        pink.setPreferredSize(new java.awt.Dimension(150, 150));
        pink.addMouseListener(new java.awt.event.MouseAdapter() {
            public void mousePressed(java.awt.event.MouseEvent evt) {
                pinkMousePressed(evt);
            }
            public void mouseReleased(java.awt.event.MouseEvent evt) {
                pinkMouseReleased(evt);
            }
        });
        pink.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                pinkActionPerformed(evt);
            }
        });

        yellow.setBackground(new java.awt.Color(89, 89, 0));
        yellow.setCursor(new java.awt.Cursor(java.awt.Cursor.HAND_CURSOR));
        yellow.setPreferredSize(new java.awt.Dimension(150, 150));
        yellow.addMouseListener(new java.awt.event.MouseAdapter() {
            public void mousePressed(java.awt.event.MouseEvent evt) {
                yellowMousePressed(evt);
            }
            public void mouseReleased(java.awt.event.MouseEvent evt) {
                yellowMouseReleased(evt);
            }
        });
        yellow.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                yellowActionPerformed(evt);
            }
        });

        cyan.setBackground(new java.awt.Color(0, 89, 71));
        cyan.setCursor(new java.awt.Cursor(java.awt.Cursor.HAND_CURSOR));
        cyan.setPreferredSize(new java.awt.Dimension(150, 150));
        cyan.addMouseListener(new java.awt.event.MouseAdapter() {
            public void mousePressed(java.awt.event.MouseEvent evt) {
                cyanMousePressed(evt);
            }
            public void mouseReleased(java.awt.event.MouseEvent evt) {
                cyanMouseReleased(evt);
            }
        });
        cyan.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                cyanActionPerformed(evt);
            }
        });

        blue.setBackground(new java.awt.Color(0, 0, 89));
        blue.setCursor(new java.awt.Cursor(java.awt.Cursor.HAND_CURSOR));
        blue.setPreferredSize(new java.awt.Dimension(150, 150));
        blue.addMouseListener(new java.awt.event.MouseAdapter() {
            public void mousePressed(java.awt.event.MouseEvent evt) {
                blueMousePressed(evt);
            }
            public void mouseReleased(java.awt.event.MouseEvent evt) {
                blueMouseReleased(evt);
            }
        });
        blue.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                blueActionPerformed(evt);
            }
        });

        x3.setFont(new java.awt.Font("Segoe UI", 0, 100)); // NOI18N
        x3.setForeground(new java.awt.Color(255, 255, 255));
        x3.setText("X");

        x1.setFont(new java.awt.Font("Segoe UI", 0, 100)); // NOI18N
        x1.setForeground(new java.awt.Color(255, 255, 255));
        x1.setText("X");

        x2.setFont(new java.awt.Font("Segoe UI", 0, 100)); // NOI18N
        x2.setForeground(new java.awt.Color(255, 255, 255));
        x2.setText("X");

        javax.swing.GroupLayout jPanel1Layout = new javax.swing.GroupLayout(jPanel1);
        jPanel1.setLayout(jPanel1Layout);
        jPanel1Layout.setHorizontalGroup(
            jPanel1Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(jPanel1Layout.createSequentialGroup()
                .addGroup(jPanel1Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                    .addGroup(jPanel1Layout.createSequentialGroup()
                        .addContainerGap()
                        .addGroup(jPanel1Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                            .addGroup(javax.swing.GroupLayout.Alignment.TRAILING, jPanel1Layout.createSequentialGroup()
                                .addComponent(green, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                                .addGap(18, 18, 18)
                                .addComponent(orange, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED, 20, Short.MAX_VALUE)
                                .addComponent(red, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE))
                            .addGroup(javax.swing.GroupLayout.Alignment.TRAILING, jPanel1Layout.createSequentialGroup()
                                .addComponent(leaf, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                                .addGap(18, 18, 18)
                                .addComponent(grey, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED, javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)
                                .addComponent(pink, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE))
                            .addGroup(jPanel1Layout.createSequentialGroup()
                                .addComponent(yellow, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                                .addGap(18, 18, 18)
                                .addComponent(cyan, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED, javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)
                                .addComponent(blue, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE))))
                    .addGroup(jPanel1Layout.createSequentialGroup()
                        .addGap(134, 134, 134)
                        .addComponent(x1)
                        .addGap(27, 27, 27)
                        .addComponent(x2)
                        .addGap(27, 27, 27)
                        .addComponent(x3)
                        .addGap(0, 0, Short.MAX_VALUE)))
                .addContainerGap())
        );
        jPanel1Layout.setVerticalGroup(
            jPanel1Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(jPanel1Layout.createSequentialGroup()
                .addContainerGap(javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)
                .addGroup(jPanel1Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                    .addComponent(green, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                    .addComponent(orange, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                    .addComponent(red, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE))
                .addGap(18, 18, 18)
                .addGroup(jPanel1Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                    .addComponent(leaf, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                    .addComponent(grey, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                    .addComponent(pink, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE))
                .addGap(18, 18, 18)
                .addGroup(jPanel1Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                    .addComponent(yellow, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                    .addComponent(cyan, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                    .addComponent(blue, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE))
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                .addGroup(jPanel1Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                    .addComponent(x3, javax.swing.GroupLayout.PREFERRED_SIZE, 98, javax.swing.GroupLayout.PREFERRED_SIZE)
                    .addComponent(x1, javax.swing.GroupLayout.PREFERRED_SIZE, 99, javax.swing.GroupLayout.PREFERRED_SIZE)
                    .addComponent(x2, javax.swing.GroupLayout.PREFERRED_SIZE, 98, javax.swing.GroupLayout.PREFERRED_SIZE))
                .addContainerGap())
        );

        javax.swing.GroupLayout layout = new javax.swing.GroupLayout(getContentPane());
        getContentPane().setLayout(layout);
        layout.setHorizontalGroup(
            layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addComponent(jPanel1, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
        );
        layout.setVerticalGroup(
            layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addComponent(jPanel1, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
        );

        pack();
    }// </editor-fold>//GEN-END:initComponents

    boolean focus;
    int[] colorOrder = new int[0];
    int order = 0;
    int color, present = 0, strike = 0;
    SimonSaysOrder obj = new SimonSaysOrder();
    
    public void randomColor() {
        color = (int)(Math.random() * 9) + 1;
        order++;
        colorOrder = Arrays.copyOf(colorOrder, order);
        colorOrder[order-1] = color;
        showOrder();
        
    }
    
    public void bright() {
        green.setBackground(new Color(0, 255, 49));
        orange.setBackground(new Color(255, 101, 0));
        red.setBackground(new Color(255, 0, 0));
        leaf.setBackground(new Color(190,255,61));
        grey.setBackground(new Color(255,222,169));
        pink.setBackground(new Color(255,0,255));
        yellow.setBackground(new Color(255,255,0));
        cyan.setBackground(new Color(0,255,202));
        blue.setBackground(new Color(0,0,255));
    }
    
    public void dim() {
        green.setBackground(new Color(0,89,16));
        orange.setBackground(new Color(89,35,0));
        red.setBackground(new Color(89,0,0));
        leaf.setBackground(new Color(66,89,21));
        grey.setBackground(new Color(89,78,59));
        pink.setBackground(new Color(89,0,89));
        yellow.setBackground(new Color(89,89,0));
        cyan.setBackground(new Color(0,89,71));
        blue.setBackground(new Color(0,0,89));
    }
    
    public void flash(int i) {
        switch (colorOrder[i]) {
            case 1:
                green.setBackground(new Color(0, 255, 49));
                break;
            case 2:
                orange.setBackground(new Color(255, 101, 0));
                break;
            case 3:
                red.setBackground(new Color(255, 0, 0));
                break;
            case 4:
                leaf.setBackground(new Color(190,255,61));
                break;
            case 5:
                grey.setBackground(new Color(255,222,169));
                break;
            case 6:
                pink.setBackground(new Color(255,0,255));
                break;
            case 7:
                yellow.setBackground(new Color(255,255,0));
                break;
            case 8:
                cyan.setBackground(new Color(0,255,202));
                break;
            case 9:
                blue.setBackground(new Color(0,0,255));
        }
    }
    
    public void clicked(int num) {
        hideOrder();
        if (colorOrder[present] == num) {
            present++;
            if (present >= colorOrder.length) {
                present = 0;
                randomColor();
            }
        } else {
            strike++;
            showOrder();
            switch (strike) {
                case 1:
                    x1.setForeground(Color.red);
                    break;
                case 2:
                    x2.setForeground(Color.red);
                    break;
                case 3:
                    x3.setForeground(Color.red);
                    JOptionPane.showMessageDialog(null, "Game Over!\n\nScore: " + (colorOrder.length - 1));
                    System.exit(0);
            }
            present = 0;
        }
    }
    
    public void showOrder() {
        obj.setVisible(true);
        obj.setTxtOrder(colorOrder);
    }
    
    public void hideOrder() {
        obj.setVisible(false);
    }
    
    private void greenActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_greenActionPerformed
        clicked(1);
    }//GEN-LAST:event_greenActionPerformed

    private void orangeActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_orangeActionPerformed
        clicked(2);
    }//GEN-LAST:event_orangeActionPerformed

    private void redActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_redActionPerformed
        clicked(3);
    }//GEN-LAST:event_redActionPerformed

    private void leafActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_leafActionPerformed
        clicked(4);
    }//GEN-LAST:event_leafActionPerformed

    private void greyActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_greyActionPerformed
        clicked(5);
    }//GEN-LAST:event_greyActionPerformed

    private void pinkActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_pinkActionPerformed
        clicked(6);
    }//GEN-LAST:event_pinkActionPerformed

    private void yellowActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_yellowActionPerformed
        clicked(7);
    }//GEN-LAST:event_yellowActionPerformed

    private void cyanActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_cyanActionPerformed
        clicked(8);
    }//GEN-LAST:event_cyanActionPerformed

    private void blueActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_blueActionPerformed
        clicked(9);
    }//GEN-LAST:event_blueActionPerformed

    private void greenMousePressed(java.awt.event.MouseEvent evt) {//GEN-FIRST:event_greenMousePressed
        green.setBackground(new Color(0,255,49));
    }//GEN-LAST:event_greenMousePressed

    private void greenMouseReleased(java.awt.event.MouseEvent evt) {//GEN-FIRST:event_greenMouseReleased
        green.setBackground(new Color(0,89,16));
    }//GEN-LAST:event_greenMouseReleased

    private void orangeMousePressed(java.awt.event.MouseEvent evt) {//GEN-FIRST:event_orangeMousePressed
        orange.setBackground(new Color(255,101,0));
    }//GEN-LAST:event_orangeMousePressed

    private void orangeMouseReleased(java.awt.event.MouseEvent evt) {//GEN-FIRST:event_orangeMouseReleased
        orange.setBackground(new Color(89,35,0));
    }//GEN-LAST:event_orangeMouseReleased

    private void redMousePressed(java.awt.event.MouseEvent evt) {//GEN-FIRST:event_redMousePressed
        red.setBackground(new Color(255,0,0));
    }//GEN-LAST:event_redMousePressed

    private void redMouseReleased(java.awt.event.MouseEvent evt) {//GEN-FIRST:event_redMouseReleased
        red.setBackground(new Color(89,0,0));
    }//GEN-LAST:event_redMouseReleased

    private void leafMousePressed(java.awt.event.MouseEvent evt) {//GEN-FIRST:event_leafMousePressed
        leaf.setBackground(new Color(190,255,61));
    }//GEN-LAST:event_leafMousePressed

    private void leafMouseReleased(java.awt.event.MouseEvent evt) {//GEN-FIRST:event_leafMouseReleased
        leaf.setBackground(new Color(66,89,21));
    }//GEN-LAST:event_leafMouseReleased

    private void greyMousePressed(java.awt.event.MouseEvent evt) {//GEN-FIRST:event_greyMousePressed
        grey.setBackground(new Color(255,222,169));
    }//GEN-LAST:event_greyMousePressed

    private void greyMouseReleased(java.awt.event.MouseEvent evt) {//GEN-FIRST:event_greyMouseReleased
        grey.setBackground(new Color(89,78,59));
    }//GEN-LAST:event_greyMouseReleased

    private void pinkMousePressed(java.awt.event.MouseEvent evt) {//GEN-FIRST:event_pinkMousePressed
        pink.setBackground(new Color(255,0,255));
    }//GEN-LAST:event_pinkMousePressed

    private void pinkMouseReleased(java.awt.event.MouseEvent evt) {//GEN-FIRST:event_pinkMouseReleased
        pink.setBackground(new Color(89,0,89));
    }//GEN-LAST:event_pinkMouseReleased

    private void yellowMousePressed(java.awt.event.MouseEvent evt) {//GEN-FIRST:event_yellowMousePressed
        yellow.setBackground(new Color(255,255,0));
    }//GEN-LAST:event_yellowMousePressed

    private void yellowMouseReleased(java.awt.event.MouseEvent evt) {//GEN-FIRST:event_yellowMouseReleased
        yellow.setBackground(new Color(89,89,0));
    }//GEN-LAST:event_yellowMouseReleased

    private void cyanMousePressed(java.awt.event.MouseEvent evt) {//GEN-FIRST:event_cyanMousePressed
        cyan.setBackground(new Color(0,255,202));
    }//GEN-LAST:event_cyanMousePressed

    private void cyanMouseReleased(java.awt.event.MouseEvent evt) {//GEN-FIRST:event_cyanMouseReleased
        cyan.setBackground(new Color(0,89,71));
    }//GEN-LAST:event_cyanMouseReleased

    private void blueMousePressed(java.awt.event.MouseEvent evt) {//GEN-FIRST:event_blueMousePressed
        blue.setBackground(new Color(0,0,255));
    }//GEN-LAST:event_blueMousePressed

    private void blueMouseReleased(java.awt.event.MouseEvent evt) {//GEN-FIRST:event_blueMouseReleased
        blue.setBackground(new Color(0,0,89));
    }//GEN-LAST:event_blueMouseReleased

    /**
     * @param args the command line arguments
     * @throws java.lang.InterruptedException
     */
    public static void main(String args[]) {
        /* Set the Nimbus look and feel */
        //<editor-fold defaultstate="collapsed" desc=" Look and feel setting code (optional) ">
        /* If Nimbus (introduced in Java SE 6) is not available, stay with the default look and feel.
         * For details see http://download.oracle.com/javase/tutorial/uiswing/lookandfeel/plaf.html 
         */
        try {
            for (javax.swing.UIManager.LookAndFeelInfo info : javax.swing.UIManager.getInstalledLookAndFeels()) {
                if ("Nimbus".equals(info.getName())) {
                    javax.swing.UIManager.setLookAndFeel(info.getClassName());
                    break;
                }
            }
        } catch (ClassNotFoundException ex) {
            java.util.logging.Logger.getLogger(SimonSays.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        } catch (InstantiationException ex) {
            java.util.logging.Logger.getLogger(SimonSays.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        } catch (IllegalAccessException ex) {
            java.util.logging.Logger.getLogger(SimonSays.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        } catch (javax.swing.UnsupportedLookAndFeelException ex) {
            java.util.logging.Logger.getLogger(SimonSays.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        }
        //</editor-fold>
        
        /* Create and display the form */
        java.awt.EventQueue.invokeLater(new Runnable() {
            public void run() {
                new SimonSays().setVisible(true);
            }
        });
        
    }

    // Variables declaration - do not modify//GEN-BEGIN:variables
    private javax.swing.JButton blue;
    private javax.swing.JButton cyan;
    private javax.swing.JButton green;
    private javax.swing.JButton grey;
    private javax.swing.JFrame jFrame1;
    private javax.swing.JPanel jPanel1;
    private javax.swing.JButton leaf;
    private javax.swing.JButton orange;
    private javax.swing.JButton pink;
    private javax.swing.JButton red;
    private javax.swing.JLabel x1;
    private javax.swing.JLabel x2;
    private javax.swing.JLabel x3;
    private javax.swing.JButton yellow;
    // End of variables declaration//GEN-END:variables
}
