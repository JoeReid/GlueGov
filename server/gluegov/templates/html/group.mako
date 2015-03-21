<%inherit file="_base.mako"/>

<h1>${data.get('group')}</h1>

<ul>
% for name, fields in data.get('tables', {}).items():
    <li>
        <a href="${request.path}/${name}">${name}</a>
        <ul>
        % for field in fields:
            <li>${field}</li>
        % endfor
        </ul>
    </li>
% endfor
</ul>
