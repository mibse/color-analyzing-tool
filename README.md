# About the color-analyzing-tool
The purpose of this tool is to calculate the percentage of colors contained in a given photo.
## Description
The user selects a photo whose color amounts are to be calculated. The user provides the tool with the Absolute file path of the photo, after which the user launches the program. The program ignores transparent pixels and combines similar colors into groups. As a final result, the program prints the colors contained in the photo and their proportion of the image in order of magnitude.
The program uses different technologies, such as Image, webcolors and threads. The reason for these is to process photo features, recognize colors and increase processing speed.
I encountered difficulties in writing the code, because handling images and colors were a completely new subject for me. The problem with identifying transparent pixels was that I didn't realize that pixels can have four values, the last of which tells if it is transparent. There was also an existing problem left, namely code execution speed. With large images (I used 1920 x 1080 images) the performance is slow, and on my own laptop it could take up to 20 minutes. Increasing the number of threads did not speed up the program, but I think on more powerful computers the program can run faster.


## Getting Started

### Dependencies

* Windows 10

### Installing

* Any modifications needed to be made to files/folders

### Executing program

* How to run the program
* Step-by-step bullets
