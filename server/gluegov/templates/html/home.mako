<%inherit file="_base.mako"/>

<h1>Project</h1>

<ul>
% for group in data.get('groups', []):
    <li><a href="${group}">${group}</a></li>
% endfor
</ul>
