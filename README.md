This is a Configurable Automated Testing application that uses Python, Selenium and Excel.    
Excel is used to describe the action, selector_type, selector, expected value, actual value and description for each action.
A separate Excel application, Commands.xlsm, that is not included with this application, due to source controls limiting it's alterability, is used to create separate Excel files(CommandScripts.xlsx) 
that are used by the application to perform one or more actions.
An additional Excel file, TestLogs.xlsx, with a single Sheet entitled Logs, also not included, serves as the LogFile for the application.

At the time of this writing, Actions in the Commands.xlsm and CommandScripts.xlsx files consist of the following Commands and similar but not exact Descriptions:  (Descriptions listed below are more robust for general understanding.)
|Actions	                            |  Description|
|Navigate	                            |- Navigate to URL provided |
|Compare Text	                        |- Compares element text, based on the selector type and selector, against last Get Text that was saved |
|Click	                                |- Clicks the element based on the selector type and selector |
|Get all xpath and css selectors	    |- Prints all element xPath and Css Selector values based on selector type and selector and saves them to the specified file |
|Get JSON from API	                    |- Gets JSON from the API endpoint |
|Get table information					|- Prints table information based on the selector type and selector in vertical or horizontal orientation |
|Get Text	                            |- Gets the element text based on the selector type and selector |
|Hover	                                |- Hovers over the element based on the selector type and selector |
|Print All Elements	                    |- Prints the text of all child elements based on the parent selector type and selector |
|Print Child Elements	                |- Prints the text of all child elements based on the parent selector type and selector |
|Print Step Description	                |- Prints the text provided to the output |
|Refresh	                            |- Refreshes the page resetting controls to initial values |
|Right Click	                        |- Right Clicks the element based on the selector type and selector |
|Save complete har file					|- Saves one HAR file for all pages on the site and must be the last command |
|Save HAR file							|- Saves the HAR contents for the current page to a file (may depricate this in favor of the Save complete above)
|Select All Elements	                |- Selects all elements based on selector type and selector and prints them |
|Select dropdown by value	            |- Select dropdown value based on the selector type and selector and value |
|Send Keys	                            |- Sends keystroks to the element based on the selector type, selector and text to send |
|Switch to Window	                    |- Switches to a new window based on the window index |
|Take Screenshot	                    |- Takes a screenshot |
|Wait	                                |- Wait a specified time in seconds |
|Wait for clickable element	            |- Wait for the element based on the selector type and selector, to be clickable |
|Wait for element presence	            |- Wait up to 20 seconds(configurable but 20 is default if missing) for the presence of an element based on the selector type and selector |
|Reset Sheet	                        |- Clears the Commands Sheet |

