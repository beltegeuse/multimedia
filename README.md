# Multimedia website

The only requirement for building and testing the website is [Zola](https://www.getzola.org/). Several way to install `zola` on your computer: https://www.getzola.org/documentation/getting-started/installation/. 

After Zola installed on your computer, you can test the website on your local machine. For that, open a terminal:
```shell
zola serve
```
Open your browser at the URL given by the command line. You can edit the website content freely. Each time you save a file, the website will reload automatically. 

To build the website (for deployment only):
```shell
zola build
```
The website will be stored inside `public` directory. Copy the content on the web server. 

## Professor check list

Each professor's directory is inside `content/team/<prof-name>`. This directory contains the following files:

- `img.jpg`: the image displayed on the team webpage and professor card. The image is automatically resized internally. 
- `index.en.md` and `index.md`: markdown files controlling your information on the website (the two files are for providing the information in English and French). Please check Adrien's files for an example. There is two part to this file:
  - Parameter after `[extra]`: control the information shown on the team's main page 
  - Text after the last `+++`: control the information shown on your entry page (markdown format).
- `students.json` (optional): The list of students inside your research group. Each entry needs to have `name` and `type` (list: `intern`, `phd`, `master`). Please check the Adrien students.json file for an example.   
- `papers.bib` (optional): The list of published papers in BibTeX format. This file can be generated automatically by Google scholar (i.e., go to your google scholar profile, select all your publications and click on export). 

If you want to include some images, you can add them directly inside your own directory or inside `static/img`. 

