This is a Configurable-Automated Testing application that uses Python, Selenium and Excel. 
    PyTest: pip install pytest
    html reports: pip install pytest-html
    Update reports with screenshots - Beautiful Soup: pip install beautifulsoup4
    Excel (read/write) - pip install openpyxl
    Full size screenshots - pip install pillow pyscreeze pyautogui
   
Excel is used to describe the action, selector_type, selector, expected value, actual value and description for each action.
A separate Excel application, Commands.xlsm, that is not included with this application, due to source controls limiting its alter-ability, 
is used to create separate Excel files(CommandScripts.xlsx with the tab of commands entitled CommandScripts) that are used by the application 
to perform one or more actions. 
See a list of commands below and a sample CommandScripts.xlsx file at the bottom showing how each command is used.

An additional Excel file, TestLogs.xlsx, with a single Sheet entitled Logs, also not included, serves as the LogFile for the application.

At the time of this writing, Actions in the Commands.xlsm and CommandScripts.xlsx files consist of the following Commands and similar but not exact Descriptions:  
(Descriptions listed below are more robust for general understanding.)
Actions                                 |Description                                                                                                                |Display Value                           |
Navigate                                |Navigate to URL                                                                                                            |Page URL                                |
Check Page Tagging                      |Checks page tagging                                                                                                        |Checks page tagging                     |
Click                                   |Clicks the element based on the selector type and selector                                                                 |                                        |
Close tab                               |Closes an open tab                                                                                                         |1                                       |
Compare Text                            |Compares element text, based on the selector type and selector, against last Get Text that was saved                       |                                        |
Connect to Database                     |Provide Server Name and Database Name                                                                                      |Server=ServerName, Database=DatabaseName|
Get all xpath and css selectors         |Prints all element xPath and Css Selector values based on selector type and selector and saves them to the specified file  |File Path and File Name                 |
Get JSON from API                       |Gets JSON from the API endpoint                                                                                            |                                        |
Get table information                   |Prints table information based on the selector type and selector in vertical or horizontal orientation                     |Horizontal or Vertical print orientation|
Get Text                                |Gets the element text based on the selector type and selector                                                              |                                        |
Hover                                   |Hovers over the element based on the selector type and selector                                                            |                                        |
Open link in new tab                    |Opens link url in new tab based on the parent selector type and selector                                                   |                                        |
Perform WCAG ADA Checks                 |Checks all WCAG and ADA HTML elements with no selector type and selector or just elements indicated                        |                                        |
Print All Elements                      |Prints the text of all child elements based on the parent selector type and selector                                       |Print Child element values              |
Print Child Elements                    |Prints the text of all child elements based on the parent selector type and selector                                       |Print Child element values              |
Print Step Description                  |Prints the text provided to the output                                                                                     |Phrase to print                         |
Query Database                          |Write a SQL Query to return results                                                                                        |Select * from myTable where Id = 1      |
Refresh                                 |Refreshes the page resetting controls to initial values                                                                    |                                        |
Right Click                             |Right Clicks the element based on the selector type and selector                                                           |Not implemented                         |
Select All Elements                     |Selects all elements based on selector type and selector                                                                   |                                        |
Save complete har file                  |Saves one HAR file for all pages on the site and must be the last command                                                  |File Path and File Name                 |
Save HAR file                           |Saves the HAR contents to a file                                                                                           |File Path and File Name                 |
Select dropdown by value                |Select dropdown value based on the selector type and selector and value                                                    |                                        |
Send Keys                               |Sends keystroks to the element based on the selector type, selector and text to send                                       |Phrase/keys to send                     |
Switch to Tab                           |Switches to a new tab based on the window index                                                                            |1                                       |
Take Screenshot                         |Takes a screenshot                                                                                                         |File Path and File Name                 |
Wait                                    |Wait a specified time in seconds                                                                                           |5                                       |
Wait for clickable element              |Wait for the element based on the selector type and selector, to be clickable                                              |20                                      |
Wait for element presence               |Wait up to 20 seconds for the presence of an element based on the selector type and selector                               |20                                      |
Retrieve Web Page                       |Retrieves Web Page HTML based on text_url field                                                                            |https://www.mycoolsite.com/             |
Retrieve Elements-List Properties       |Gets Retrieved page elements based on selector. Prints properties.                                                         |src,alt,srcset                          |
Save Web Page                           |Saves Web page retrieved or retrieves and saves it.                                                                        |https://www.mycoolsite.com/             |
Spider Site Save URLs                   |Spiders the site collecting all hrefs and building a list of links to save to a file.                                      |https://www.mycoolsite.com/             |
Reset Sheet                             |Clears the Commands Sheet                                                                                                  |                                        |
                                        |                                                                                                                           |                                        |
                                        |                                                                                                                           |                                        |

----------------------------------------------------------------------------------------------------------------
Sample Excel CommandScripts.xlsx file.  Tab must be named CommandScripts.
Simple rule to remember, if you are interacting with an element, you must provided the Selector_type and Selector for that element.
If you are attempting to compare a value, you must provide the Expected value in the Expected column.
The default value for comparing the URL after navigation is current_url.

Command                           |Selector_type   |Selector                           |Text or URL                            |Expected                      |Actual|Description (50 characters or less for best presentation results) |
Print Step Description            |                |                                   |========[ Start MySite Test ]==========|                              |      |Print start of test to run                                        |
Navigate                          |                |                                   |https://www.mycoolsite.com/en-us       |current_url                   |      |Navigate to URL & check that Navigate URL matches current url     |
Wait                              |                |                                   |3                                      |                              |      |Wait a specified time in seconds                                  |
Click                             |id              |onetrust-accept-btn-handler        |                                       |                              |      |Click to close OneTrust banner                                    |
Wait                              |                |                                   |3                                      |                              |      |Wait a specified time in seconds                                  |
Get Text                          |Tag_Name        |h1                                 |                                       |My Cool Website               |      |Print the test of the element specified                           |
Compare Text                      |id              |title                              |                                       |                              |      |Compares element text, against last Get Text value                |
Print Child Elements              |xpath           |(//ul[@id='productList'])/li       |                                       |                              |      |Prints child elements based on the selector                       |
Hover                             |xpath           |(//span[contains(text(),'Men')])[1]|                                       |                              |      |Hovers over element based on selector                             |
Get table information             |id              |resultTable                        |                                       |                              |      |Gets all table information                                        |
Perform WCAG ADA Checks           |                |                                   |                                       |                              |      |Checks all WCAG & ADA HTML elements                               |
Perform WCAG ADA Checks           |CSS_SELECTOR    |img                                |                                       |alt,id,name                   |      |Check WCAG and ADA for img elements only.                         |
Send Keys                         |id              |name                               |tester                                 |                              |      |Send the word tester to the name field (sends keystrokes)         |
Print All Elements                |css_selector    |#listbox                           |                                       |                              |      |Prints all listbox options                                        |
Select All Elements               |css_selector    |#listbox > option                  |                                       |                              |      |Selects all listbox option elements                               |
Get all xpath and css selectors   |css_selector    |input, select                      |mycoolsite_input_and_selects.txt       |                              |      |Prints & Saves to file all matching element xPath & Css selectors.|
Get table information             |id              |resultTable                        |horizontal                             |20                            |      |Get and Print table information horizontally                      |
Get table information             |id              |resultTable                        |vertical                               |                              |      |Get and Print table information vertically                        |
Save complete har file            |                |                                   |mycoolsite_complete_har.txt            |                              |      |Saves one HAR file for all pages visited. Must be last command.   |
Check Page Tagging                |google-analytics|                                   |                                       |en=page_view,tid=G-SV00000000 |      |Checks Page Analytics/Media tags(google-analytics)                |
Check Page Tagging                |facebook        |                                   |                                       |ev=PageView,id=300000000000000|      |Checks Page Analytics/Media tagss(facebook)                       |
Check Page Tagging                |google-analytics|                                   |har_files\mycoolsite_har_file.txt      |en=page_view,tid=G-SV00000000 |      |Checks Tags in saved har file (filename in text_url field)        |
Check Page Tagging                |facebook        |                                   |har_files\mycoolsite_har_file.txt      |ev=PageView,id=300000000000000|      |Checks Tags in saved har files (filename in text_url field)       |
Refresh                           |                |                                   |                                       |                              |      |Refreshes the page resetting controls to initial values           |
Wait for clickable element        |id              |resultTable                        |20                                     |                              |      |Wait up to 20 seconds for the element to be clickable             |
Wait for element presence         |id              |resultTable                        |20                                     |                              |      |Wait up to 20 seconds for the presence of an element              |
Open link in new tab              |css_selector    |a#shoeselection                    |                                       |                              |      |Opens link url in new tab based selector type and selector        |
Wait                              |                |                                   |3                                      |                              |      |Wait a specified time in seconds                                  |
Switch to Tab                     |                |                                   |1                                      |                              |      |Switches to a new tab based on the window index                   |
Take Screenshot                   |                |                                   |./screenshots/mycoolsite.png           |                              |      |Take screenshot and save it to file listed in text_url field.     |
Close tab                         |                |                                   |1                                      |                              |      |Closes an open tab                                                |
Select dropdown by value          |css_selector    |#jacketsize                        |large                                  |                              |      |Select dropdown value based on and text_url value.                |
Get JSON from API                 |                |                                   |https://mycoolsite.com/en-us/projects  |                              |      |Gets JSON from the API endpoint                                   |
Connect to Database               |                |                                   |Server=MySqlServer, Database=GameStore |                              |      |Provide Server Name and Database Name                             |
Query Database                    |                |                                   |Select * from [Games]                  |                              |      |Retrieve all Games                                                |
Retrieve Web Page                 |                |                                   |https://mycoolsite.com/                |                              |      |Retrieves Web Page HTML based on text_url field                   | 
Save Web Page                     |                |                                   |https://mycoolsite.com/                |                              |      |Saves/Retrieves Web page to data folder with valid name from URL. |
Retrieve Elements-List Properties |tag_name        |img                                |src,alt,srcset                         |TRUE                          |      |Gets Retrieved page elements based on selector. Prints properties.|
Spider Site Save URLs             |                |                                   |https://mycoolsite.com/                |mycool_site_links.txt         |      |Spiders site gets all hrefs and saves them to a file.             |