<%inherit file="_base.mako"/>

<h1>${data.get('group')}: ${data.get('name')}</h1>

<table>

%for field in data.get('fields', []):
<th>${field}</th>
% endfor

% for item in data.get('list'):
<tr>
% for field in data.get('fields', []):
<td>${item[field]}</td>
% endfor
</tr>
% endfor

</table>
