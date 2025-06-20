This is a Configurable Automated Testing application that uses Python, Selenium and Excel. 
    PyTest: pip install pytest
    html reports: pip install pytest-html
    Update reports with screenshots - Beautiful Soup: pip install beautifulsoup4
    Excel (read/write) - pip install openpyxl
    Full size screenshots - pip install pillow pyscreeze pyautogui
   
Excel is used to describe the action, selector_type, selector, expected value, actual value and description for each action.
A separate Excel application, Commands.xlsm, that is not included with this application, due to source controls limiting it's alterability, is used to create separate Excel files(CommandScripts.xlsx) 
that are used by the application to perform one or more actions.
An additional Excel file, TestLogs.xlsx, with a single Sheet entitled Logs, also not included, serves as the LogFile for the application.

At the time of this writing, Actions in the Commands.xlsm and CommandScripts.xlsx files consist of the following Commands and similar but not exact Descriptions:  (Descriptions listed below are more robust for general understanding.)
Actions                                 |Description                                                                                                                |Display Value                           |
Navigate                                |Navigate to URL                                                                                                            |Page URL                                |
Check Page Tagging                      |Checks page tagging                                                                                                        |Checks page tagging                     |
Click                                   |Clicks the element based on the selector type and selector                                                                 |                                        |
Compare Text                            |Compares element text, based on the selector type and selector, against last Get Text that was saved                       |                                        |
Connect to Database                     |Provide Server Name and Database Name                                                                                      |Server=ServerName, Database=DatabaseName|
Get all xpath and css selectors         |Prints all element xPath and Css Selector values based on selector type and selector and saves them to the specified file  |File Path and File Name                 |
Get JSON from API                       |Gets JSON from the API endpoint                                                                                            |                                        |
Get table information                   |Prints table information based on the selector type and selector in vertical or horizontal orientation                     |Horizontal or Vertical print orientation|
Get Text                                |Gets the element text based on the selector type and selector                                                              |                                        |
Hover                                   |Hovers over the element based on the selector type and selector                                                            |                                        |
Perform WCAG ADA Checks                 |Checks all WCAG and ADA HTML elements with no selector type and selector or just elements indicated                        |                                        |
Print All Elements                      |Prints the text of all child elements based on the parent selector type and selector                                       |Print Child element values              |
Print Child Elements                    |Prints the text of all child elements based on the parent selector type and selector                                       |Print Child element values              |
Print Step Description                  |Prints the text provided to the output                                                                                     |Phrase to print                         |
Query Database                          |Write a SQL Query to return results                                                                                        |Select * from myTable where Id = 1      |
Refresh                                 |Refreshes the page resetting controls to initial values                                                                    |                                        |
Right Click                             |Right Clicks the element based on the selector type and selector                                                           |                                        |
Select All Elements                     |Selects all elements based on selector type and selector                                                                   |                                        |
Save complete har file                  |Saves one HAR file for all pages on the site and must be the last command                                                  |File Path and File Name                 |
Save HAR file                           |Saves the HAR contents to a file                                                                                           |File Path and File Name                 |
Select dropdown by value                |Select dropdown value based on the selector type and selector and value                                                    |                                        |
Send Keys                               |Sends keystroks to the element based on the selector type, selector and text to send                                       |Phrase/keys to send                     |
Switch to Window                        |Switches to a new window based on the window index                                                                         |1                                       |
Take Screenshot                         |Takes a screenshot                                                                                                         |File Path and File Name                 |
Wait                                    |Wait a specified time in seconds                                                                                           |5                                       |
Wait for clickable element              |Wait for the element based on the selector type and selector, to be clickable                                              |20                                      |
Wait for element presence               |Wait up to 20 seconds for the presence of an element based on the selector type and selector                               |20                                      |
Reset Sheet                             |Clears the Commands Sheet                                                                                                               |                                        |
                                        |                                                                                                                           |                                        |
                                        |                                                                                                                           |                                        |
                                        |                                                                                                                           |                                        |
                                        |                                                                                                                           |                                        |
                                        |                                                                                                                           |                                        |
                                        |                                                                                                                           |                                        |
                                        |                                                                                                                           |                                        |
                                        |                                                                                                                           |                                        |
                                        |                                                                                                                           |                                        |
                                        |                                                                                                                           |                                        |
                                        |                                                                                                                           |                                        |
                                        |                                                                                                                           |                                        |
                                        |                                                                                                                           |                                        |
                                        |                                                                                                                           |                                        |
                                        |                                                                                                                           |                                        |
                                        |                                                          

