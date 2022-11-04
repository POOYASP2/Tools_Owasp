const raw_cookie = document.cookie + '; ';
const my_regxp = /(?<cookie>(?<name>[^=]+)=(?<value>[^;]+);\s*)/gm;
const matches = [...raw_cookie.matchAll(my_regxp)];
// I try show inside of document
let table = document.createElement("table");
table.setAttribute("id", "temp_table");
document.body.appendChild(table);
temp_table.appendChild(document.createElement("tr"));
let temp_tr = temp_table.firstChild;
temp_tr.appendChild(document.createElement("th"));
temp_tr.appendChild(document.createElement("th"));
temp_tr.firstChild.appendChild(document.createTextNode("key"));
temp_tr.lastChild.appendChild(document.createTextNode("value"));
//
matches.forEach(e=>{
    temp_tr = document.createElement('tr');
    temp_tr.appendChild(document.createElement('td'));
    temp_tr.appendChild(document.createElement('td'));
    temp_tr.firstChild.appendChild(document.createTextNode(e.groups.name));
    temp_tr.lastChild.appendChild(document.createTextNode(e.groups.value));
    temp_table.appendChild(temp_tr);
})
