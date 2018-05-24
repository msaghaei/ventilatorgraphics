from pathlib import Path

file_name = input("File name: ")
file_name = file_name.replace(" ", "_").lower()
path = Path(file_name + ".html")
if path.exists():
    print(file_name + " already exists!")
    exit()
page_title = input("title: ")
data = open("page_template.html").read()
data = data.replace("$$page_id$$", file_name).replace("$$page_title$$", page_title)
out_file = open(file_name + ".html", "w")
out_file.write(data)
out_file.flush()
out_file.close()
link_str = """<li>
                        <a href="$$page_id$$.html">
                    $$page_title$$
                        </a>
                    </li>
                    $$LI$$"""
index_data = open("index.html").read()
new_li = link_str.replace("$$page_id$$", file_name).replace("$$page_title$$", page_title)
index_data = index_data.replace("$$LI$$", new_li, 1)
f = open("index.html", "w")
f.write(index_data)
f.flush()
f.close()
