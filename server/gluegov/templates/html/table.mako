<%inherit file="_base.mako"/>

<h1>${data.get('group')}: ${data.get('name')}</h1>

<table>

<%
    fields_fallback = []
    if data.get('list'):
        fields_fallback = tuple(data.get('list')[0].keys())
%>

% for field in data.get('fields') or fields_fallback:
<th>${field}</th>
% endfor

% for item in data.get('list'):
<tr>
% for field in data.get('fields') or fields_fallback:
<td>${item[field]}</td>
% endfor
</tr>
% endfor

</table>
