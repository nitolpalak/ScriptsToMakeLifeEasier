# =========== Links2CSRF ===========

A script to convet api routes into CSRF include able format.

**Assumption:**
- The route will be in first column
- There is no header in the csv file
- Expected format of the output is '"/api/.....",'
- No '//' is expected in the output
- Need to keep the data until '?', '(', ' ' or '{' is found

**Process:**
- Takes input of a CSV file
- Perform following operations to the First data of each row:
  - Lower case the string
  - Strip the data until it finds '?', '(', ' ' or '{'
  - Adds a '/' if there is not any at the start of the route
  - Removes the '/' if there is any at the end of the route
  - Replaces any '//' with '/'
  - Remove all duplicate strings
  - Adds double quotation and comma separates them 
- Generates a text file containing the unique data

**Example:**
Converts a data like one of the following formats into '"/api/.....",'
- 'api//...?....'
- 'api/.../{param}/ (some description)'
- etc.
