import json
import string

with open("data.json") as f:
    data = json.loads(f.read())

content = ""
for idx, (author, title) in enumerate(data.items()):
    content += "<tr>"
    content += f"<td>{idx + 1}</td>"
    content += f"<td>{author}</td>"
    content += f"<td>{title}</td>"
    content += "</tr>"

with open("template.html") as t:
    template = string.Template(t.read())

final_output = template.safe_substitute(elements=content)
with open("report.html", "w") as output_file:
    output_file.write(final_output)
