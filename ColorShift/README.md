# Final Exam 2017 - IS 537

Welcome to the IS 537 Final Exam! Here are the rules of the exam:

* You are limited to 3 hours, start to finish.  Please time yourself.
* The exam is closed neighbor, but you are welcome to search the internet, use past projects, etc.  Please do not simply copy code directly from the Internet.
* When you are finished, fill out the rubric below with your best estimate of how you did on the final.  This sets my expectations when I grade it.

## Setup

In a terminal window, run `pip3 install -r pip-requirements.txt` to install the requirements of the project. The requirements are minimal: the most recent versions of Django and DMP.

The project should run immediately, even though some code is missing.  The functions with missing code (the part you need to complete) have enough of a "stub" to allow the project to run.  Be sure to run the project before you modify anything so you know it runs as expected.  Once the server is running, take a browser to `http://localhost:8000/`.

The project should show all gray circles (`#808080`) because the stub methods aren't doing what they should yet.  This will change as you complete the final.

## Structure

The project contains a single view, `/homepage/views/index.py` that contains a color entry form.  Nothing needs to be changed in this file, but be sure to look at this file first to get a sense for the program flow.  You can assume the user will enter a valid color (no need for validation).

When a color is submitted, the view converts the hex code into an integer.  For example, the hex code `AABBCC` would convert to the integer `11189196`.  This integer (not the hex code) is then used throughout the rest of the view.  The program further separates this number into the R, G, B integers.  The values for `11189196` are `(170, 187, 204)`.  

The program steps through the `OPERATIONS` list to create the adjusted colors.  On each operation, it adjusts the three individual colors and combines the results into a new integer.  The results are stored in `ColorTile` objects, which are then displayed on the web page.

Once created, `color_tiles` (the list of result tiles) is sorted by the luma value (a measure of brightness).  We now have two lists: the original tile list `color_tiles` and the sorted tile list `color_tiles2`.  These are each displayed on the template.

Stop here and look at the files in `/homepage/lib/`.  These are the support functions that do most of the work, and these are where you need to spend your time.  Many of these functions are "empty" and require your expertise.


## Tasks

You need to complete five functions:

* Four functions in `/homepage/lib/color_utils.py`
* One function in `/homepage/lib/color_sort.py`

The only modifications you need to make should be in these two files.  Replace the current "stub" implementations in the functions with your own code.

See the individual functions for detail on what needs to be done.

## Rubric

Please **fill out the following** with your expected grades on the following:

| Function       | Task                                                   |  Score  | Possible |
|----------------|--------------------------------------------------------|--------:|---------:|
| `separate_rgb` | function uses bit masking correctly                    |       5 |        5 |
| `separate_rgb` | function uses bit shifting correctly                   |       5 |        5 |
| `separate_rgb` | return value is correct                                |       5 |        5 |
| `combine_rgb`  | function uses bit shifting correctly                   |       5 |        5 |
| `combine_rgb`  | return value is correct                                |       5 |        5 |
| `adjust_color` | num is adjusted higher or lower (based on the percent) |       5 |        5 |
| `adjust_color` | return value cannot be below 0                         |       5 |        5 |
| `adjust_color` | return value cannot be above 255                       |       5 |        5 |
| `adjust_color` | return value is an integer (not a float)               |       5 |        5 |
| `calc_luma`    | formula is correctly implemented                       |       10|       10 |
| `calc_luma`    | return value is an integer (not a float)               |       5 |        5 |
| `luma_sort`    | counting list created with empty sublists              |       10|       10 |
| `luma_sort`    | counting list size is correct                          |       5 |        5 |
| `luma_sort`    | iteration places tiles into counting list              |       10|       10 |
| `luma_sort`    | counting list is flattened into results list           |       10|       10 |
| `luma_sort`    | returns value is a new list, sorted by luma            |       5 |        5 |
| Final Score    |                                                        |      100|      100 |
