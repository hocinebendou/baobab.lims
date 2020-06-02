*** Settings ***
Suite Setup       Start browser
Suite Teardown    Close All Browsers
Library           BuiltIn
Library           Selenium2Library    timeout=5    implicit_wait=0.3
Library           String
Resource          ../../keywords.txt
Resource          plone/app/robotframework/selenium.robot
Library           Remote    ${PLONEURL}/RobotRemote
Variables         plone/app/testing/interfaces.py
Variables         ../../variables.py
Library           DebugLibrary

*** Variables ***

${USER_ROLE}  LabManager
${USER}  admin
${PASSWORD}    secret

*** Test Cases ***
LAB SETTINGS SETUP
    #Enable autologin as     ${USER_ROLE}
    Login    ${USER}    ${PASSWORD}
    LAB Settings Links
    Adding Valid Lab Default Settings
    Adding Invalid Lab Default Settings
    Adding Valid Lab Contact
    Adding InValid Lab Contact
    #@Todo: Password Activation Process
    Add Valid Department
    Add InValid Department
    
*** Keywords ***
LAB Settings Links
    Go to    ${PLONEURL}/@@overview-controlpanel
    wait until page contains   Configuration area for Plone and add-on Products.
    Go to    ${PLONEURL}/bika_setup/laboratory/base_edit    
    wait until page contains   Laboratory Supervisor
    
Default Lab Form Parameters   
    Input Text    TaxNumber    123456777
    Input Text    Phone    0214454441
    Input Text    Fax    0214454442
    #select from dropdown    css=#LaboratorySupervisor    »Lab » Manager
    #Input Text    LaboratoryLicenseID    ID456724RDEE

Adding Valid Lab Default Settings  
    LAB Settings Links
    Input Text    Name    Test Laboratory
    Default Lab Form Parameters
    Click Button    Save
    wait until page contains    Changes saved.
    Go to    ${PLONEURL}/bika_setup/laboratory/base_edit
    
Default Lab Contact Form Parameters
    Input Text    Salutation    Dr
    Input Text    Middleinitial    DD
    Input Text    Middlename    Elizabeth
    Input Text    Surname    Johnson
    Input Text    JobTitle    Technician
    
Adding Valid Lab Contact
    Go to    ${PLONEURL}/bika_setup/bika_labcontacts    
    wait until page contains   Lab Contacts
    Click link    Add
    wait until page contains   Add Lab Contact
    Input Text    Firstname    Dominique    
    Default Lab Contact Form Parameters
    Click Button    Save
    wait until page contains    Changes saved.
    Adding Valid Login Details
    Adding InValid Login Details

Adding InValid Lab Contact
    Go to    ${PLONEURL}/bika_setup/bika_labcontacts    
    wait until page contains   Lab Contacts
    Click link    Add
    wait until page contains   Add Lab Contact
    Input Text    Firstname    ${EMPTY}    
    Default Lab Contact Form Parameters
    Click Button    Save
    wait until page contains    Please correct the indicated errors.

Adding Invalid Lab Default Settings  
    LAB Settings Links
    Input Text    Name    ${EMPTY}
    Default Lab Form Parameters
    Click Button    Save
    wait until page contains    Please correct the indicated errors.
    Go to    ${PLONEURL}/bika_setup/laboratory/base_edit

Login Form Details
    Input Password    password    secretuser
    Input Password    confirm    secretuser
    Input Text    email    dominiqueuser@test.co.za
    Select From List     name=groups    LabManagers

Adding Valid Login Details
    click element    //a[text()='Login details']
    wait until page contains    Create a new User
    Input Text    username    dominique_user
    Login Form Details
    Click Button    Save
    wait until page contains    SMTP server disconnected. User creation aborted.
 
Adding InValid Login Details
    click element    //a[text()='Login details']
    wait until page contains    Create a new User
    Input Text    username    ${EMPTY}
    Login Form Details
    Click Button    Save
    wait until page contains    username: Input is required but not given.
         
Add Valid Department
    Go to    ${PLONEURL}/bika_setup/bika_departments
    wait until page contains   Lab Departments
    Click link    Add
    Input Text    title    My Test Department
    Department Form Details
    Click Button    Save
    wait until page contains    Changes saved.
    Go To    ${PLONEURL}/bika_setup/bika_departments
    wait until page contains   My Test Department
    
Add InValid Department
    Go to    ${PLONEURL}/bika_setup/bika_departments
    wait until page contains   Lab Departments
    Click link    Add
    Input Text    title    ${EMPTY}
    Department Form Details
    Click Button    Save
    wait until page contains    Please correct the indicated errors.
    
Department Form Details
    Input Text    description    The Baobab LIMS Test Department 
    #select from dropdown    Manager:list    Dominique Elizabeth Johnson

Start browser
    Open browser    ${PLONEURL}    chrome
    Set selenium speed    ${SELENIUM_SPEED}