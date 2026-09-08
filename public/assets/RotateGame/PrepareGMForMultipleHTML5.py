#https://www.reddit.com/r/gamemaker/comments/at4sf2/multiple_html5_games_on_a_single_webpage/

import re

path = "/Users/aradia/Documents/TEC/IC-TEC\ Large\ Files/2026/S-II/CG/Notes/CGNotes/src/assets/rotategame"
js_folder = "rotategame"
index_filename = "rotategame.html"
js_filename = "rotategame.js"
canvas_name = "rotategame"
div_name = "gm_div_rotategame"
js_init_function = "GameMaker_Init_rotategame"
js_wrapper_function = "game_rotategame"

output_index_filename = "index_rotategame_improved.html"
output_js_filename = "rotategame_improved.js"


# Step 1 - process index.html file to modify canvas and div IDs and eliminate window.onload
index_txt = []
with open(path+"\\"+index_filename,encoding='utf-8-sig') as f:
    for string in f.readlines():
        string = string.replace("\"canvas\"", "\""+canvas_name+"\"").replace("'canvas'", "\""+canvas_name+"\"").replace("gm4html5_div_id", div_name).replace(js_filename, output_js_filename)
        if string.find("<script>window.onload = GameMaker_Init;</script>") == -1:
            index_txt.append(string)

with open(path+"\\"+output_index_filename, "w", encoding='utf-8-sig') as f:
    f.writelines(index_txt)


# Step 2 - process js file
js_txt = []
js_txt.append("var "+js_wrapper_function+" = {}; "+js_wrapper_function+".launch = function() {\n\n")
with open(path+"\\"+js_folder+"\\"+js_filename,encoding='utf-8') as f:
    for string in f.readlines():
        t = re.search(r",([^,]*)='canvas'", string)        
        if (t != None):
            var1 = t.groups()[0]
            
        t = re.search(r"\;([^\;]*)=\"canvas\"", string)
        if (t != None):
            var2 = t.groups()[0]	

with open(path+"\\"+js_folder+"\\"+js_filename,encoding='utf-8-sig') as f: 
    for string in f.readlines():
        string = string.replace("gm4html5_div_id", div_name).replace("getElementById(\"canvas\")", "getElementById(\""+canvas_name+"\")").replace("getElementById('"+canvas_name+"'')", "getElementById(\""+canvas_name+"\")").replace("document.getElementById("+var1+")","document.getElementById(\""+canvas_name+"\")").replace("document.getElementById("+var2+")","document.getElementById(\""+canvas_name+"\")").replace("GameMaker_Init",js_init_function)
        
        js_txt.append(string)

js_txt.append("\n\n"+js_init_function+"()\n} \n\n"+js_wrapper_function+".launch()")

with open(path+"\\"+js_folder+"\\"+output_js_filename, "w", encoding='utf-8-sig') as f:
    f.writelines(js_txt)