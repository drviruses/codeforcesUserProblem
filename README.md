      # codeforcesUserProblem
      This is a simple web scrapping project where you can know the problems that the user
      did, when he 
      was in like Pupil, Specialist, .. etc phases.
      
      
1. Clone / Download this repository.
2. Download [chromedriver](https://chromedriver.chromium.org/downloads) from and place it in the current location.
3. Run `pip install selenium` if you do not have that already.
4. Run `python problem.py`.
5. For Video Demonstration .[Video](https://drive.google.com/file/d/1mjmzozjZTmIItNk5lhcbncDXSrdFbXXc/view?usp=sharing)
      
            So You just have to download the python file install ChromeWebdriver in the same 
            directory and selinium in 
            your system and run the pyhon code and enter the 
            user Id of the user of which you want want to know the problems he solved when he
            was newbie, pupil, expert, etc.

            You just have set the starting page and the ending page of his submission that 
            is official.
            
            For setting the strting page you just have to change the variable named "cur" 
            at line number 31 
            
            For setting the ending page and this will be lesser than the starting 
            page because we are going 
            backwards, the variable named as "totPages" at line 14

            While Executing the code it will ask you the uderId and the Rating status.
            And after that it will create a CSV file of name ProblemList.csv in 
            the same directory 
            with Name and Link of the Problem as well.


            I will keep on updating it.
            Thank You.
