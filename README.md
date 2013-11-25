Facebook-Hacker-Cup-2014-Qualification-Round
============================================

Facebook Hacker Cup 2014 Qualification Round Solutions 

URL: https://www.facebook.com/hackercup/problems.php?pid=318555664954399&amp;round=598486203541358
There were three problems for the Qualification Round. As per facebook, any participant who were able to succedd in any of the problems would be able to qualify for the next round.

Because of Licensing issue, I will Just provide links to the Problem statement rather than quoting the questions 

Problem 1:
    Square Detector: Carried 20 marks
    URL: https://www.facebook.com/hackercup/problems.php?pid=318555664954399&round=598486203541358
    Approach:
    Example Input:
    
        .......
        ..##...
        ..##...
        .......
        .##....
        .##....
        .......
        
    Step 1: Scan and Skip the lines until the first occurance of '#' 
    
        -SKIP- .......
        --->   ..##...
               ..##...
               .......
               .##....    
               .##....
               .......
               
    
    Step 2: Scan and Select until you encounter the first line without a '#'

        -SKIP- .......
        -SEL-- ..##...
        -SEL-- ..##...
        -----> .......
               .##....   
               .##....
               .......

    Step 3: Scan and Skip until you encounter the line with a '#'. If you encounter the line, StopIterating.               

        -SKIP- .......
        -SEL-- ..##...
        -SEL-- ..##...
        -SKIP- .......
        -----> .##....   
               .##....
               .......
    
    Step 4: Invert the Selected Lines.
    
        -SEL-- ..##...            -SEL-- ..
        -SEL-- ..##...  =====>    -SEL-- ..
                                  -SEL-- ##
                                  -SEL-- ##
                                  -SEL-- ..
                                  -SEL-- ..
                                  -SEL-- ..
    
    Step 5: Redo Step 1 .. 3 with the new selected list
    
        -SKIP- ..
        -SKIP- ..
        -SEL-- ##
        -SEL-- ##
        -SKIP- ..
        -SKIP- ..
        -SKIP- ..
        
    Step 6: Check if the selected lines makes a perfect square and if the grid contains any '.'
    
    
Problem 2:     
    Basketball Game: Carried 35 marks
    URL: https://www.facebook.com/hackercup/problems.php?pid=740733162607577&round=598486203541358

    Approach:
    
    The Solution file is commented enough to highlight the approach 
    
Problem 3:
    Tennison: Carried 45 marks
    URL: https://www.facebook.com/hackercup/problems.php?pid=373965339404375&round=598486203541358
    
    Approach:
    
    My inital approach uses Dynamic Programming but the approach shared by facebook is eaier to implement
    as it uses recursion with memorization. The Facebook page 
    URL :https://www.facebook.com/notes/facebook-hacker-cup/2014-qualification-round-solutions/775180192497884
    has a wonderful explanation of the approach. I have two implementation in this branch.
    1. Tennison.py: The one I submitted using DP
    2. Tennsion_FB_Version.py: Based on the approach shared by FB

    
