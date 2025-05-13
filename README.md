# testing_poc_project

Tech Stack used :-

    1. Language: Python 3                           --> Core language use to write the step defination code.

    2. PIP                                          --> Package manager for Python, use to install the different python packages.

    3. Behave                                       --> BDD test framework (like Cucumber) used for Python.

    4. HTTP Client: requests                        --> Web services which we are targeting to Automate and test.

    5. Reporting: Allure                            --> Used to do the reporting after the automation test execution.

    6. Containerization: Docker                     -->

    7. CI/CD: Azure DevOps or GitLab                -->

-----------------------------------------------------------------------------------------------------------------------

Project folder structure:-

        automation_testing/
        │
        ├── features/
        │   ├── create_update_booking.feature
        │   ├── get_booking_details.feature
        │   ├── get_booking_id.feature
        │   ├── steps/
        │   │   └── create_update_booking_steps.py
        │   │   └── get_booking_details.py
        │   │   └── get_booking_id_steps.py
        │   └── environment.py
        ├── utils/
        │   └── api_helpers.py
        ├── requirements.txt
        ├── README.md

-----------------------------------------------------------------------------------------------------------------------

Steps completed :-

    1. Task must be implemented using Bhave & Python programming language       --> COMPLETED
    2. Ensure the test execution report is generated.                           --> COMPLETED
    3. Utilize Scenario Outline in Cucumber to define scenarios with examples.  --> COMPLETED
    4. Dockerize the test Cases                                                 -->
    5. Execute the tests In Pipeline Azure or Gitlab                            -->
    6. Upload the completed code to GitHub along with a README file.            --> COMPLETED
    7. Share the GitHub repository link for review.                             --> COMPLETED

-----------------------------------------------------------------------------------------------------------------------

Steps to execute the Project :- 

    1. Download the code from Giithub repository 'https://github.com/SauravSuin/automation_testing.git'.
    2. Open Visual Studio Code. Go to File --> Open folder --> Select the project folder which is downloaded from GitHub.
    3. Once open the project folder structure displayed.
    4. Before doing the execution you need to install all the prerequsite setup.
    5. Once it's done open a terminal in VS code. By clicking (...) present in the top --> Clik on Terminal --> Click new terminal.
    5. In terminal you should be there in the project root folder, if you are not in root folder then go to root folder by using CD command.
    6. Once you are in root folder then execute below mentioned command.
        behave -f allure_behave.formatter:AllureFormatter -o allure-results ./features
        allure serve allure-results
    7. Once the command executed successfully Allure report will open automatically in your browser.
    8. In report your are able to see the test result and you should also able to expand and explore the result output.

-----------------------------------------------------------------------------------------------------------------------

Installation of all the component :-

1. Install Python :-
    a. Dowload python form <https://www.python.org/downloads/>
    b. While the installation make sure you can check the option of adding python to environment variable.
    c. After the installation verify if the python is installed or not, for that run your command prompt as admin and type the below command which will display the verson details. of python and PIP (PAckage Manager for Python packages).
        1. python --version
        2. pip --version

-----------------------------------------------------------------------------------------------------------------------

2. Install required python packages :- by executing below command
    a. pip install behave request allure-behave

-----------------------------------------------------------------------------------------------------------------------

3. We need to install behave an Allure - It can be done by below two methods :-
    a. Open your cmd prompt in admin mode andexecute the command -
        1. pip install behave
        2. pip install allure-behave

    Once it's install you can go and verify it if it is installed properly or not, to check that execute below mentioned cmd :-
        1. behave --version
        2. allure --version

    If version number displayed that means it is installed properly.

    b. Create a "requirements.txt" file and put all the required setup in it and then execute the 'pip install' command by passing the text file.
        1. Create a "requirements.txt" file add the below entries in it :-
            behave
            allure-behave

        2. Execute the pip command.
            pip install -r requirements.txt

-----------------------------------------------------------------------------------------------------------------------

4. Installl Allure CLI (Command Line Tool) :-
    a. Download Allure from: <https://github.com/allure-framework/allure2/releases>
    b. Extract the ZIP.
    c. Add the bin directory (e.g., C:\allure\bin) to your System PATH
    d. Test if installed by executing "allure --version"

    -- Install using Scoop :-
    a. If Scoop isn't installed :- Open power shell as Admin and run below command -
        Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
        iwr -useb get.scoop.sh | iex

    b. Then install Allure:- b yexecuting below command
        scoop install allure

-----------------------------------------------------------------------------------------------------------------------

5. Create a Sample Test :- Inside the features folder. i.e. 'features/example.feature
    This can be written in 'Gherkin' laguage. Or we can say we can create the feature fie which will be considered as test case.
    We can create mulltipe feature files.

    eg:- Feature: Example
            Scenario: Simple API check
                Giver <Input or prerequisiet>
                When  <Step logic which will execute the main process as per the functionality mentioned like create order, create booking, get the details etc.>
                Then  <It should be the output which we received from the 2nd step, like for services if response code is 200 means it is successful, also we can capture the desired result>

@booking
Feature: Booking API
  
  @create_booking
  Scenario Outline: Successfully create a new booking
    Given I have booking data with "<firstname>", "<lastname>", "<price>", "<deposit>", "<checkin>", "<checkout>", "<additionalneeds>"
    When I send a create booking request
    Then the response code should be 200
    And the booking ID should be present in the response

    Examples:
      | firstname | lastname | price | deposit | checkin    | checkout   | additionalneeds |
      | Sam       | sui      |   500 | true    | 2025-05-12 | 2025-05-20 | Breakfast       |
      | suin      | sam      |   150 | false   | 2025-06-10 | 2025-06-15 | Breakfast       |

  @get_booking_id
  Scenario: Fetch all booking IDs
    When I send a GET request to the booking IDs endpoint
    Then the response status code should be 200
    And the response should contain a list of booking IDs

1. Scenario Outline: We can use this when we need to run the same test with different input valuse, or          perametrized values. We called it data driven testing. And the different perametrized value is defined in Example section.
In our scenario we are calling POST service which is used to created different booking data according to different input values like firstname, lastname, price, checkin time, checkout time, additional service.

2. Scenario: It can be used to execute single test case with fixed values. In our case we are calling GET service to fetch the data, so we just need to call service url which is fixed and after execution we are going to receive the different data in list.

-----------------------------------------------------------------------------------------------------------------------

6. Create a step defination :- Which comprise or hold the functional logic of the transaction or process which user try to automate, like if it is creating order then how we are creating the order that logic can be written here using different programing languages like C#, Python, Java Script etc.

        features/steps/example_steps.py :- 


        from behave import given, then
        import requests

        @given('I call a sample API')
        def step_impl(context):
            context.response = requests.get("https://api.github.com")

        @then('the response status should be 200')
        def step_impl(context):
            assert context.response.status_code == 200

-----------------------------------------------------------------------------------------------------------------------

7. Run Test & Generate Allure Report :-

    a. Run behave tests with Allure formatter:- by executing the below command

        behave -f allure_behave.formatter:AllureFormatter -o allure-results

    b. Generate HTML report:-

        allure generate allure-results -o allure-report --clean

    c. View the report :-

        allure open allure-report

    Allure Reporting :- After test run :-

        allure generate allure-results -o allure-report --clean
        allure open allure-report

-----------------------------------------------------------------------------------------------------------------------

8. We can execute the below command in Terminald and it will run the behave test and generated & open the report in browser :-

NOTE :- Make Sure we can run this command in test 'ROOT' folder (i.e. Projects Root folder).
        e.g. :- C:\Users\Desktop\GIT Repo\automation_testing\automation_testing>

        behave -f allure_behave.formatter:AllureFormatter -o allure-results ./features
        allure serve allure-results

        OR

        behave -f allure_behave.formatter:AllureFormatter -o allure-results ./features
        allure generate allure-results -o allure-report --clean
        allure open allure-report

Explain above command :- 
        1. behave -f allure_behave.formatter:AllureFormatter -o allure-results ./features
            a. behave --> Runs BDD-style test cases written in .feature files.
            b. -f allure_behave.formatter:AllureFormatter --> Tells Behave to format the output as Allure-compatible results.
            c. -o allure-results --> Output the result files into the allure-results/ folder.
            d. ./features --> Specifies where .feature files are located.

        After this runs, you’ll have raw test result files (*.json, *.txt) in the allure-results/ folder. 
        These are not human-readable yet.

        2. allure generate allure-results -o allure-report --clean
            a. allure generate --> Uses the Allure CLI to convert raw test data into a beautiful HTML report.
            b. allure-results --> Source directory that contains the raw output generated by Behave after execution of 1st query.
            c. -o allure-report --> Output the final report (HTML, JS, CSS files) into the allure-report/ directory.
            d. --clean --> Deletes old contents in the allure-report/ directory before generating a new report.

        3. allure open allure-report
            a. allure open --> Launches a temporary local web server and opens the report in your default browser.
            b. allure-report --> Points to the folder containing the static HTML report.


-----------------------------------------------------------------------------------------------------------------------
