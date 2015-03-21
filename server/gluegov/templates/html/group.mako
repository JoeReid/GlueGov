<%inherit file="_base.mako"/>

<h1>group</h1>

<ul>
% for name, fields in data.get('tables', {}).items():
    <li>
        ${name}
        <ul>
        % for field in fields:
            <li>${field}</li>
        % endfor
        </ul>
    </li>
% endfor
</ul>
