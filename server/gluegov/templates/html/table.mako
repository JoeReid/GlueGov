<%inherit file="_base.mako"/>

<h1>table</h1>

<%
    keys = list(data.get('list')[0].keys()) if data.get('total', 0) > 0 else []
%>

<table>

%for key in keys:
<th>${key}</th>
% endfor

% for item in data.get('list'):
<tr>
% for key in keys:
<td>${item[key]}</td>
% endfor
</tr>
% endfor

</table>
