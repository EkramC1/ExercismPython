### My Learning Notes 
## What I Learned From the Exercises

### **Learning Exercises**

### (1) hello-world
* **Syntax:** How to use the "print()" function to output text.
* **Strings:** Text must always be enclosed in quotes ("TEXT").

### (2) guidos-gorgeous-lasagna
* **Constants:** Fixed values that never change must be written in ALL CAPS.
* **Linkage:** Functions can call other functions.
* **Docstrings:** """Description""" under def shows as help text for documentation.

### (3) ghost-gobble-arcade-game
* **Booleans:** Applied the theory of truth values (True/False) in a practical way. Solved logical conditions (like in the Pac-Man exercise) compactly using and, or, and not operators directly via return.

### (4) currency-exchange
**Python Math & Data Types:**
* int and float
* **% Modulo:** Calculates only the remainder of a division ( 7 % 4 results in 3, because 3 is what is left over).
* **// Floor Division:** Divides two numbers and chops off everything after the decimal point ( 7 // 4 results in 1, would result in 1.75 in a normal division).

    * After analyzing the code of others, I realized that I could shorten the docstrings. Also, I noticed that others write the last function differently than I did. Their version was much shorter, and they used better       variable names, which made the code cleaner and still successful. Mine is a clear and easy understandable documentation. I still want to try their version in the next exercices.
      
      * **Automation**: Documentation tools (like Sphinx) read these tags to automatically generate nice PDF manuals or project websites.
      * **The Job Value ("Hover" Effect)**
        * **Teamwork**: colleagues can see exactly what your function expects without reading your actual code line-by-line.
        * **The Hover Feature**: When typing a function in an editor (f.e. VS Code), these **:param** descriptions automatically pop up in a floating info window saving tons of time.
 * :param parameter_name : Data Type - explanation.
 * :return : Data Type - explanation.

### (5) Meltdown Mitigation
* If, elif, else
* Narrowest condition on top!
   * the code is read from top to bottom. As soon as one condition is met, Python stops checking the rest. Therefore, I have to check the extreme danger category first, then checking the general warning category below it.
* Percentages are Decimals: To use percentages in the code, I must always convert them into decimals by shifting the decimal point **two places to the left** (:100)
   * 90% of x is (0.9 * x)
   * 110% of x is (1.1 * x)
